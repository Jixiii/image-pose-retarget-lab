# Blind Review: E005/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E005-r001-blind-review.md` and the images linked inside it.
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

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose1.png)

`datasets/assets/native_1/renders/native1-pose1.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r001/outputs/ai_generate_7986_1.png)

`experiments/E005/runs/r001/outputs/ai_generate_7986_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r001/outputs/ai_generate_7986_2.png)

`experiments/E005/runs/r001/outputs/ai_generate_7986_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r001/outputs/ai_generate_7986_3.png)

`experiments/E005/runs/r001/outputs/ai_generate_7986_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r001/outputs/ai_generate_7986_4.png)

`experiments/E005/runs/r001/outputs/ai_generate_7986_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Full body is visible and centered; the result keeps the human character identity, orange sweatshirt, denim shorts, yellow shoes, and the sweatshirt cat graphic better than the other candidates. It is front-facing like the pose source, with the sword/hand placed on the same image side as the pose reference.
- Problems: The lower-body pose is only approximate: it becomes a natural walking step rather than the pose source's more compact front-facing stance. The sword is imported from the pose source even though the pose source should not control accessories. The arm and hand structure is usable but not very close to the blocky source pose.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 4/5 / 4/5 / 4/5 / 3/5 / 4/5
- Acceptable: Borderline, and only as the relatively best option for pose-recovery use.
- Reason: It has the clearest full-body frontal structure with low deformation and mostly correct side correspondence, but the pose is not exact and the unwanted sword contaminates the character-only appearance.

### Candidate B

- Correct: Full body is visible; the limbs form a clean, readable walking pose with low anatomical deformation. Character clothing, hairstyle, shorts, and shoes are mostly retained.
- Problems: The camera/viewpoint changes to a side or strong three-quarter walking view, while the pose source is front-facing. The stride pose does not match the pose source's stance, and the side view makes left/right correspondence harder to recover. The sword is imported from the pose source, and the sweatshirt cat graphic loses its facial details.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`, `style_drift`, `accessory_lost`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2/5 / 1/5 / 2/5 / 3/5 / 2/5 / 4/5
- Acceptable: No.
- Reason: Although visually coherent, it changes the viewpoint and body orientation too much for reliable downstream 3D pose recovery against the reference.

### Candidate C

- Correct: Full body is visible, centered, and front-facing. The result preserves the main character clothing and body identity, and the limbs are anatomically clean.
- Problems: The pose collapses toward a neutral standing posture: both legs are nearly straight and the arms are too relaxed compared with the pose source. It imports the pose-source sword, loses the cat face detail on the sweatshirt, and provides less useful lower-body asymmetry for pose recovery.
- Failure tags: `pose_mismatch`, `accessory_lost`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2/5 / 4/5 / 4/5 / 4/5 / 2/5 / 4/5
- Acceptable: No.
- Reason: It is clean and frontal, but the body pose is too neutral and loses important reference-pose structure.

### Candidate D

- Correct: Full body is visible and front-facing, with a clear asymmetric lower-body step/crossing structure. The main character identity, outfit colors, shorts, shoes, and hairstyle are preserved, and the body has low deformation.
- Problems: The sword arm is raised and angled differently from the pose source, so the upper-body pose is less faithful than Candidate A. The sword is still an unwanted pose-source accessory, and the sweatshirt cat graphic loses its face detail. The leg arrangement is clearer than Candidate C but still not an exact match to the reference stance.
- Failure tags: `pose_mismatch`, `accessory_lost`, `accessory_deformed`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 4/5 / 4/5 / 4/5 / 2/5 / 4/5
- Acceptable: Borderline, but weaker than Candidate A.
- Reason: It has good full-body visibility and usable joint structure, but the arm/sword pose diverges more from the reference and the accessory contamination is stronger.

## Best Candidate

- Best candidate: Candidate A.
- Reason: Candidate A is the most usable for downstream 3D pose recovery because it is full-body, frontal, low-deformation, and keeps the most reliable left/right correspondence while preserving the character identity. It is not a strict success: the lower-body pose is only approximate and it incorrectly imports the pose-source sword. Still, compared with B's viewpoint failure, C's neutralized pose, and D's upper-body/sword mismatch, A has the best combined pose clarity and recoverable joint structure.
- Overall observation: All candidates preserve the human character better than the low-poly pose-source identity, but all contaminate the result with the pose-source sword. None is a clean retarget. For pose-recovery priority, frontal full-body visibility and low deformation make A the least flawed output.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
