# Blind Review: E011/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E011-r002-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
Image 1 = CHARACTER SOURCE. Images 2-4 = POSE SOURCES. Do not swap these roles.

Use Images 2-4 as references for the same pose. Image 2 is the primary pose source and controls the final camera viewpoint, body facing direction, and framing.

Generate one centered, uncropped, full-body image of the exact character from image 1 performing the pose from the pose sources.

Preserve image 1's identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use the pose sources' character identity, face, outfit, colors, materials, or style.

Use the pose sources only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match image 2's viewing angle and body facing direction.

Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from the pose sources: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in the pose sources.

Image 1 always controls appearance. The pose sources only control pose and viewpoint. Do not create a hybrid.
```

### Input Role Assumption

- Input 1 is treated as the character source unless the visible record clearly says otherwise.
- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.

## Inputs

### Input 1: Character Source

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-X.png)

`datasets/assets/native_1/renders/native1-frame11-X.png`

### Input 3: Pose Source 2

![Input 3: Pose Source 2](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11--Y.png)

`datasets/assets/native_1/renders/native1-frame11--Y.png`

### Input 4: Pose Source 3

![Input 4: Pose Source 3](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-Y.png)

`datasets/assets/native_1/renders/native1-frame11-Y.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E011/runs/r002/outputs/ai_generate_8385_1.png)

`experiments/E011/runs/r002/outputs/ai_generate_8385_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E011/runs/r002/outputs/ai_generate_8385_2.png)

`experiments/E011/runs/r002/outputs/ai_generate_8385_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E011/runs/r002/outputs/ai_generate_8385_3.png)

`experiments/E011/runs/r002/outputs/ai_generate_8385_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E011/runs/r002/outputs/ai_generate_8385_4.png)

`experiments/E011/runs/r002/outputs/ai_generate_8385_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character source identity, orange sweatshirt, white chest graphic, denim shorts, yellow shoes, and front camera framing. Full body is visible, and both arms and legs remain mostly readable.
- Problems: The pose is simplified into a normal front walk rather than the source pose. The weapon arm hangs down instead of bending across the lower torso, and the sword is invented as a long diagonal blade rather than preserving only pose structure. The lower-body correspondence is weak: the lifted/crossing leg appears on the wrong side relative to the primary front pose, and the knee/foot structure is less explicit than the pose source. Feet are close together, making the support leg vs lifted leg somewhat ambiguous for 3D recovery.
- Failure tags: `pose_mismatch`, `left_right_flip`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 5 / 8 / 4 / 9 / 6 / 8
- Acceptable: No
- Reason: Visually clean and full-body, but the arm pose and leg correspondence are not reliable enough for downstream 3D pose recovery.

### Candidate B

- Correct: Keeps the source character identity and outfit well. The body is centered, uncropped, front-facing, and the walking structure has a clear support leg, lifted leg, visible knees, visible ankles, and separated feet.
- Problems: The sword/hand arm is lowered instead of bent across the lower torso. The lifted leg appears on the opposite side from the primary pose source, so left/right leg correspondence is likely flipped. The torso is more upright and relaxed than the pose source, and the sword is an appearance transfer from the pose source rather than part of the original character identity.
- Failure tags: `pose_mismatch`, `left_right_flip`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 6 / 8 / 4 / 9 / 6 / 8
- Acceptable: Borderline
- Reason: The skeleton is clean and usable, but the left/right leg mismatch and incorrect weapon-arm pose reduce pose fidelity.

### Candidate C

- Correct: Preserves the source character and outfit, remains full-body, and gives readable limb separation. The body has a slight walking stance with visible feet and no severe anatomical breakage.
- Problems: Viewpoint drifts away from the primary front pose into a mild three-quarter view. The legs form a side-step/crossed stance rather than the clear forward walking pose in the source, and the lifted/support leg relationship does not match the primary reference. The sword arm hangs at the side, missing the bent-across-torso arm. The blade is transferred as an added prop and is too visually dominant for the original character.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 6 / 4 / 9 / 6 / 8
- Acceptable: No
- Reason: It is clean as an image, but the viewpoint and lower-body structure are farther from the pose source than the better candidates.

### Candidate D

- Correct: Strongly preserves the source character identity, outfit, colors, and full-body front framing. The pose has the clearest whole-body walking structure among the candidates: readable shoulders, arms, hips, knees, ankles, and both feet, with low deformation and good joint separability.
- Problems: The sword arm is still lowered instead of bent across the lower torso. The lifted/support leg relationship appears flipped relative to the primary front pose, and the stride is softened into a casual walk rather than the compact pose-reference step. The sword is shortened and partially occluded, though this is less harmful for body-pose recovery than limb deformation would be.
- Failure tags: `pose_mismatch`, `left_right_flip`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 6 / 8 / 4 / 9 / 6 / 9
- Acceptable: Borderline
- Reason: Not pose-accurate enough to call fully successful, but it gives the most stable, full-body, low-deformation joint layout for downstream recovery.

## Best Candidate

- Best candidate: Candidate D
- Reason: Candidate D is only relatively best. It does not correctly preserve the pose source's bent weapon arm or left/right leg correspondence, but it has the cleanest full-body skeleton, lowest deformation, visible feet, readable knees/ankles, and stable front-facing viewpoint. For downstream 3D pose recovery, that makes it more usable than A and C, and slightly preferable to B despite similar pose errors.
- Overall observation: All candidates preserve the character source much better than they preserve the exact pose. The main shared failure is pose simplification: the bent weapon arm becomes a lowered side arm, and the leg correspondence appears flipped or softened into a generic walk. None is a fully acceptable pose-retarget result if left/right correctness is strict; D is the least bad candidate for pose recovery.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
