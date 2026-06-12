from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "prepare_blind_review.py"


def write(path: Path, text: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_fake_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    write(
        repo / "docs" / "experiment-results.html",
        """
        <table>
          <tr>
            <td><img src="../datasets/assets/char/renders/char.png"><div class="path">datasets/assets/char/renders/char.png</div></td>
            <td><img src="../datasets/assets/pose/renders/pose.png"><div class="path">datasets/assets/pose/renders/pose.png</div></td>
            <td>
              <strong>提交</strong>E001 run1（r001）
              <strong>模型</strong>test model
              <strong>prompt</strong><span class="prompt-text">make character do pose</span>
              <div class="run-note"><strong>备注</strong>do not copy me</div>
            </td>
            <td><img src="../experiments/E001/runs/r001/outputs/a.png"><div class="path">experiments/E001/runs/r001/outputs/a.png</div></td>
            <td><img src="../experiments/E001/runs/r001/outputs/b.png"><div class="path">experiments/E001/runs/r001/outputs/b.png</div></td>
          </tr>
        </table>
        """,
    )
    write(repo / "datasets" / "assets" / "char" / "renders" / "char.png")
    write(repo / "datasets" / "assets" / "char" / "renders" / "char-side.png")
    write(repo / "datasets" / "assets" / "pose" / "renders" / "pose.png")
    write(repo / "experiments" / "E001" / "runs" / "r001" / "outputs" / "a.png")
    write(repo / "experiments" / "E001" / "runs" / "r001" / "outputs" / "b.png")

    write(
        repo / "experiments" / "E002" / "case.yaml",
        """
case_id: E002
character_input:
  render: datasets/assets/char/renders/char.png
character_inputs:
  - render: datasets/assets/char/renders/char.png
  - render: datasets/assets/char/renders/char-side.png
pose_reference:
  render: datasets/assets/pose/renders/pose.png
        """,
    )
    write(
        repo / "experiments" / "E002" / "runs" / "r003" / "run.yaml",
        """
run_id: r003
case_id: E002
model_tool: "fallback model"
prompt: experiments/E002/runs/r003/prompt.md
outputs_dir: experiments/E002/runs/r003/outputs/
notes: "do not copy me either"
        """,
    )
    write(
        repo / "experiments" / "E002" / "runs" / "r003" / "prompt.md",
        "# Prompt\n\nImages 1-2 = CHARACTER SOURCES. Image 3 = POSE SOURCE. Do not swap these roles.",
    )
    write(repo / "experiments" / "E002" / "runs" / "r003" / "outputs" / "out.png")

    write(repo / "experiments" / "_template" / "runs" / "r001" / "outputs" / "ignore.png")
    return repo


def run_script(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--repo-root", str(repo), *args],
        cwd=repo,
        check=False,
        text=True,
        capture_output=True,
    )


def test_all_index_prepares_each_real_run_without_template(tmp_path: Path) -> None:
    repo = make_fake_repo(tmp_path)

    result = run_script(repo, "--all", "--index")

    assert result.returncode == 0, result.stderr
    review_one = repo / "records" / "blind-reviews" / "E001-r001-blind-review.md"
    review_two = repo / "records" / "blind-reviews" / "E002-r003-blind-review.md"
    index = repo / "records" / "blind-reviews" / "index.md"
    assert review_one.exists()
    assert review_two.exists()
    assert not (repo / "records" / "blind-reviews" / "_template-r001-blind-review.md").exists()
    assert "do not copy me" not in review_one.read_text(encoding="utf-8")
    assert "make character do pose" in review_one.read_text(encoding="utf-8")
    review_two_text = review_two.read_text(encoding="utf-8")
    assert "Images 1-2 = CHARACTER SOURCES" in review_two_text
    assert "### Input 1: Character Source 1" in review_two_text
    assert "### Input 2: Character Source 2" in review_two_text
    assert "### Input 3: Pose Source 1" in review_two_text
    index_text = index.read_text(encoding="utf-8")
    assert "E001/r001" in index_text
    assert "E002/r003" in index_text
    assert "Start isolated review" in index_text
    assert "Do not read docs/experiment-results.html notes" in index_text


def test_all_does_not_overwrite_existing_review_without_overwrite(tmp_path: Path) -> None:
    repo = make_fake_repo(tmp_path)
    review = repo / "records" / "blind-reviews" / "E001-r001-blind-review.md"
    write(review, "# Blind Review: E001/r001\n\n- Best candidate: Candidate B\n")

    result = run_script(repo, "--all", "--index")

    assert result.returncode == 0, result.stderr
    assert review.read_text(encoding="utf-8") == "# Blind Review: E001/r001\n\n- Best candidate: Candidate B\n"
    assert "skipped_existing" in result.stdout
