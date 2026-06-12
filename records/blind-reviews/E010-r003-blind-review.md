# Blind Review: E010/r003

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E010-r003-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
Images 1-3 = CHARACTER SOURCES. Image 4 = POSE SOURCE. Do not swap these roles.

Use Images 1-3 as references for the same character. Image 1 is the primary character source; the other character images provide additional appearance details and views.

Generate one centered, uncropped, full-body image of the exact character from the character sources performing the pose from the pose source.

Preserve the character sources' identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use the pose source's character identity, face, outfit, colors, materials, or style.

Use the pose source only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match the pose source's viewing angle and body facing direction.

Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from the pose source: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in the pose source.

The character sources always control appearance. The pose source only controls pose and viewpoint. Do not create a hybrid.
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

![Input 4: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose6.png)

`datasets/assets/native_1/renders/native1-pose6.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r003/outputs/ai_generate_8338_1.png)

`experiments/E010/runs/r003/outputs/ai_generate_8338_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r003/outputs/ai_generate_8338_2.png)

`experiments/E010/runs/r003/outputs/ai_generate_8338_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r003/outputs/ai_generate_8338_3.png)

`experiments/E010/runs/r003/outputs/ai_generate_8338_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r003/outputs/ai_generate_8338_4.png)

`experiments/E010/runs/r003/outputs/ai_generate_8338_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the character-source human identity, outfit colors, side-facing orientation, full-body visibility, and a readable walking stride. The legs are separated enough for approximate hip/knee/ankle recovery.
- Problems: The sword is copied from the pose source even though it is not part of the character source. The sword angle and arm arrangement do not match the pose source well: the blade drops diagonally, the weapon hand is pulled behind the hip, and the free arm hangs in a different configuration. The torso and lower shirt area look slightly bulky/deformed, and the exact left/right limb correspondence is hard to verify from the generated side view.
- Failure tags: `pose_mismatch`, `style_drift`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 4 / 3 / 4 / 2 / 4
- Acceptable: Borderline.
- Reason: Usable as a side-view walking body, but the weapon/arm configuration is too different from the pose source for a clean downstream 3D pose target.

### Candidate B

- Correct: Best overall pose structure. The body is centered, uncropped, fully visible, and clearly side-facing to the right. The walking leg arrangement is readable, with one leg forward and one trailing behind, and the sword is held near the waist in a mostly horizontal direction similar to the pose source. Character identity, hairstyle, sweatshirt, shorts, and shoes are mostly preserved.
- Problems: The sword is still unwanted pose-source leakage, and the hand-to-hilt contact is not fully clean. The near arm is partly occluded by the torso and sword, so arm joint recovery is weaker than leg recovery. Minor torso bulk/cloth deformation remains.
- Failure tags: `style_drift`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 5 / 4 / 4 / 3 / 4
- Acceptable: Yes, relatively.
- Reason: It gives the clearest full-body side-view skeleton and the most pose-source-like stride among the candidates, with no obvious missing or extra limbs.

### Candidate C

- Correct: Maintains the same human character identity and a full-body right-facing side view. The walking stance is clear, with separated legs and visible feet, and the sword is roughly aligned with the pose-source direction.
- Problems: The sword/hand/hip region is more cluttered than Candidate B, making wrist and elbow structure harder to recover. The blade surface is visibly degraded and partially fused-looking, and the free arm is mostly hidden against the body. The stride is readable but a bit less clean for joint extraction because the weapon crosses the body and near thigh.
- Failure tags: `style_drift`, `accessory_deformed`, `body_deformation`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 5 / 4 / 4 / 2 / 3
- Acceptable: Borderline.
- Reason: The lower-body pose is usable, but the arm and sword area introduces too much ambiguity for high-confidence 3D pose recovery.

### Candidate D

- Correct: Preserves the character-source appearance and gives a centered, uncropped, right-facing side view with clear leg separation. The feet and main lower-body joints are reasonably readable.
- Problems: The sword points downward instead of staying close to the pose source's horizontal waist-level orientation. The hand grip and hilt placement are less anatomically clear, and the free arm hangs in a simplified pose that does not strongly match the pose source. The body silhouette is usable but slightly inflated around the torso/shorts area.
- Failure tags: `pose_mismatch`, `style_drift`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 5 / 3 / 4 / 2 / 3
- Acceptable: Borderline.
- Reason: Full-body leg recovery is possible, but the pose-source arm/weapon relationship is weaker than in Candidates B and C.

## Best Candidate

- Best candidate: Candidate B.
- Reason: Candidate B is the best fit for downstream 3D pose recovery because it has the clearest full-body side-view silhouette, the most readable walking leg structure, the least ambiguous limb layout, and the closest sword/arm orientation to the pose source. It is not perfect, but it is the least compromised candidate for skeletal recovery.
- Overall observation: All candidates preserve the character-source human identity better than the pose-source identity, but all also import the pose-source sword as an extra prop. For the stated priority, Candidate B should be preferred over the more visually similar but more cluttered Candidate C, and over Candidates A/D whose weapon angle and arm correspondence drift further from the pose source.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
