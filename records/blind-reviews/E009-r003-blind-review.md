# Blind Review: E009/r003

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E009-r003-blind-review.md` and the images linked inside it.
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

Use image 1 as the only source for identity, character design, body proportions, topology, face, hairstyle, outfit, colors, materials, accessories, props, equipment, and local part shapes. Preserve all visible character-specific details from image 1, including any held objects or attached accessories. Do not remove, hide, duplicate, replace, or redesign them.

Use image 2 only for pose, limb arrangement, body orientation, camera viewpoint, and framing. Match the pose and viewpoint from image 2, but do not copy image 2's identity, clothing, materials, accessories, props, style, topology, surface details, or local part shapes.

When transferring the pose, preserve image 1's stylization, topology, and local part shapes. Do not import local shape details, surface details, or part topology from image 2.

Do not mirror, flip, or left-right swap the pose. Preserve exact limb correspondence: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg.

If image 1's character design conflicts with image 2's body appearance, image 1 always wins for appearance and topology. Image 2 only controls pose, viewpoint, and framing. Do not create a hybrid.
```

### Input Role Assumption

- Input 1 is treated as the character source unless the visible record clearly says otherwise.
- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.

## Inputs

### Input 1: Character Source

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-noSkeleton-rest-pose1-X.png)

`datasets/assets/native_1/renders/native1-noSkeleton-rest-pose1-X.png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2--X.png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2--X.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r003/outputs/ai_generate_8301_1.png)

`experiments/E009/runs/r003/outputs/ai_generate_8301_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r003/outputs/ai_generate_8301_2.png)

`experiments/E009/runs/r003/outputs/ai_generate_8301_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r003/outputs/ai_generate_8301_3.png)

`experiments/E009/runs/r003/outputs/ai_generate_8301_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r003/outputs/ai_generate_8301_4.png)

`experiments/E009/runs/r003/outputs/ai_generate_8301_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character identity, low-poly material style, sword, vest, boots, and full-body visibility. The stance has a forward lean, bent knees, and one raised forward hand, so the broad action direction is partly readable.
- Problems: The body is still too front-facing compared with the pose source's side/profile view. The sword-side arm is pulled down and across the torso instead of joining the two raised forearms from the reference pose, so the upper-body joint structure is only partially recoverable. Leg spacing is plausible but does not clearly reproduce the pose source's long rear leg and forward supporting leg.
- Failure tags: `pose_mismatch`, `view_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 5 / 4 / 7 / 9 / 9 / 8
- Acceptable: No
- Reason: Usable as a stylized character image, but the side-view crouch and two-arm forward pose are too weak for reliable downstream 3D pose recovery.

### Candidate B

- Correct: Keeps the full body visible, preserves the character identity and sword, and gives the clearest grounded leg structure: rear leg extended back, front leg bent, both feet planted. Both forearms are raised in front of the torso, giving the most recoverable arm/hand pose among the candidates.
- Problems: The camera/viewpoint remains more front/three-quarter than the pose source's profile view. The sword-bearing forearm is lower and more horizontal than the reference arm, and the torso lean is milder than the pose source. Some hand detail is simplified, but the joints remain readable.
- Failure tags: `pose_mismatch`, `view_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 7 / 5 / 8 / 9 / 9 / 8
- Acceptable: Marginal
- Reason: Not a precise viewpoint match, but it has the best combination of full-body visibility, grounded legs, readable left/right limb layout, and low deformation.

### Candidate C

- Correct: Preserves the character identity and accessory, and both hands are raised in front of the body in a way that resembles the pose source better than A or D. The torso has a forward lean and the body is mostly full-frame.
- Problems: The lower body is unreliable for pose recovery: the screen-right foot appears lifted/floating rather than planted, and the leg placement does not clearly match the pose source's grounded staggered stance. The character is still too front-facing, and the sword is attached awkwardly along the forearm, partly confusing the wrist/hand structure.
- Failure tags: `pose_mismatch`, `view_mismatch`, `body_deformation`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 6 / 5 / 7 / 9 / 7 / 6
- Acceptable: No
- Reason: The upper-body pose is close, but the floating/unclear foot contact and accessory placement make the skeleton less dependable than Candidate B.

### Candidate D

- Correct: Preserves identity, full-body framing, sword, vest, boots, and a generally crouched stance with visible limbs.
- Problems: The sword-side arm is extended outward and downward instead of raised forward, so the two-arm pose from the reference is largely lost. The torso and head are more front-facing than the pose source, and the leg stance is broad but less faithful to the reference's staggered side-view weight bearing. The near hand/forearm relationship is less clear than B.
- Failure tags: `pose_mismatch`, `view_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 7 / 9 / 9 / 8
- Acceptable: No
- Reason: Character preservation is strong, but the reference pose is not sufficiently transferred for 3D pose recovery.

## Best Candidate

- Best candidate: Candidate B
- Reason: Candidate B is only relatively best, but it gives the clearest recoverable skeleton for downstream 3D pose recovery: full body visible, both feet grounded, legs in a readable stagger, both forearms raised forward, no major limb deformation, and the character/source accessory identity is preserved.
- Overall observation: All candidates preserve the native character better than they match the pose source viewpoint. The main shared failure is `view_mismatch`: none fully adopts the pose source's side/profile camera angle. For pose recovery, Candidate B is preferable because its joint layout is more complete and stable even though the viewpoint and arm heights are imperfect.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
