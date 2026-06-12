# Blind Review: E006/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E006-r002-blind-review.md` and the images linked inside it.
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

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E006/runs/r002/outputs/ai_generate_8129_1.png)

`experiments/E006/runs/r002/outputs/ai_generate_8129_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E006/runs/r002/outputs/ai_generate_8129_2.png)

`experiments/E006/runs/r002/outputs/ai_generate_8129_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E006/runs/r002/outputs/ai_generate_8129_3.png)

`experiments/E006/runs/r002/outputs/ai_generate_8129_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E006/runs/r002/outputs/ai_generate_8129_4.png)

`experiments/E006/runs/r002/outputs/ai_generate_8129_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the character source identity, orange sweater, shorts, shoes, and front-facing full-body framing. The viewer-left/character-right hand carries the blade-like object on the same side as the pose source, and the legs form a readable walking/cross-step structure.
- Problems: The target pose is softened into a natural human walk rather than the exact low-poly limb arrangement. The non-blade hand loses the pose-source stick/cylinder, the blade shape is simplified, and the leg crossing/weight-bearing side is only approximate.
- Failure tags: `pose_mismatch`, `accessory_lost`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4/5 / 4/5 / 4/5 / 5/5 / 3/5 / 4/5
- Acceptable: Yes, relatively.
- Reason: Best full-body pose readability among the candidates: limbs are visible, the skeleton is recoverable, and the main left/right object placement is preserved despite accessory and exact-pose errors.

### Candidate B

- Correct: Preserves the character identity and clothing well, stays centered and uncropped, and places the blade-like object on the viewer-left/character-right side. The body remains front-facing with readable major joints.
- Problems: The walking pose is weaker than the source: the legs are close to a straight standing stride, with less clear lifted/weight-bearing structure. The viewer-right/character-left hand becomes a pointing hand rather than holding the stick/cylinder, and the hand shape is somewhat unnatural.
- Failure tags: `pose_mismatch`, `accessory_lost`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 4/5 / 4/5 / 5/5 / 3/5 / 4/5
- Acceptable: Borderline.
- Reason: The body is usable for 3D pose recovery, but the source walk has been reduced to a mild forward step and loses one reference accessory.

### Candidate C

- Correct: Maintains the character source appearance, full-body visibility, front-facing view, and viewer-left/character-right blade placement. Limb boundaries are mostly clean.
- Problems: The pose is too static and upright compared with the source; the legs do not clearly reproduce the stepping/crossing pattern or weight shift. The viewer-right/character-left accessory is missing, and the non-blade hand is simplified into a narrow downward shape.
- Failure tags: `pose_mismatch`, `accessory_lost`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2/5 / 4/5 / 4/5 / 5/5 / 3/5 / 4/5
- Acceptable: No.
- Reason: It is visually clean, but for downstream pose recovery it reads closer to a neutral standing pose than the requested walking pose.

### Candidate D

- Correct: Keeps the character source outfit and full-body frontal framing. The blade-like object remains on the viewer-left/character-right side, and the legs show some asymmetric stepping.
- Problems: The pose is less clean than Candidate A: the feet and lower-leg relation are ambiguous, the torso/arms are closer to rest than the source, and the blade is deformed into a knife-like shape. The viewer-right/character-left hand loses the source accessory and is not very useful for joint interpretation.
- Failure tags: `pose_mismatch`, `accessory_lost`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 4/5 / 4/5 / 5/5 / 2/5 / 3/5
- Acceptable: Borderline.
- Reason: It has some walking asymmetry, but the object deformation and less distinct lower-body structure make it weaker for pose recovery than Candidate A.

## Best Candidate

- Best candidate: Candidate A
- Reason: Candidate A gives the most usable downstream 3D pose cue set: full body visible, front-facing framing, clear separated limbs, a readable walking/cross-step silhouette, and mostly correct left/right placement of the blade-side arm. It is not an exact pose transfer, but it is the least bad option for recoverable joint structure.
- Overall observation: All candidates preserve the character source identity and avoid a role swap, but all simplify the pose source into a generic human walk and drop the viewer-right/character-left stick accessory. The main differences are in pose clarity: A is the clearest, B and D are usable but weaker, and C is too close to standing.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
