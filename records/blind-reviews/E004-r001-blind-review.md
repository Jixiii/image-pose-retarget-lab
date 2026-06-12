# Blind Review: E004/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E004-r001-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
Keep the exact character from image 1. Use image 2 only as the reference for the full-body pose, body orientation, camera viewpoint, and framing.

Transfer the full-body pose from image 2 onto the image 1 character while preserving image 1's identity, design, proportions, colors, materials, outfit, face, and texture details.

The output must match image 2's viewing angle: same front/side/back/three-quarter view, same body facing direction, same head direction, same camera height, same perspective, and same full-body framing. Do not convert the character to a default front view. Do not rotate the character away from the viewpoint shown in image 2.

Output one centered, uncropped, full-body image of only the image 1 character, with the entire body visible. Do not copy the image 2 character, clothing, colors, face, style, or create a hybrid.
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

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E004/runs/r001/outputs/ai_generate_7967_1.png)

`experiments/E004/runs/r001/outputs/ai_generate_7967_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E004/runs/r001/outputs/ai_generate_7967_2.png)

`experiments/E004/runs/r001/outputs/ai_generate_7967_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E004/runs/r001/outputs/ai_generate_7967_3.png)

`experiments/E004/runs/r001/outputs/ai_generate_7967_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E004/runs/r001/outputs/ai_generate_7967_4.png)

`experiments/E004/runs/r001/outputs/ai_generate_7967_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character-source identity much better than the other candidates: realistic female body, bun hairstyle, orange sweater with white chest mark, denim shorts, bare legs, socks, and yellow shoes are all recognizable. The figure is centered, full-body, front-facing, and the limbs are clean enough for downstream pose recovery. The sword-side placement appears broadly consistent with the pose source.
- Problems: The pose is only a loose match to the pose source. The pose source has a simple upright stance with one sword arm and one relaxed arm, while this output turns it into a walking/crossed-leg stance with both arms lowered. It also copies the sword from the pose source, which is not part of the character source. Lower-leg and foot placement are readable but not faithful to the reference stance.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5 / 4 / 3.5 / 4.5 / 3 / 4
- Acceptable: Borderline for pose-recovery use; not acceptable as a strict retarget.
- Reason: The retargeted pose is inaccurate, but the full-body structure is visible, low-deformation, and attached to the correct character identity.

### Candidate B

- Correct: Keeps a front-facing, full-body composition and has a readable head/torso/limb layout. The hands are visible and separated enough to infer an upper-body pose.
- Problems: This is a role swap: it copies the low-poly pose-source character, clothing, hair, face style, boots, and sword instead of the character-source woman. The pose also does not match the pose source well; both hands are lifted forward like the character-source pose rather than one arm holding the sword lower and the other arm relaxed. The lower body is stiff, with weak foot contact and an unclear weight-bearing structure.
- Failure tags: `role_swap`, `identity_drift`, `style_drift`, `pose_mismatch`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 4 / 2.5 / 0 / 0 / 2.5
- Acceptable: No.
- Reason: The body is readable, but it solves the wrong role and gives a pose closer to the character-source crouch than to the requested pose source.

### Candidate C

- Correct: Full body is visible, the torso and limbs are cleanly separated, and the feet are more grounded than in Candidate B. It has relatively usable joint structure and low deformation for pose recovery.
- Problems: This is also a role swap, retaining the low-poly pose-source boy rather than the character-source woman. The pose is not the pose-source stance: both arms are raised, the knees are bent, and the body leans into a defensive/crouched posture. The sword is carried forward on the viewer-left side rather than matching the simpler relaxed sword-bearing reference structure.
- Failure tags: `role_swap`, `identity_drift`, `style_drift`, `pose_mismatch`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5 / 3.5 / 2 / 0 / 0 / 3.5
- Acceptable: No.
- Reason: It is structurally readable, but the output character and pose are both substantially wrong for the task.

### Candidate D

- Correct: Full body is visible, the silhouette is mostly coherent, and the upper-body joints are easy to locate. The image is low-deformation and readable as a single figure.
- Problems: It copies the pose-source character identity and style, losing the character-source woman entirely. The pose is again closer to the character-source bent-knee, hands-forward posture than to the pose-source upright stance. The sword appears on the opposite side of the body compared with the clearest pose-source cue, making left/right correspondence unreliable. The legs are simplified and do not preserve the pose-source foot placement.
- Failure tags: `role_swap`, `identity_drift`, `style_drift`, `pose_mismatch`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 3.5 / 1.5 / 0 / 0 / 3
- Acceptable: No.
- Reason: It is a clean image, but it is not a valid character retarget and has unreliable left/right mapping.

## Best Candidate

- Best candidate: Candidate A
- Reason: Candidate A is the only output that keeps the intended character source while remaining full-body, centered, and anatomically usable for downstream 3D pose recovery. Its pose match is weak, especially in the arms and stepping stance, but B-D are all role swaps that copy the pose-source character and therefore fail the central retargeting requirement.
- Overall observation: All candidates are flawed. A is only the relative best because it preserves identity and gives a clean recoverable body. B-D have readable low-poly bodies, but they mostly transfer the wrong direction: they keep the pose-source identity and borrow the character-source crouched/raised-hand pose rather than placing the character-source woman into the pose-source stance.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
