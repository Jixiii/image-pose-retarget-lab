# Blind Review: E002/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E002-r002-blind-review.md` and the images linked inside it.
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

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r002/outputs/ai_generate_7926_1.png)

`experiments/E002/runs/r002/outputs/ai_generate_7926_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r002/outputs/ai_generate_7926_2.png)

`experiments/E002/runs/r002/outputs/ai_generate_7926_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r002/outputs/ai_generate_7926_3.png)

`experiments/E002/runs/r002/outputs/ai_generate_7926_3.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the intended low-poly native character identity, outfit colors, boots, belt pouch, and sword. Full body is visible and roughly centered. Both arms are raised forward and the legs are at least partially bent, so the output starts to follow the pose source.
- Problems: The pose is too upright and front-facing compared with the pose source's deeper crouch and forward lean. Lower-body structure is weak: one leg remains close to a standing pose and the feet do not clearly reproduce the wide, bent support pattern. The copied joint/marker overlays and large pelvis/foot markers obscure important joints, which hurts downstream 3D pose recovery. Hands are readable but simplified and not as clearly arranged as the pose source.
- Failure tags: `pose_mismatch`, `body_deformation`, `view_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 5 / 6 / 7 / 9 / 8 / 5
- Acceptable: Marginal.
- Reason: The character is preserved, but the crouch and joint readability are compromised by an incomplete lower-body transfer and heavy marker occlusion.

### Candidate B

- Correct: Best full-body pose structure for recovery. The torso leans forward, both arms reach forward with clear elbows/wrists/hands, both knees are bent, and both feet remain visible. The intended low-poly character, hair, vest, blue clothing, boots, and sword are preserved without copying the pose-source identity. The image has low deformation and clean, unobscured limb boundaries.
- Problems: The camera/viewpoint shifts to a stronger three-quarter side view than the pose source, so the front-facing relationship and left/right leg spacing are not perfectly preserved. The legs are readable but less wide than the pose reference, and the sword/accessory placement changes with the body turn.
- Failure tags: `view_mismatch`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 8 / 6 / 8 / 9 / 8 / 9
- Acceptable: Yes.
- Reason: Despite the viewpoint mismatch, it gives the clearest usable full-body skeleton and the least obstructed joint structure.

### Candidate C

- Correct: Preserves the intended character identity, outfit, sword, belt pouch, and full-body framing. The raised arm hints at the pose-source upper-body action.
- Problems: Pose transfer is poor: the figure remains mostly upright, the torso does not lean forward enough, one arm drops toward the original character pose, and the legs do not form the pose source's crouched support. Marker overlays obscure the torso, pelvis, knees, ankles, and foot area, making joint recovery noisy. Lower limbs are less clearly aligned than Candidate B and the stance reads closer to the source character's original standing pose than the pose reference.
- Failure tags: `pose_mismatch`, `body_deformation`, `view_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 6 / 6 / 9 / 8 / 5
- Acceptable: No.
- Reason: It keeps identity but does not provide a sufficiently clear or faithful crouched pose for 3D recovery.

## Best Candidate

- Best candidate: Candidate B.
- Reason: Candidate B is the best choice for downstream 3D pose recovery because it has the clearest full-body crouched structure, visible hands and feet, unobscured limb boundaries, and low deformation. Its main weakness is the shifted three-quarter viewpoint, but the skeleton is more recoverable than A or C.
- Overall observation: All candidates preserve the character identity reasonably well. A and C are hurt by copied marker overlays and incomplete crouch transfer; B sacrifices some viewpoint correctness but is the only candidate with a clean, readable, full-body joint layout.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
