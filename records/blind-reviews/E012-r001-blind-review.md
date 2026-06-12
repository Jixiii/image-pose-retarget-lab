# Blind Review: E012/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E012-r001-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
Images 1-3 = CHARACTER SOURCES. Images 4-6 = POSE SOURCES. Do not swap these roles.

Use Images 1-3 as references for the same character. Image 1 is the primary character source; the other character images provide additional appearance details and views.

Use Images 4-6 as references for the same pose. Image 4 is the primary pose source and controls the final camera viewpoint, body facing direction, and framing.

Generate one centered, uncropped, full-body image of the exact character from the character sources performing the pose from the pose sources.

Preserve the character sources' identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use the pose sources' character identity, face, outfit, colors, materials, or style.

Use the pose sources only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match image 4's viewing angle and body facing direction.

Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from the pose sources: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in the pose sources.

The character sources always control appearance. The pose sources only control pose and viewpoint. Do not create a hybrid.
```

### Input Role Assumption

- Input 1 is treated as the character source unless the visible record clearly says otherwise.
- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.

## Inputs

### Input 1: Character Source 1

![Input 1: Character Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png`

### Input 2: Character Source 2

![Input 2: Character Source 2](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-X).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-X).png`

### Input 3: Character Source 3

![Input 3: Character Source 3](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-Y.png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-Y.png`

### Input 4: Pose Source 1

![Input 4: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-X.png)

`datasets/assets/native_1/renders/native1-frame11-X.png`

### Input 5: Pose Source 2

![Input 5: Pose Source 2](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11--Y.png)

`datasets/assets/native_1/renders/native1-frame11--Y.png`

### Input 6: Pose Source 3

![Input 6: Pose Source 3](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-Y.png)

`datasets/assets/native_1/renders/native1-frame11-Y.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E012/runs/r001/outputs/ai_generate_8443_1.png)

`experiments/E012/runs/r001/outputs/ai_generate_8443_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E012/runs/r001/outputs/ai_generate_8443_2.png)

`experiments/E012/runs/r001/outputs/ai_generate_8443_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E012/runs/r001/outputs/ai_generate_8443_3.png)

`experiments/E012/runs/r001/outputs/ai_generate_8443_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E012/runs/r001/outputs/ai_generate_8443_4.png)

`experiments/E012/runs/r001/outputs/ai_generate_8443_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character identity, clothing colors, sweatshirt graphic, shorts, bare legs, and yellow shoes well. Full body is visible and centered. The weapon is in the viewer-left/character-right side, broadly consistent with the primary pose source, and the free arm hangs down.
- Problems: The walking pose is weak and close to a neutral front-facing stance. The legs are too vertical and not clearly separated into the source's forward/back gait, reducing downstream joint recoverability. The sword is too horizontal and does not match the stronger diagonal/downward weapon angle. The sword hand/wrist area is partly ambiguous.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5/5 / 4/5 / 3.5/5 / 4.5/5 / 4/5 / 4/5
- Acceptable: Partly, but not ideal for pose recovery.
- Reason: Clean full-body visibility and identity preservation are useful, but the lower-body pose is under-retargeted and lacks the clear gait structure needed for reliable 3D pose recovery.

### Candidate B

- Correct: Strongly captures a walking stride with separated legs, visible feet, a hanging free arm, and a weapon held low. Identity and outfit are mostly preserved, including the tan sweatshirt, white chest graphic, denim shorts, bare legs, and yellow shoes. Limb structure is readable and deformation is low.
- Problems: The camera/body orientation shifts to a side/three-quarter view instead of the primary pose source's more frontal view. The sword points to viewer-right rather than viewer-left as in the primary pose source, so the output appears to follow one of the side references more than Image 4 and may introduce a left/right/view correspondence error. The crossed legs are clear visually, but the exact source leg order is not fully reliable.
- Failure tags: `view_mismatch`, `left_right_flip`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4/5 / 2/5 / 2.5/5 / 4/5 / 4/5 / 4/5
- Acceptable: Partly.
- Reason: This is one of the clearest walking poses for downstream joint extraction, but the wrong viewpoint and likely side/correspondence mismatch make it less faithful to the requested primary pose.

### Candidate C

- Correct: Best preserves the primary frontal camera/viewpoint while keeping the character full body visible and centered. Identity, outfit, colors, sweatshirt graphic, shorts, legs, and shoes are well preserved. The sword is on the viewer-left/character-right side and points diagonally down-left, closer to the primary pose source than Candidate A. The free arm hangs naturally, and the body has low deformation with readable major joints.
- Problems: The gait is still softened compared with the pose source: the legs are not as dynamically offset, and the forward/back relationship is only mildly expressed. The sword arm is simplified and the hand grip is not very explicit. The lower-body pose is usable but not a precise retarget of the source stride.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 4/5 / 4/5 / 4.5/5 / 4/5 / 4/5
- Acceptable: Yes, as the best compromise.
- Reason: It has the cleanest combination of full-body visibility, primary-view alignment, apparent left/right consistency, low deformation, and recoverable joint structure, even though the walking pose is somewhat damped.

### Candidate D

- Correct: Captures a clearer walking stride than A/C, preserves the character identity and outfit well, and keeps the body mostly intact. The sword is present and held low, and the limb arrangement has some usable gait information.
- Problems: The camera is high-angle three-quarter, far from the primary pose source's frontal full-body framing. The top-down view and diagonal composition reduce the usefulness of the image for clean 3D pose recovery, especially around hip/knee/ankle relationships. The sword overlaps the lower body and can confuse limb parsing. The side/view correspondence appears closer to the auxiliary pose views than to Image 4.
- Failure tags: `view_mismatch`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 1.5/5 / 3/5 / 4/5 / 4/5 / 3.5/5
- Acceptable: No, unless the high-angle view is allowed.
- Reason: The pose energy is useful, but the camera angle and occlusion make it weaker than B for gait clarity and weaker than C for primary-view, recoverable full-body structure.

## Best Candidate

- Best candidate: Candidate C
- Reason: Candidate C is the best downstream 3D pose-recovery compromise because it keeps the full body visible, preserves the primary frontal viewpoint, keeps the sword on the expected viewer-left/character-right side, avoids major deformation, and leaves the main joints readable. Candidate B has the clearest walking stride, but its side/three-quarter viewpoint and sword direction make it less faithful to the primary pose source and risk left/right/view mismatch.
- Overall observation: All candidates preserve the character identity better than they preserve the exact pose. The main failure mode is pose damping or viewpoint drift: A/C become too frontal and subdued in the legs, while B/D recover more gait motion but follow side/high-angle views instead of the primary pose source. For 3D pose recovery, C is only relatively best, not a fully accurate retarget.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
