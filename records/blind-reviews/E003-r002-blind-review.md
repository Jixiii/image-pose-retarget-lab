# Blind Review: E003/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E003-r002-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
Keep the exact character from image 1. Use image 2 only as a pose reference. Transfer the full-body pose from image 2 onto the image 1 character while preserving image 1's identity, design, proportions, colors, and materials. Output one centered, uncropped, full-body image. Do not copy the image 2 character or create a hybrid.
```

### Input Role Assumption

- Input 1 is treated as the character source unless the visible record clearly says otherwise.
- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.

## Inputs

### Input 1: Character Source

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose1.png)

`datasets/assets/native_1/renders/native1-pose1.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E003/runs/r002/outputs/ai_generate_7948_1.png)

`experiments/E003/runs/r002/outputs/ai_generate_7948_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E003/runs/r002/outputs/ai_generate_7948_2.png)

`experiments/E003/runs/r002/outputs/ai_generate_7948_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E003/runs/r002/outputs/ai_generate_7948_3.png)

`experiments/E003/runs/r002/outputs/ai_generate_7948_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E003/runs/r002/outputs/ai_generate_7948_4.png)

`experiments/E003/runs/r002/outputs/ai_generate_7948_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Full body is visible, roughly centered, and the output keeps a front-facing readable humanoid structure with both arms and legs identifiable.
- Problems: It copies the low-poly pose-reference character instead of the character source. The woman's hair, face, orange sweatshirt, denim shorts, yellow shoes, and body proportions are all lost. The sword/accessory is copied from the pose source, and the arm/leg pose is only a loose match rather than a clean transfer.
- Failure tags: `role_swap`, `identity_drift`, `style_drift`, `pose_mismatch`, `accessory_lost`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 4 / 3 / 0 / 0 / 3
- Acceptable: No.
- Reason: The body is usable as a generic low-poly pose image, but it fails the retargeting task because the target character identity is replaced by the pose-source identity.

### Candidate B

- Correct: Full body is mostly visible, and the limbs are separable enough to infer a walking-like skeleton.
- Problems: It is a role swap to the low-poly pose-reference character. The view changes to a side/profile walking pose, which does not match the frontal pose source. The sword is still copied from the reference, the torso is rotated away, and the left/right limb correspondence is hard to trust from the side view.
- Failure tags: `role_swap`, `identity_drift`, `style_drift`, `pose_mismatch`, `view_mismatch`, `left_right_flip`, `accessory_lost`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 1 / 1 / 1 / 0 / 0 / 3
- Acceptable: No.
- Reason: It has readable limbs, but both the character identity and the requested camera/body orientation are wrong.

### Candidate C

- Correct: Preserves the intended woman character, clothing colors, cat sweatshirt mark, denim shorts, yellow shoes, and full-body framing. The front-facing view makes left/right and joint locations comparatively clear for downstream 3D pose recovery. Limbs are visible with low deformation.
- Problems: The pose is only partially transferred: the arms are too relaxed and symmetric, the torso is upright rather than matching the reference stance, and the legs read more like a neutral step than the pose source's offset stance. It incorrectly copies the pose-source sword into the character's hand.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 4 / 4 / 5 / 3 / 4
- Acceptable: Yes, but only as the least bad option for pose recovery.
- Reason: It keeps the correct character and provides the clearest frontal full-body structure, even though the pose transfer is incomplete and the extra sword is wrong.

### Candidate D

- Correct: Preserves the intended woman character, outfit, hair, and full-body visibility. The body is cleanly rendered with low deformation, and most major joints are visible.
- Problems: The pose becomes a side-view walking stride instead of the frontal pose source. The torso, head, arms, and legs are all rotated away from the reference orientation, making left/right correspondence less reliable. It does not reproduce the pose-source arm arrangement or stance.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 1 / 2 / 5 / 5 / 4
- Acceptable: No.
- Reason: It is visually clean and keeps identity, but the side-view walking pose is too far from the pose reference for this run's pose-recovery priority.

## Best Candidate

- Best candidate: Candidate C.
- Reason: Candidate C is the best relative choice for downstream 3D pose recovery because it preserves the correct character, keeps the full body visible, stays near the frontal viewpoint, and has the clearest left/right-readable joint structure. Its main weaknesses are incomplete pose transfer and the erroneous copied sword, but those are less damaging here than the role swaps in A/B or the side-view pose mismatch in D.
- Overall observation: None of the candidates cleanly solves the task. A and B copy the pose-source character, D preserves identity but changes to an unrelated side-walking pose, and C is only a partial retarget. For pose recovery, C is the most usable because its full-body skeleton is clear and front-facing.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
