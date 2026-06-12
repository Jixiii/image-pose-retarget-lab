# Blind Review: E005/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E005-r002-blind-review.md` and the images linked inside it.
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

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r002/outputs/ai_generate_7988_1.png)

`experiments/E005/runs/r002/outputs/ai_generate_7988_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r002/outputs/ai_generate_7988_2.png)

`experiments/E005/runs/r002/outputs/ai_generate_7988_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r002/outputs/ai_generate_7988_3.png)

`experiments/E005/runs/r002/outputs/ai_generate_7988_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E005/runs/r002/outputs/ai_generate_7988_4.png)

`experiments/E005/runs/r002/outputs/ai_generate_7988_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character source identity, hairstyle, orange sweater, denim shorts, and yellow shoes. Full body is visible and centered. The front-facing viewpoint and arm side correspondence are mostly aligned with the pose source: viewer-left arm is bent with the white object, viewer-right arm hangs down.
- Problems: Lower-body pose is over-interpreted into a lifted/crossed walking step; the raised foot and knee are more dynamic than the pose source and make the support structure less reliable for 3D recovery. The right hand gains a tan prop from the pose/reference side, so accessories are mixed rather than preserved. Some hip/leg proportions are softened by the generated clothing.
- Failure tags: `pose_mismatch`, `style_drift`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 7 / 8 / 8 / 8 / 4 / 7
- Acceptable: Borderline.
- Reason: Usable as a full-body image with mostly correct side ordering, but the lifted/crossed leg creates a less dependable joint configuration than the target pose.

### Candidate B

- Correct: Keeps the main character appearance and is full-body, front-facing, and uncropped. The arm layout follows the same visible side arrangement as the pose source, with the viewer-left arm bent and the viewer-right arm lowered.
- Problems: Body shape is noticeably swollen around the torso and shoulders, reducing anatomical clarity. The crossed/lifted leg is ambiguous, with weak foot contact and less readable knee/ankle structure. It also imports or invents a tan object in the lowered hand, which mixes reference-side details into the character.
- Failure tags: `pose_mismatch`, `style_drift`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 6 / 8 / 8 / 8 / 4 / 6
- Acceptable: No.
- Reason: The full body is visible, but the torso and lower-limb geometry are too soft for reliable downstream pose recovery.

### Candidate C

- Correct: Preserves the character identity and outfit well, remains centered, and keeps a clear front-facing full-body view. The legs are more grounded than A/B, with both feet visible and a readable crossed stance. The lowered arm is less occluded by a hallucinated prop than in A/B/D.
- Problems: The target arm pose is weakened: both arms hang more passively than the pose source, and the viewer-left forearm/object relationship is less clear. The right hand is malformed, and the knees/feet do not exactly match the pose source's compact stance. Some accessory detail from the character source is simplified.
- Failure tags: `pose_mismatch`, `accessory_lost`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 6 / 8 / 8 / 8 / 5 / 7
- Acceptable: Borderline.
- Reason: It has a stable full-body silhouette, but the arm pose and hand quality are not strong enough to be the best pose-recovery candidate.

### Candidate D

- Correct: Best preserves a usable full-body, front-facing skeleton. Both feet are visible and grounded, the crossed-leg stance is clear, the torso is upright, and the left/right arm arrangement matches the pose source visually. Identity, outfit colors, shoes, and hairstyle remain close to the character source.
- Problems: The lowered hand includes a tan prop that appears to come from the pose/reference side, so accessory preservation is imperfect. The pose is slightly simplified and more symmetric than the source, and the left hand/object partly occludes the wrist. Limb shape is not exact, but deformation is lower than in the other candidates.
- Failure tags: `pose_mismatch`, `style_drift`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 8 / 8 / 8 / 8 / 4 / 8
- Acceptable: Yes.
- Reason: It gives the clearest recoverable body structure: full-body visibility, grounded feet, readable knees/ankles, correct visible side ordering, and relatively low deformation.

## Best Candidate

- Best candidate: Candidate D.
- Reason: D is the strongest for downstream 3D pose recovery because it has the clearest full-body joint layout: upright front view, visible grounded feet, readable crossed-leg structure, and low body deformation. A is more dynamic but over-raises the leg, B has worse torso/lower-limb deformation, and C loses too much of the target arm pose.
- Overall observation: All candidates preserve the character source better than they preserve accessory semantics; several import or invent a tan object from the pose/reference side. For this review's priority, D is only relatively best, but it is the most usable candidate for recovering a stable pose skeleton.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
