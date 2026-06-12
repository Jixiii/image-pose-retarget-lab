# Blind Review: E001/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nanobanana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E001-r002-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
生成第一张图的角色做第二张图角色的动作的图片。
```

### Input Role Assumption

- Input 1 is treated as the character source unless the visible record clearly says otherwise.
- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.

## Inputs

### Input 1: Character Source

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/y_bot/renders/Y-bot-Apose-front.png)

`datasets/assets/y_bot/renders/Y-bot-Apose-front.png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-pose1.png)

`datasets/assets/Body-Block/renders/body-block-pose1.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E001/runs/r002/outputs/ai_generate_7382_1.png)

`experiments/E001/runs/r002/outputs/ai_generate_7382_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E001/runs/r002/outputs/ai_generate_7382_2.png)

`experiments/E001/runs/r002/outputs/ai_generate_7382_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E001/runs/r002/outputs/ai_generate_7382_3.png)

`experiments/E001/runs/r002/outputs/ai_generate_7382_3.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the Y-bot character identity and material style. The output is full-body, with both feet visible, bent knees, raised forearms, and hands near the face/chest like the pose source. The screen-left leg remains the more forward/extended leg, so the coarse left/right layout is mostly preserved.
- Problems: Torso and camera view are more front-facing and upright than the pose source. The hands and wrists are crowded around the face, making the exact wrist/finger structure hard to recover. The lower-body weight shift is weaker than the pose source, and the feet/ankles are slightly distorted.
- Failure tags: `pose_mismatch`, `view_mismatch`, `body_deformation`, `accessory_deformed`.
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 3/5 / 4/5 / 4.5/5 / 4/5 / 3/5
- Acceptable: Borderline.
- Reason: The main skeleton is recoverable, but the raised-hand area and lower-body weight-bearing pose are not clean enough for a strong 3D pose recovery target.

### Candidate B

- Correct: Keeps the Y-bot identity and shows the complete body. The raised elbows, bent forearms, hands near the mouth/chest, bent knees, and screen-left extended leg are the closest overall match to the pose source. The shoulders, elbows, hips, knees, ankles, and feet are mostly visible and separable.
- Problems: Still too front-facing compared with the pose source, and the torso lean/weight shift is under-expressed. The hands and fingers are cluttered and deformed, with some ambiguity in the wrist positions. The armature-like gray elements partially occlude the head and upper torso.
- Failure tags: `pose_mismatch`, `view_mismatch`, `body_deformation`, `accessory_deformed`.
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4/5 / 3.5/5 / 4/5 / 4.5/5 / 4/5 / 3.5/5
- Acceptable: Yes.
- Reason: It has the clearest recoverable full-body joint structure among the candidates while preserving the pose source's coarse left/right limb arrangement.

### Candidate C

- Correct: Keeps the Y-bot identity and gives the most generous full-body framing. Both legs, feet, arms, and the raised-hand gesture are visible, with no major role swap.
- Problems: The pose is less faithful than A or B: the torso is too upright, the crouch and weight shift are softened, and the lower body reads more like a generic bent-leg stance than the pose source. The raised hands are visible but clustered, and the foot/ankle shapes are less clean for joint recovery.
- Failure tags: `pose_mismatch`, `view_mismatch`, `body_deformation`, `accessory_deformed`.
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 3.5/5 / 3.5/5 / 4.5/5 / 4/5 / 3.5/5
- Acceptable: Borderline.
- Reason: The full-body visibility is useful, but the recovered pose is too generic and loses important lower-body structure from the pose source.

## Best Candidate

- Best candidate: Candidate B.
- Reason: Candidate B is the best choice for downstream 3D pose recovery because it preserves the full body, keeps the coarse left/right limb layout, and provides the clearest readable shoulders, elbows, hips, knees, ankles, and feet. Its hand region is still messy, but the main body structure is more usable than A's more occluded upper body and C's weaker pose match.
- Overall observation: All candidates preserve the Y-bot identity, but all remain more front-facing and less weight-shifted than the pose source. The main failure mode is not aesthetics; it is incomplete transfer of the crouched, raised-hands pose and deformation/occlusion around the hands and wrists.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
