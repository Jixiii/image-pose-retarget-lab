# Blind Review: E006/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E006-r001-blind-review.md` and the images linked inside it.
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

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-noSkeleton-pose1.png)

`datasets/assets/native_1/renders/native1-noSkeleton-pose1.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E006/runs/r001/outputs/ai_generate_8127_1.png)

`experiments/E006/runs/r001/outputs/ai_generate_8127_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E006/runs/r001/outputs/ai_generate_8127_2.png)

`experiments/E006/runs/r001/outputs/ai_generate_8127_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E006/runs/r001/outputs/ai_generate_8127_3.png)

`experiments/E006/runs/r001/outputs/ai_generate_8127_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E006/runs/r001/outputs/ai_generate_8127_4.png)

`experiments/E006/runs/r001/outputs/ai_generate_8127_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the character-source identity, sweatshirt, shorts, shoes, and full-body framing. The output is front-facing like the pose source and gives a usable walking structure: the viewer-left leg is the forward/bent leg and the viewer-right leg remains more weight-bearing.
- Problems: The pose is softened toward a neutral walk. The pose-source arm asymmetry is mostly lost: both arms hang naturally instead of preserving the stronger bent/held-arm structure. The raised/forward leg is not as high or blocky-clear as the pose source, so joint recovery would be approximate rather than exact.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 4.5/5 / 4/5 / 5/5 / 5/5 / 4.5/5
- Acceptable: Yes, relatively.
- Reason: It is full-body, low-deformation, frontal, and has the least confusing limb structure among the candidates, even though the arm pose is under-matched.

### Candidate B

- Correct: Preserves the character-source appearance well and remains a centered, uncropped full-body image. It attempts the same frontal walking stance with one leg forward and one leg more vertical.
- Problems: The lower-body pose is less clear than Candidate A: the legs overlap more, the knee/foot relationship is harder to read, and the weight-bearing structure is ambiguous. Arm positions remain too neutral and do not match the pose source's asymmetric held-arm silhouette.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 4.5/5 / 3.5/5 / 5/5 / 5/5 / 4/5
- Acceptable: Borderline.
- Reason: It is visually clean, but the leg overlap and softened arm pose reduce its value for 3D pose recovery.

### Candidate C

- Correct: Keeps much of the character-source clothing and body identity, and the stride is visually dynamic with a clear crossed-leg walking action. The body is fully visible.
- Problems: The viewpoint is wrong: it turns into a 3/4 side walking view instead of the pose source's mostly frontal view. It imports the pose-source sword/prop even though the character source has no such accessory, and the prop/hand area partially occludes the limb structure. The crossed legs are exaggerated and can confuse left/right and depth ordering for recovery.
- Failure tags: `view_mismatch`, `style_drift`, `accessory_deformed`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5/5 / 2/5 / 2.5/5 / 4/5 / 1/5 / 3.5/5
- Acceptable: No.
- Reason: The pose is expressive but not faithful enough to the source viewpoint, and the added sword/occlusion makes the joint structure less usable.

### Candidate D

- Correct: Preserves the character-source identity and outfit, stays front-facing, and keeps the body uncropped with low visible deformation.
- Problems: The pose collapses closest to a neutral standing/walking frame. The forward leg is weakly expressed, both legs are almost vertical, and the pose-source asymmetric arm arrangement is not preserved. The viewer-right foot/sole is somewhat odd and could introduce foot-orientation noise.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5/5 / 4.5/5 / 3/5 / 5/5 / 5/5 / 4/5
- Acceptable: No.
- Reason: It is clean and full-body, but the target pose is too diluted for reliable pose-transfer evaluation.

## Best Candidate

- Best candidate: Candidate A
- Reason: Candidate A is the best fit for downstream 3D pose recovery because it keeps a frontal, uncropped, low-deformation full body while preserving the clearest target-like walking structure without importing the pose-source sword or style. It is only relatively best: the arm pose is too neutral and the leg lift is softened, but its left/right and joint layout are more recoverable than the other candidates.
- Overall observation: All candidates preserve the character identity better than they preserve the pose. The main failure mode is pose dilution toward a generic walk/stand; Candidate C is the only strongly dynamic version, but it pays for that with viewpoint drift, an added prop, and less reliable limb correspondence.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
