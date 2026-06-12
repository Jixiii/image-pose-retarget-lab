# Blind Review: E005/r003

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E005-r003-blind-review.md` and the images linked inside it.
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

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r003/outputs/ai_generate_8002_1.png)

`experiments/E005/runs/r003/outputs/ai_generate_8002_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r003/outputs/ai_generate_8002_2.png)

`experiments/E005/runs/r003/outputs/ai_generate_8002_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r003/outputs/ai_generate_8002_3.png)

`experiments/E005/runs/r003/outputs/ai_generate_8002_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r003/outputs/ai_generate_8002_4.png)

`experiments/E005/runs/r003/outputs/ai_generate_8002_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the character-source identity, orange sweatshirt, denim shorts, hair bun, yellow shoes, and a full-body frontal framing. The output uses the pose source mainly for an upright walking/standing pose with one arm lowered holding a white prop and the opposite arm hanging down.
- Problems: The pose is only partially matched. The torso is too naturalistic and softened compared with the pose source's simple front-facing stance, and the legs are crossed/overlapped enough that the exact knee and foot order is hard to recover. The held prop is simplified into a plain white cylinder and the hand contact is not very clear. The feet remain visible, but the rear foot and ankle are partly hidden by overlap.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 4 / 3 / 5 / 3 / 4
- Acceptable: Marginal.
- Reason: The full body is visible and the gross limb layout is usable, but the crossed lower legs and simplified prop reduce reliability for downstream 3D pose recovery.

### Candidate B

- Correct: Preserves the character-source appearance well and keeps a centered, full-body frontal view. The lowered prop-holding arm, opposite hanging arm, slight forward/downward head angle, and walking/stepping leg arrangement are reasonably close to the pose source. Most joints are visible enough to infer a skeleton.
- Problems: The legs are still more human-walk stylized than the pose source and overlap near the ankles, so depth order is not perfectly clear. The white prop is simplified and shifted into a flat rectangular object rather than the source's sword-like shape. The stance is smoother and less block-structured than the pose reference.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 4 / 5 / 3 / 4
- Acceptable: Yes.
- Reason: This is the most recoverable pose: full body, clear torso orientation, visible arms, visible knees, visible feet, and no severe anatomical deformation.

### Candidate C

- Correct: Keeps the source character identity and gives a complete, uncropped body with generous background margin. The prop-holding arm and relaxed opposite arm roughly follow the pose source, and the frontal viewpoint is maintained.
- Problems: The figure is smaller in frame, which makes hand, foot, and joint details less useful for pose recovery. The upper body and legs drift toward a generic walking pose, with the front/back relationship of the feet less clear than in Candidate B. The prop is enlarged into a thicker white handle and its connection to the hand is ambiguous.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `framing_error`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 4 / 3 / 5 / 2 / 4
- Acceptable: Marginal.
- Reason: Full-body visibility is good, but the reduced subject scale and unclear lower-limb ordering make it less useful than Candidate B for 3D pose recovery.

### Candidate D

- Correct: Keeps the character-source identity and provides a clean, centered, full-body frontal view. Both legs and arms are visible, with little cropping.
- Problems: The pose is too static and symmetrical compared with the pose source; the stepping/walking structure is weakened. The held object is badly malformed into a large white folded/blob-like shape, which can confuse hand and wrist localization. The lower body has less convincing weight shift, and the feet are close enough that the intended limb correspondence is less clear.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 4 / 3 / 5 / 1 / 3
- Acceptable: No.
- Reason: Although the silhouette is complete, the pose match and prop geometry are too degraded for reliable downstream recovery.

## Best Candidate

- Best candidate: Candidate B.
- Reason: Candidate B has the clearest usable skeleton for downstream 3D pose recovery. It preserves the full body, keeps the frontal viewpoint, shows both arms and both legs with relatively low deformation, and best maintains the pose source's prop-side arm versus relaxed opposite arm structure. Its lower-leg overlap and simplified prop are flaws, but they are less damaging than the smaller scale of Candidate C, the crossed/ambiguous legs of Candidate A, and the malformed prop/static pose of Candidate D.
- Overall observation: All candidates transfer the character identity more successfully than the exact low-poly pose. The main recurring issue is that the pose source is converted into a generic human walking/standing pose, with softened limb correspondence and simplified or deformed prop geometry. For pose-recovery use, Candidate B is only relatively best rather than clean.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
