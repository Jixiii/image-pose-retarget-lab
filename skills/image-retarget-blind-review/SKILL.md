---
name: image-retarget-blind-review
description: Project-local workflow for blind-reviewing image pose-retarget experiment runs in this repository. Use when the user asks to test/analyze a run such as "测试E001r001", "测试 E011 r002", or wants Codex to read docs/experiment-results.html, inspect the corresponding input/output images, identify per-candidate visual errors, and write the result to Markdown before any confirmed update to docs/experiment-results.html.
---

# Image Retarget Blind Review

Use this project-local skill to evaluate whether a vision model or Codex can understand pose-retarget outputs without seeing the user's prior notes.

## Workflow

1. Parse the requested run id, accepting compact forms like `E001r001`, `E001 r001`, or `E001 run1`.
2. For one run, run the helper from the repository root:

   ```bash
   python3 skills/image-retarget-blind-review/scripts/prepare_blind_review.py E001r001
   ```

3. For stage-one queue setup, prepare every real run and an index:

   ```bash
   python3 skills/image-retarget-blind-review/scripts/prepare_blind_review.py --all --index
   ```

4. The helper reads `docs/experiment-results.html` first. If the HTML row is incomplete, it falls back to `experiments/<case>/case.yaml`, `experiments/<case>/runs/<run>/run.yaml`, `prompt.md`, and `outputs/`.
5. The helper writes Markdown drafts under `records/blind-reviews/<case>-<run>-blind-review.md` with task images, candidate images, an isolated-review prompt, and an empty analysis form.
6. With `--all`, existing review files are skipped unless `--overwrite` is provided. This protects already-filled blind analyses.
7. Inspect the listed images directly. Do not read or use `run.yaml` notes, HTML remarks, or previous human notes before writing the blind review.
8. Fill the Markdown with concrete per-candidate errors. Do not modify `docs/experiment-results.html` unless the user confirms the blind review should be recorded there.

## Isolation Rule

Use one fresh conversation per run. Within a run, compare all candidates together. Across runs, do not reuse context, conclusions, or previous blind-review files.

The generated `records/blind-reviews/index.md` contains a copyable prompt for each run. Use that prompt in a fresh conversation and restrict the analysis to the named review packet plus linked images.

## Review Criteria

Prioritize task correctness over visual attractiveness:

1. Role separation: the output should use the character source identity, not the pose source identity.
2. Pose match: limbs, torso, stance, body orientation, and weight-bearing structure should match the pose source.
3. Viewpoint and framing: camera view, body-facing direction, centering, and full-body visibility should match the task.
4. Left/right correctness: do not mirror or swap left and right limbs.
5. Identity and style preservation: body proportions, colors, materials, hairstyle, outfit, and accessories should remain from the character source.
6. Artifact control: no extra limbs, missing limbs, broken hands/feet, distorted body parts, or malformed accessories.

Use these tags when helpful:

`pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

## Output Discipline

- Keep the review blind: omit human notes from the analysis section.
- Choose a best candidate only after describing every candidate.
- If all candidates are flawed, choose the least bad one and say it is only relatively best.
- Save the analysis in the generated Markdown file first; later synchronization into `docs/experiment-results.html` is a separate user-confirmed step.
