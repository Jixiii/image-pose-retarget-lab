# Blind Review: E005/r004

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E005-r004-blind-review.md` and the images linked inside it.
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

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-noSkeleton-pose1.png)

`datasets/assets/native_1/renders/native1-noSkeleton-pose1.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r004/outputs/ai_generate_8006_1.png)

`experiments/E005/runs/r004/outputs/ai_generate_8006_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r004/outputs/ai_generate_8006_2.png)

`experiments/E005/runs/r004/outputs/ai_generate_8006_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r004/outputs/ai_generate_8006_3.png)

`experiments/E005/runs/r004/outputs/ai_generate_8006_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r004/outputs/ai_generate_8006_4.png)

`experiments/E005/runs/r004/outputs/ai_generate_8006_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Full body is visible, front-facing view is close to the pose source, arms are lowered with a similar asymmetry, and the legs form a readable stepping/crossing structure. Character identity, sweatshirt, shorts, hair bun, and shoes are mostly preserved.
- Problems: Lower-body pose is only approximate: the supporting/crossed-leg relationship is softened and reads more like a normal walk than the compact pose source stance. A gray object from the pose source appears in the hand, which violates role separation and can add a small occlusion. Hands are simplified, but the main limb joints remain recoverable.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 4.5/5 / 4/5 / 4.5/5 / 3/5 / 4/5
- Acceptable: Yes, relatively.
- Reason: It is not the closest pose match, but it gives the clearest full-body, front-facing, low-deformation structure for downstream 3D pose recovery.

### Candidate B

- Correct: Full body is visible, identity and clothing are mostly preserved, and both legs and arms remain anatomically readable.
- Problems: Viewpoint shifts to a left-facing three-quarter/profile walk instead of the pose source's mostly frontal view. The leg crossing is exaggerated and the body direction/head direction do not match the reference. Arm placement is also different, with one arm drifting outward. Left/right correspondence is uncertain because the turn changes which limb is visually forward.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5/5 / 2.5/5 / 2.5/5 / 4.5/5 / 4/5 / 4/5
- Acceptable: No.
- Reason: The body is clean, but the viewpoint and walking direction are too different for reliable pose-retarget evaluation.

### Candidate C

- Correct: Full body is visible, the character identity and outfit are well preserved, and the anatomy is mostly stable.
- Problems: The output becomes a side-view walking stride rather than the source's frontal, compact stance. The head, torso, pelvis, and feet all rotate away from the requested viewpoint. Limb placement is therefore not a faithful left/right transfer even though the body itself is coherent.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2/5 / 1.5/5 / 2/5 / 4.5/5 / 4/5 / 4/5
- Acceptable: No.
- Reason: It is visually coherent but unsuitable for this task because the pose and camera direction are substantially wrong.

### Candidate D

- Correct: Mostly frontal full-body view, arms hang in the same broad pattern as the pose source, and the forward/near-center foot relationship is closer to the reference than B or C. Identity, clothing, hair, and shoes are mostly preserved.
- Problems: The framing is tighter and the lower foot is partly contaminated by the pose-source ground/cursor marker, which can interfere with foot localization. A gray object from the pose source is copied into the hand. The leg relationship is readable but still not exact, and the bottom-foot artifact reduces usefulness for pose recovery.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `style_drift`, `framing_error`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4/5 / 4.5/5 / 4/5 / 4.5/5 / 3/5 / 3.5/5
- Acceptable: Yes, relatively.
- Reason: It matches the frontal pose structure well, but the cursor/ground artifact near the foot makes it less clean than Candidate A for downstream joint extraction.

## Best Candidate

- Best candidate: Candidate A
- Reason: Candidate A is the best choice for downstream 3D pose recovery because it keeps the whole body visible, stays front-facing, has low deformation, and leaves the main joints and feet more clearly recoverable than Candidate D. Candidate D has a slightly closer leg/stance match, but the cursor/ground artifact over the lower foot is a practical problem for foot and ankle localization.
- Overall observation: All candidates preserve the character source reasonably well, but none perfectly transfers the pose source. A and D are the only usable candidates for pose recovery; B and C drift into a different camera direction and walking pose. The main recurring failure is copying pose-source artifacts/accessories while only approximately matching the lower-body left/right structure.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
