# Blind Review: E002/r003

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E002-r003-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
Keep the exact character from image 1. Use image 2 only as a pose reference. Transfer the full-body pose from image 2 onto the image 1 character while preserving image 1's identity, design, proportions, colors, and materials. Output one centered, uncropped, full-body image. Do not copy the image 2 character or create a hybrid.
```

### Input Role Assumption

- Input 1 is treated as the character source unless the visible record clearly says otherwise.
- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.

## Inputs

### Input 1: Character Source

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose1.png)

`datasets/assets/native_1/renders/native1-pose1.png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r003/outputs/ai_generate_7940_1.png)

`experiments/E002/runs/r003/outputs/ai_generate_7940_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r003/outputs/ai_generate_7940_2.png)

`experiments/E002/runs/r003/outputs/ai_generate_7940_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E002/runs/r003/outputs/ai_generate_7940_3.png)

`experiments/E002/runs/r003/outputs/ai_generate_7940_3.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the source character identity well: low-poly boy design, hair, blue sleeves/pants, brown vest, boots, belt pouch, sword, and visible joint/control markers remain recognizable. The output is centered and nearly full-body. Both hands are brought forward, so the upper-body intent is partially captured.
- Problems: Lower body does not match the pose source well. The pose source has a crouched, forward-leaning stance with bent knees and asymmetric weight, but this candidate stays mostly upright with only a mild leg bend. Torso lean is weak. Hands/forearms are forward but lower and flatter than the pose reference, and the fingers introduce some small deformation. The feet/ground contact are not as clear as the pose source.
- Failure tags: `pose_mismatch`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5 / 4 / 4 / 4.5 / 4.5 / 3.5
- Acceptable: Borderline no.
- Reason: Good identity and accessories, but the target pose is only partially transferred; for downstream 3D pose recovery, the upright lower body would likely recover the wrong leg structure.

### Candidate B

- Correct: Keeps the character broadly recognizable and centered, with full-body visibility. The front-facing view is stable and the body is not heavily deformed.
- Problems: The target pose is mostly lost. One arm remains down holding the sword instead of both arms bending forward at chest height. The legs read as a simple standing or walking pose, not the crouched asymmetric stance from the pose source. The belt pouch and visible joint/control markers are lost, and the sword changes shape/material. Because the limbs do not follow the reference pose, left/right correctness is not meaningfully reliable.
- Failure tags: `pose_mismatch`, `accessory_lost`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 1.5 / 4 / 2 / 3.5 / 2 / 3.5
- Acceptable: No.
- Reason: Clean render, but it is not a useful pose-retarget result for 3D pose recovery because the arm and leg configuration is far from the pose source.

### Candidate C

- Correct: Best captures the pose source structure. The torso leans forward, both elbows are bent forward near chest height, and the legs form a clearer crouched asymmetric stance with readable knee bends and foot placement. Full body is visible, with no extra or missing limbs, and the character identity remains recognizable through the hair, face style, vest, blue clothing, pants, and boots.
- Problems: Viewpoint shifts toward a stronger three-quarter angle than the pose source, which is closer to front-facing. Hands are simplified into mitten/fist shapes instead of matching the reference hand pose. The sword, belt pouch, and visible joint/control markers are missing, so accessory preservation is poor. Some lower-body proportions are softened, especially around the hips and thighs, though the joint layout remains usable.
- Failure tags: `view_mismatch`, `accessory_lost`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 3 / 4 / 3.5 / 1.5 / 4
- Acceptable: Yes, with caveats.
- Reason: Despite accessory loss and a mild view mismatch, this candidate gives the clearest recoverable full-body pose and the least ambiguous limb structure.

## Best Candidate

- Best candidate: Candidate C.
- Reason: Candidate C is the most useful for downstream 3D pose recovery because it has the clearest crouched stance, forward-bent arms, full-body visibility, readable knees/feet, and no major limb deformation. Candidate A preserves identity and accessories better, but its lower-body pose is too upright. Candidate B is visually clean but misses the target pose.
- Overall observation: All candidates preserve the character better than they preserve every pose detail. Candidate C should be selected when pose recoverability is the priority; Candidate A would only be preferable if source accessories and visible control markers mattered more than accurate lower-body pose.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
