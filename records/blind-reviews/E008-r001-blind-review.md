# Blind Review: E008/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E008-r001-blind-review.md` and the images linked inside it.
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

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose6.png)

`datasets/assets/native_1/renders/native1-pose6.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E008/runs/r001/outputs/ai_generate_8213_1.png)

`experiments/E008/runs/r001/outputs/ai_generate_8213_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E008/runs/r001/outputs/ai_generate_8213_2.png)

`experiments/E008/runs/r001/outputs/ai_generate_8213_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E008/runs/r001/outputs/ai_generate_8213_3.png)

`experiments/E008/runs/r001/outputs/ai_generate_8213_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E008/runs/r001/outputs/ai_generate_8213_4.png)

`experiments/E008/runs/r001/outputs/ai_generate_8213_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character-source identity, orange sweatshirt, shorts, yellow shoes, and side-facing walking view. Full body is visible and the main leg stride is readable.
- Problems: Arm pose is simplified relative to the pose source; the rear arm hangs down instead of clearly matching the weapon-arm/back-arm structure. Hands are weakly formed, and the torso/hip transition is soft, which reduces joint confidence for 3D recovery.
- Failure tags: `pose_mismatch`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 4.5/5 / 4/5 / 4.5/5 / 5/5 / 3.5/5
- Acceptable: Marginal.
- Reason: Good full-body side-walk candidate without role contamination, but arm and hip landmarks are not as explicit as needed for robust downstream pose recovery.

### Candidate B

- Correct: Strong side-view framing, full body visibility, and a clear walking stride. The body faces the same general direction as the pose source and the leg placement is easy to parse.
- Problems: Imports the sword from the pose source even though the character source has no sword. The sword occludes the hand, hip, and upper-leg region, making skeletal recovery less clean. The rear arm is mostly defined through the prop instead of a clearly visible limb.
- Failure tags: `identity_drift`, `accessory_deformed`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4/5 / 4.5/5 / 4/5 / 4/5 / 2/5 / 3/5
- Acceptable: No.
- Reason: Pose is readable, but the pose-source prop leak and occlusion make it a poor choice for this task's role separation and 3D pose-recovery priority.

### Candidate C

- Correct: Preserves the character-source appearance while giving a clean full-body side-profile walk. The forward/back leg relationship is clear, both feet are visible, and arms remain unobstructed. No pose-source sword is copied.
- Problems: Arm swing is generic and does not reproduce the pose source's weapon-arm configuration; the torso leans and bulges slightly, and the sweatshirt shape softens the shoulder and hip landmarks.
- Failure tags: `pose_mismatch`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4/5 / 4.5/5 / 4/5 / 4.5/5 / 5/5 / 4/5
- Acceptable: Yes, relatively.
- Reason: Among the candidates, this gives the cleanest unobstructed full-body joint structure while avoiding role contamination from the pose-source prop.

### Candidate D

- Correct: Side-facing full-body walk is mostly preserved, with a readable stride and the character-source clothing and shoes retained.
- Problems: Copies the sword from the pose source, causing role leakage and occluding the hand/hip/thigh area. The prop also makes the rear arm hard to recover as an independent limb. The stride is slightly compressed compared with the clearest walking candidates.
- Failure tags: `identity_drift`, `accessory_deformed`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 4.5/5 / 4/5 / 4/5 / 2/5 / 3/5
- Acceptable: No.
- Reason: The pose is usable at a coarse level, but the imported sword and occlusion make it weaker for downstream 3D pose recovery.

## Best Candidate

- Best candidate: Candidate C.
- Reason: Candidate C is the best for downstream 3D pose recovery because it keeps a full-body side walk with clear leg separation, visible feet, unobstructed arms, and no copied sword from the pose source. Candidate B has a slightly stronger prop-related pose match, but the sword is role contamination and creates occlusion around important hand, hip, and thigh landmarks.
- Overall observation: All candidates capture the broad side-view walking setup and preserve the character source better than the pose-source identity. The main split is that B and D follow the sword-bearing reference too literally, while A and C are cleaner for character-only retargeting. C is only relatively best because its arm configuration is still generic and not an exact pose-source limb match.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
