# Blind Review: E007/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E007-r001-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
Image 1 = CHARACTER SOURCE. Image 2 = POSE SOURCE. Do not swap these roles.

Generate one centered, uncropped, full-body image of the exact character from image 1 performing the pose from image 2.

Preserve image 1's identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use image 2's character identity, face, outfit, colors, materials, or style.

Use image 2 only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match image 2's viewing angle and body facing direction.

Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from image 2: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in image 2.

Image 1 always controls appearance. Image 2 only controls pose and viewpoint. Do not create a hybrid.
```

### Input Role Assumption

- Input 1 is treated as the character source unless the visible record clearly says otherwise.
- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.

## Inputs

### Input 1: Character Source

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-noSkeleton-rest-pose1-X.png)

`datasets/assets/native_1/renders/native1-noSkeleton-rest-pose1-X.png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E007/runs/r001/outputs/ai_generate_8132_1.png)

`experiments/E007/runs/r001/outputs/ai_generate_8132_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E007/runs/r001/outputs/ai_generate_8132_2.png)

`experiments/E007/runs/r001/outputs/ai_generate_8132_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E007/runs/r001/outputs/ai_generate_8132_3.png)

`experiments/E007/runs/r001/outputs/ai_generate_8132_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E007/runs/r001/outputs/ai_generate_8132_4.png)

`experiments/E007/runs/r001/outputs/ai_generate_8132_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the low-poly character identity, outfit colors, hair, boots, and sword accessory. Full body is visible and the general crouched, arms-forward pose is recognizable.
- Problems: The body is too upright compared with the pose source's forward lean. The legs only roughly match the bent stance; foot contact and lower-leg geometry are awkward, with the boots deformed into blocky shapes that would make ankle/foot recovery unreliable. The sword-hand side is visible, but the weapon and hands partially obscure the arm/wrist structure.
- Failure tags: `pose_mismatch`, `body_deformation`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 3/5 / 3/5 / 4/5 / 4/5 / 3/5
- Acceptable: Marginal.
- Reason: It is usable as a rough full-body pose, but the lower-body deformation and unclear foot placement are risky for downstream 3D pose recovery.

### Candidate B

- Correct: Preserves the character's identity, clothing palette, boots, and sword. The arms are bent forward and the legs attempt the same uneven crouched stance as the pose source.
- Problems: The lower body reads as floating or poorly grounded, with unclear foot contact and a weak weight-bearing structure. The torso is more upright than the reference. The candidate keeps the sword, but it changes the hand silhouette and makes wrist positions harder to read.
- Failure tags: `pose_mismatch`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 3/5 / 3/5 / 4/5 / 4/5 / 2/5
- Acceptable: No.
- Reason: Full-body visibility is present, but the floating/ungrounded lower body makes the pose skeleton less reliable than the other candidates.

### Candidate C

- Correct: Maintains the character identity and most outfit features. The legs have a clearer bent stance than Candidate B, and the full body remains visible.
- Problems: The sword has been rotated into a horizontal bar across the torso and both hands appear organized around it, which deviates from the pose source's open hands and obscures elbow/wrist interpretation. The torso is still too upright, and the body orientation is more front-facing than the reference. Lower-body pose is only approximate.
- Failure tags: `pose_mismatch`, `view_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 3/5 / 3/5 / 4/5 / 3/5 / 3/5
- Acceptable: Marginal.
- Reason: It has readable full-body structure, but the horizontal sword and hand arrangement are a major issue for arm-pose recovery.

### Candidate D

- Correct: Best preserves a clear, unobstructed full-body joint structure: both arms and hands are visible, both legs are readable, and the feet have clearer ground contact than the other candidates. The character identity, hair, face style, vest, blue sleeves, pants, and boots are mostly preserved.
- Problems: The sword accessory is missing. The pose is still not exact: the torso is too upright, the crouch is shallower than the pose source, and the leg spread/weight shift only approximates the reference. The pose source's hand shape and forward reach are simplified.
- Failure tags: `pose_mismatch`, `accessory_lost`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 4/5 / 4/5 / 4/5 / 1/5 / 4/5
- Acceptable: Yes, for pose-recovery priority.
- Reason: Despite losing the sword, it provides the cleanest and least obstructed body layout for estimating a usable 3D skeleton.

## Best Candidate

- Best candidate: Candidate D
- Reason: Candidate D is the least flawed for downstream 3D pose recovery because it has the clearest full-body visibility, least obstructed hands/arms, better foot grounding, and lower deformation. The missing sword is a serious identity/accessory error, but it improves pose readability compared with candidates where the sword obscures or distorts the hand and wrist structure.
- Overall observation: All candidates preserve the character role rather than swapping to the pose-source human, but none matches the pose source precisely. The main shared failures are insufficient forward torso lean, only approximate crouched leg placement, and simplified arm/hand structure. Candidate D is relatively best because its skeleton is most recoverable, not because it is the most faithful to every character detail.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
