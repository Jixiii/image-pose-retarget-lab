# Blind Review: E011/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E011-r001-blind-review.md` and the images linked inside it.
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

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E011/runs/r001/outputs/ai_generate_8384_1.png)

`experiments/E011/runs/r001/outputs/ai_generate_8384_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E011/runs/r001/outputs/ai_generate_8384_2.png)

`experiments/E011/runs/r001/outputs/ai_generate_8384_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E011/runs/r001/outputs/ai_generate_8384_3.png)

`experiments/E011/runs/r001/outputs/ai_generate_8384_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E011/runs/r001/outputs/ai_generate_8384_4.png)

`experiments/E011/runs/r001/outputs/ai_generate_8384_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character source identity, clothing colors, hairstyle, shorts, and shoes. Full body is visible, and the side-view walking structure gives a recoverable pelvis-to-leg chain with one planted leg and one trailing/lifted leg.
- Problems: The pose is only approximate: the arm/sword arrangement is borrowed from the pose source even though the character source has no sword, and the rear/free arm is mostly hidden. The side orientation appears to choose one side reference rather than the primary front/three-quarter pose source, so left/right correspondence is not fully reliable. The sword and hand area add occlusion/noise around the wrist and hip.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`, `style_drift`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 6 / 5 / 5 / 9 / 6 / 7
- Acceptable: Borderline.
- Reason: It is usable for rough 3D pose recovery because the full body and leg structure are clear, but the added sword, hidden arm, and uncertain side choice make the skeleton less trustworthy.

### Candidate B

- Correct: Strongly preserves the side walking pose, with clean full-body visibility, clear leg separation, and a readable sword-hand relationship. The joint structure is the easiest to parse geometrically.
- Problems: This is essentially the pose-source character, not the character source. The face, hair, body proportions, outfit, colors, materials, boots, and sword all come from the pose source, so role separation fails. It is also a side view rather than the primary front/three-quarter input view.
- Failure tags: `role_swap`, `identity_drift`, `style_drift`, `view_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 8 / 5 / 8 / 1 / 0 / 8
- Acceptable: No.
- Reason: Although it is the cleanest pose image, it is not a retargeted output of the character source and should not be selected except as a pose-only control.

### Candidate C

- Correct: Preserves the character source identity and outfit well, keeps the body uncropped, and has low visual deformation. Both arms and legs are visible, which is helpful for 3D recovery.
- Problems: The pose drifts into a generic front/three-quarter walking pose. It loses the low carried-arm/sword-side structure from the pose references, the leg crossing does not clearly match the reference limb order, and the body orientation is not as side-readable as the side pose references. Feet are also somewhat ambiguous because one foot floats/lands at an odd angle.
- Failure tags: `pose_mismatch`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 5 / 6 / 4 / 9 / 9 / 8
- Acceptable: Borderline.
- Reason: It is clean and easy to segment, but the actual target pose is too weakened for reliable downstream pose evaluation.

### Candidate D

- Correct: Preserves the character source identity, clothing, hair, and full-body framing while producing a clear side-view walking pose. The head, torso, pelvis, legs, knees, ankles, and feet are readable, with less body deformation than Candidate A.
- Problems: It still imports the sword from the pose source, which is an identity/style leak and partially occludes the hand/hip area. The non-sword arm is mostly hidden behind the torso, and the lifted/trailing leg is flatter and more grounded than in the pose references. Viewpoint is side-oriented rather than the primary front/three-quarter source.
- Failure tags: `pose_mismatch`, `view_mismatch`, `style_drift`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 7 / 5 / 6 / 8 / 6 / 8
- Acceptable: Yes, with caveats.
- Reason: Among the character-preserving outputs, it gives the clearest usable full-body joint structure with comparatively low deformation.

## Best Candidate

- Best candidate: Candidate D.
- Reason: Candidate D is the best tradeoff for downstream 3D pose recovery: it keeps the character source while providing the clearest full-body side-pose skeleton, readable leg separation, stable feet, and low deformation. Candidate B has a cleaner pose but is a role swap, so it is not a valid retargeted result. Candidate A is close but has more uncertain laterality and more hand/sword occlusion; Candidate C is clean but too generic and pose-mismatched.
- Overall observation: The run can produce a recoverable walking skeleton, but the best candidates still leak the pose-source sword and do not cleanly satisfy the primary-view/left-right constraints. For 3D pose recovery, Candidate D is relatively best, not fully correct.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
