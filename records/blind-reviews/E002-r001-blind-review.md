# Blind Review: E002/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E002-r001-blind-review.md` and the images linked inside it.
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

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose1.png)

`datasets/assets/native_1/renders/native1-pose1.png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-pose2.png)

`datasets/assets/Body-Block/renders/body-block-pose2.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r001/outputs/ai_generate_7889_1.png)

`experiments/E002/runs/r001/outputs/ai_generate_7889_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r001/outputs/ai_generate_7889_2.png)

`experiments/E002/runs/r001/outputs/ai_generate_7889_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r001/outputs/ai_generate_7889_3.png)

`experiments/E002/runs/r001/outputs/ai_generate_7889_3.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Uses the character-source identity, outfit colors, low-poly style, and sword-like accessory. Full body is visible. The arms are raised near the head and the legs are bent into a staggered stance, so it captures the broad pose-source intent.
- Problems: Upper-body pose is cluttered by the sword and visible rig overlay; hands, forearms, and accessory overlap the face, making arm joints hard to recover. The pose is not a clean match: the elbows and hands are too compressed around the head, torso lean differs, and the feet/ankles are partly ambiguous. Lower limbs are usable but simplified, with weak foot contact and some deformation around the knees/boots. Left/right assignment is difficult to verify because the crossed arms and sword obscure the front-facing skeleton.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 6 / 8 / 5 / 8 / 6 / 5
- Acceptable: Marginal.
- Reason: It is one of the two candidates that actually attempts the target raised-arm pose, but the occluded arms and crowded joint structure make it risky for downstream 3D pose recovery.

### Candidate B

- Correct: Best preserves the pose-source structure among the candidates: both arms are raised toward the head, knees are bent, the stance is asymmetrical, and the full body remains visible. Character identity, colors, and low-poly proportions are mostly retained, and the sword/accessory is still present.
- Problems: The sword is enlarged and intrudes through the upper-body pose, causing occlusion around the head and arms. Hands and wrists are still noisy, and the arm overlay makes exact left/right reading only moderately reliable. The torso is more front-facing and compact than the pose source, and the legs are chunkier than the reference, but the knee/ankle structure remains more readable than Candidate A. Some visible rig markers/overlays reduce artifact quality.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 7 / 8 / 6 / 8 / 6 / 6
- Acceptable: Yes, relatively.
- Reason: Despite visual clutter, it gives the clearest recoverable full-body pose: arms are raised, leg asymmetry is visible, body is uncropped, and the skeleton-like structure is more usable than in the other outputs.

### Candidate C

- Correct: Preserves the character-source identity, low-poly style, outfit, and accessory cleanly. The image is full-body, centered, and has fewer visible rendering artifacts than A or B.
- Problems: Fails the retargeting task for 3D recovery: the arms stay near the original character pose instead of raising toward the head, the torso remains upright, and the leg pose is only a mild walking/standing variant rather than the bent, staggered pose source. The figure lacks visible pose-reference joint structure, and the feet are floating/unclear. Because the requested target pose is mostly absent, left/right correctness is not meaningfully demonstrated.
- Failure tags: `pose_mismatch`, `view_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 7 / 4 / 9 / 8 / 8
- Acceptable: No.
- Reason: It is visually clean, but it mostly preserves the input character pose instead of transferring the pose source, so it is not useful for downstream 3D pose recovery.

## Best Candidate

- Best candidate: Candidate B.
- Reason: Candidate B is only relatively best, but it provides the strongest usable pose signal: raised arms, bent/asymmetric legs, full-body visibility, and a readable enough joint layout. Candidate A is close but has heavier upper-body occlusion and less clear limb separation. Candidate C is cleanest visually but does not perform the pose transfer.
- Overall observation: For downstream 3D pose recovery, the successful candidates are limited by arm/hand occlusion and accessory interference. The model can approximate the target stance when it tries to follow the pose source, but the sword and overlapping upper limbs make left/right and hand-joint recovery unreliable.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
