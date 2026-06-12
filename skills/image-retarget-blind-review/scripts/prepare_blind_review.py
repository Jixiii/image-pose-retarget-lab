#!/usr/bin/env python3
"""Prepare blind-review Markdown drafts for image-retarget runs."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
from pathlib import Path


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def parse_target(raw: str) -> tuple[str, str]:
    compact = raw.strip()
    match = re.search(r"(?i)e\s*0*(\d+)\s*(?:[-_/ ]|run|r)*\s*(?:run|r)?\s*0*(\d+)", compact)
    if not match:
        raise ValueError(f"Could not parse run target: {raw!r}")
    return f"E{int(match.group(1)):03d}", f"r{int(match.group(2)):03d}"


def find_repo_root(start: Path) -> Path:
    for candidate in [start.resolve(), *start.resolve().parents]:
        if (candidate / "docs" / "experiment-results.html").exists() and (candidate / "experiments").exists():
            return candidate
    raise FileNotFoundError("Could not find repo root with docs/experiment-results.html and experiments/")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_tags(fragment: str) -> str:
    text = re.sub(r"<[^>]+>", "", fragment)
    return html.unescape(text).strip()


def normalize_path(path: str) -> str:
    path = html.unescape(path).strip()
    while path.startswith("../"):
        path = path[3:]
    while path.startswith("./"):
        path = path[2:]
    return path


def natural_key(value: str) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", value)]


def find_html_row(repo_root: Path, case_id: str, run_id: str) -> str | None:
    html_text = read_text(repo_root / "docs" / "experiment-results.html")
    rows = re.findall(r"<tr\b[^>]*>(.*?)</tr>", html_text, flags=re.S | re.I)
    for row in rows:
        plain = strip_tags(row)
        if case_id in plain and run_id in plain:
            return row
    return None


def extract_html_row_data(repo_root: Path, case_id: str, run_id: str) -> dict[str, object]:
    row = find_html_row(repo_root, case_id, run_id)
    if row is None:
        return {}

    path_divs = [normalize_path(value) for value in re.findall(r'<div class="path">\s*(.*?)\s*</div>', row, flags=re.S | re.I)]
    srcs = [normalize_path(value) for value in re.findall(r'<img[^>]+src="([^"]+)"', row, flags=re.S | re.I)]
    paths = path_divs or srcs

    output_prefix = f"experiments/{case_id}/runs/{run_id}/outputs/"
    output_paths = [path for path in paths if path.startswith(output_prefix)]
    input_paths = []
    seen = set()
    for path in paths:
        if path.startswith(output_prefix) or path in seen:
            continue
        if Path(path).suffix.lower() in IMAGE_EXTS:
            input_paths.append(path)
            seen.add(path)

    prompt_match = re.search(r'<span class="prompt-text">\s*(.*?)\s*</span>', row, flags=re.S | re.I)
    prompt_text = strip_tags(prompt_match.group(1)) if prompt_match else ""

    model_match = re.search(r"<strong>模型</strong>\s*([^<]+)", row, flags=re.S)
    model_text = strip_tags(model_match.group(1)) if model_match else ""

    return {
        "source": "docs/experiment-results.html",
        "input_paths": input_paths,
        "output_paths": output_paths,
        "prompt_text": prompt_text,
        "model": model_text,
    }


def extract_render_paths_from_yaml_text(text: str) -> list[str]:
    paths = []
    for line in text.splitlines():
        match = re.match(r"\s*(?:-\s*)?render:\s*['\"]?([^'\"]+)['\"]?\s*$", line)
        if match:
            paths.append(match.group(1).strip())
    return paths


def scalar_from_yaml_text(text: str, key: str) -> str:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.*?)\s*$", text)
    if not match:
        return ""
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value


def fallback_data(repo_root: Path, case_id: str, run_id: str) -> dict[str, object]:
    case_file = repo_root / "experiments" / case_id / "case.yaml"
    run_dir = repo_root / "experiments" / case_id / "runs" / run_id
    run_file = run_dir / "run.yaml"
    output_dir = run_dir / "outputs"

    input_paths: list[str] = []
    prompt_text = ""
    model_text = ""

    for yaml_file in [run_file, case_file]:
        if yaml_file.exists():
            text = read_text(yaml_file)
            for render_path in extract_render_paths_from_yaml_text(text):
                if render_path not in input_paths:
                    input_paths.append(render_path)
            if yaml_file == run_file:
                model_text = scalar_from_yaml_text(text, "model_tool")
                prompt_ref = scalar_from_yaml_text(text, "prompt")
                if prompt_ref:
                    prompt_file = repo_root / prompt_ref
                    if prompt_file.exists():
                        prompt_text = strip_prompt_markdown(read_text(prompt_file))

    prompt_file = run_dir / "prompt.md"
    if not prompt_text and prompt_file.exists():
        prompt_text = strip_prompt_markdown(read_text(prompt_file))

    output_paths = []
    if output_dir.exists():
        output_paths = [
            str(path.relative_to(repo_root))
            for path in sorted(output_dir.iterdir(), key=lambda p: natural_key(p.name))
            if path.is_file() and path.suffix.lower() in IMAGE_EXTS
        ]

    return {
        "source": "experiments fallback",
        "input_paths": input_paths,
        "output_paths": output_paths,
        "prompt_text": prompt_text,
        "model": model_text,
    }


def strip_prompt_markdown(text: str) -> str:
    lines = [line for line in text.splitlines() if line.strip() and not line.strip().startswith("#")]
    return "\n".join(lines).strip()


def merge_data(primary: dict[str, object], fallback: dict[str, object]) -> dict[str, object]:
    merged = dict(fallback)
    for key, value in primary.items():
        if value:
            merged[key] = value
    if primary.get("input_paths") and fallback.get("input_paths"):
        # HTML order matches the visible review page, so keep it.
        merged["input_paths"] = primary["input_paths"]
    if primary.get("output_paths") and fallback.get("output_paths"):
        merged["output_paths"] = primary["output_paths"]
    return merged


def image_block(repo_root: Path, rel_path: str, label: str) -> str:
    abs_path = repo_root / rel_path
    return f"### {label}\n\n![{label}]({abs_path})\n\n`{rel_path}`\n"


def parse_prompt_roles(prompt_text: str) -> dict[int, str]:
    roles: dict[int, str] = {}
    pattern = re.compile(
        r"\bImages?\s+(\d+)(?:\s*-\s*(\d+))?\s*=\s*(CHARACTER|POSE)\s+SOURCES?\b",
        flags=re.I,
    )
    for match in pattern.finditer(prompt_text):
        start = int(match.group(1))
        end = int(match.group(2) or start)
        role = match.group(3).lower()
        for index in range(start, end + 1):
            roles[index] = role
    return roles


def input_role_labels(count: int, prompt_text: str) -> list[str]:
    prompt_roles = parse_prompt_roles(prompt_text)
    roles = []
    for index in range(1, count + 1):
        roles.append(prompt_roles.get(index) or ("character" if index == 1 else "pose"))

    character_total = roles.count("character")
    character_index = 0
    pose_index = 0
    labels = []
    for role in roles:
        if role == "character":
            character_index += 1
            labels.append("Character Source" if character_total == 1 else f"Character Source {character_index}")
        else:
            pose_index += 1
            labels.append(f"Pose Source {pose_index}")
    return labels


def review_path(repo_root: Path, case_id: str, run_id: str) -> Path:
    return repo_root / "records" / "blind-reviews" / f"{case_id}-{run_id}-blind-review.md"


def isolated_review_prompt(repo_root: Path, case_id: str, run_id: str) -> str:
    rel_review = review_path(repo_root, case_id, run_id).relative_to(repo_root)
    return "\n".join(
        [
            "Use the project-local skill at `skills/image-retarget-blind-review`.",
            f"Review only `{rel_review}` and the images linked inside it.",
            "Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.",
            "Fill only the Blind Analysis and Best Candidate sections.",
            "Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.",
        ]
    )


def write_review(repo_root: Path, case_id: str, run_id: str, data: dict[str, object], overwrite: bool) -> Path:
    output_dir = repo_root / "records" / "blind-reviews"
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = review_path(repo_root, case_id, run_id)
    if out_path.exists() and not overwrite:
        raise FileExistsError(f"{out_path} already exists. Re-run with --overwrite to replace the draft.")

    input_paths = list(data.get("input_paths") or [])
    output_paths = list(data.get("output_paths") or [])
    prompt_text = str(data.get("prompt_text") or "").strip()
    model_text = str(data.get("model") or "").strip()
    source = str(data.get("source") or "")

    if not input_paths:
        raise ValueError(f"No input images found for {case_id}/{run_id}.")
    if not output_paths:
        raise ValueError(f"No output images found for {case_id}/{run_id}.")

    labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts = [
        f"# Blind Review: {case_id}/{run_id}",
        "",
        "## Metadata",
        "",
        f"- Created: {now}",
        f"- Source used for image collection: `{source}`",
        f"- Model/tool from record: `{model_text or 'unknown'}`",
        "- Human notes: intentionally not copied into this blind-review draft.",
        "",
        "## Start Isolated Review",
        "",
        "Copy this prompt into a fresh Codex conversation for this run only:",
        "",
        "```text",
        isolated_review_prompt(repo_root, case_id, run_id),
        "```",
        "",
        "## Task",
        "",
        "Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.",
        "",
        "### Generation Prompt",
        "",
        "```text",
        prompt_text or "(No prompt text found.)",
        "```",
        "",
        "### Input Role Assumption",
        "",
        "- Input 1 is treated as the character source unless the visible record clearly says otherwise.",
        "- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.",
        "",
        "## Inputs",
        "",
    ]

    role_labels = input_role_labels(len(input_paths), prompt_text)
    for index, rel_path in enumerate(input_paths, start=1):
        parts.append(image_block(repo_root, rel_path, f"Input {index}: {role_labels[index - 1]}"))

    parts.extend(
        [
            "## Candidate Outputs",
            "",
        ]
    )
    for index, rel_path in enumerate(output_paths):
        label = labels[index]
        parts.append(image_block(repo_root, rel_path, f"Candidate {label}"))

    parts.extend(
        [
            "## Blind Analysis",
            "",
            "Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.",
            "",
        ]
    )

    for index, _ in enumerate(output_paths):
        label = labels[index]
        parts.extend(
            [
                f"### Candidate {label}",
                "",
                "- Correct:",
                "- Problems:",
                "- Failure tags:",
                "- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality =",
                "- Acceptable:",
                "- Reason:",
                "",
            ]
        )

    parts.extend(
        [
            "## Best Candidate",
            "",
            "- Best candidate:",
            "- Reason:",
            "- Overall observation:",
            "",
            "## Post-Review Comparison",
            "",
            "After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.",
            "",
        ]
    )

    out_path.write_text("\n".join(parts), encoding="utf-8")
    return out_path


def discover_run_targets(repo_root: Path) -> list[tuple[str, str]]:
    targets: set[tuple[str, str]] = set()
    experiments_dir = repo_root / "experiments"
    if not experiments_dir.exists():
        return []
    for outputs_dir in experiments_dir.glob("E*/runs/r*/outputs"):
        if "_template" in outputs_dir.parts:
            continue
        if not outputs_dir.is_dir():
            continue
        if not any(path.is_file() and path.suffix.lower() in IMAGE_EXTS for path in outputs_dir.iterdir()):
            continue
        run_dir = outputs_dir.parent
        case_dir = run_dir.parent.parent
        if re.fullmatch(r"E\d+", case_dir.name) and re.fullmatch(r"r\d+", run_dir.name):
            targets.add((f"E{int(case_dir.name[1:]):03d}", f"r{int(run_dir.name[1:]):03d}"))
    return sorted(targets, key=lambda item: (natural_key(item[0]), natural_key(item[1])))


def load_run_data(repo_root: Path, case_id: str, run_id: str) -> dict[str, object]:
    html_data = extract_html_row_data(repo_root, case_id, run_id)
    file_data = fallback_data(repo_root, case_id, run_id)
    return merge_data(html_data, file_data)


def prepare_one(repo_root: Path, case_id: str, run_id: str, overwrite: bool, skip_existing: bool) -> tuple[str, Path, str]:
    out_path = review_path(repo_root, case_id, run_id)
    if out_path.exists() and not overwrite and skip_existing:
        return "skipped_existing", out_path, f"{case_id}/{run_id}"
    data = load_run_data(repo_root, case_id, run_id)
    written = write_review(repo_root, case_id, run_id, data, overwrite)
    return "written", written, f"{case_id}/{run_id}"


def write_index(repo_root: Path, targets: list[tuple[str, str]], statuses: dict[tuple[str, str], str]) -> Path:
    output_dir = repo_root / "records" / "blind-reviews"
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "index.md"
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts = [
        "# Blind Review Index",
        "",
        f"- Updated: {now}",
        "- Purpose: stage-one isolated per-run VLM selector tests.",
        "- Rule: one run per fresh conversation; do not reuse context across runs.",
        "",
        "## Queue",
        "",
    ]
    for case_id, run_id in targets:
        rel_review = review_path(repo_root, case_id, run_id).relative_to(repo_root)
        status = statuses.get((case_id, run_id), "pending")
        parts.extend(
            [
                f"### {case_id}/{run_id}",
                "",
                f"- Status: `{status}`",
                f"- Review packet: `{rel_review}`",
                "- Start isolated review:",
                "",
                "```text",
                isolated_review_prompt(repo_root, case_id, run_id),
                "```",
                "",
            ]
        )
    out_path.write_text("\n".join(parts), encoding="utf-8")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", help="Run target such as E001r001, E001 r001, or E001 run1")
    parser.add_argument("--repo-root", type=Path, default=None, help="Repository root. Defaults to auto-detection from cwd.")
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing blind-review Markdown draft.")
    parser.add_argument("--all", action="store_true", help="Prepare blind-review drafts for every real experiment run.")
    parser.add_argument("--index", action="store_true", help="Write records/blind-reviews/index.md with isolated review prompts.")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve() if args.repo_root else find_repo_root(Path.cwd())

    if args.all:
        targets = discover_run_targets(repo_root)
        statuses: dict[tuple[str, str], str] = {}
        for case_id, run_id in targets:
            status, path, label = prepare_one(repo_root, case_id, run_id, args.overwrite, skip_existing=True)
            statuses[(case_id, run_id)] = status
            print(f"{status}: {label} -> {path}")
        if args.index:
            index_path = write_index(repo_root, targets, statuses)
            print(f"index: {index_path}")
        return 0

    if not args.target:
        parser.error("target is required unless --all is used")

    case_id, run_id = parse_target(args.target)
    status, out_path, _ = prepare_one(repo_root, case_id, run_id, args.overwrite, skip_existing=False)
    print(out_path if status == "written" else f"{status}: {out_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
