# Blind Review: E009/r004

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E009-r004-blind-review.md` and the images linked inside it.
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

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r004/outputs/ai_generate_8317_1.png)

`experiments/E009/runs/r004/outputs/ai_generate_8317_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r004/outputs/ai_generate_8317_2.png)

`experiments/E009/runs/r004/outputs/ai_generate_8317_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r004/outputs/ai_generate_8317_3.png)

`experiments/E009/runs/r004/outputs/ai_generate_8317_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r004/outputs/ai_generate_8317_4.png)

`experiments/E009/runs/r004/outputs/ai_generate_8317_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the low-poly character identity, clothing colors, boots, hair, and sword. The body is full enough for joint recovery and the camera is mostly a right-facing side view.
- Problems: The pose only partially follows the reference. The legs form a crouch, but the upper body is closer to a guarded sword stance: the sword arm is held upright across the torso and the other arm is extended upward instead of both forearms being forward in the reference pose. The hand and sword placement make the arm endpoints less reliable for downstream pose recovery.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 4 / 3 / 4 / 3 / 4
- Acceptable: No.
- Reason: Clear full-body character, but the upper-limb pose is too different from the pose source for reliable 3D pose recovery.

### Candidate B

- Correct: Best overall match to the reference pose structure. The character faces right in side view, leans forward, has a clear crouched stance, and both arms are raised in front of the torso. Full-body visibility and joint readability are good.
- Problems: The hands become compact fists rather than the open, relaxed hands in the pose source. The sword is moved vertically between the forearms and partly obscures the wrist/hand relationship, so accessory-hand correspondence is ambiguous. The exact front/back limb correspondence is not fully verifiable from the silhouette.
- Failure tags: `accessory_deformed`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 3 / 4 / 3 / 4
- Acceptable: Yes, relatively.
- Reason: Despite hand and sword issues, the whole-body pose is clear, full-body, and the least ambiguous for recovering a usable skeleton.

### Candidate C

- Correct: Strong side-view framing with a forward lean, bent knees, and both arms raised forward. The open hand shapes are closer to the pose source than Candidate B, and the character identity is mostly preserved.
- Problems: The sword is no longer plausibly held in the correct hand; it protrudes diagonally from the lower arm/hip area and cuts across the pose. This creates ambiguity around the right-side forearm, wrist, and accessory relationship. The lower body is usable, but the upper-limb structure is less clean than B for pose recovery.
- Failure tags: `accessory_deformed`, `body_deformation`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 3 / 4 / 2 / 3
- Acceptable: Borderline.
- Reason: The pose is close, but the sword/arm intersection makes the joint structure less reliable for downstream 3D recovery.

### Candidate D

- Correct: Preserves the character design, sword, full-body framing, and a mostly right-facing side view. The legs are bent enough to suggest a crouched stance.
- Problems: The arm pose is substantially wrong: the sword arm trails horizontally across the body and the other arm reaches outward/upward, rather than both arms being forward in the reference pose. The result reads more like an action/swing pose than the source's guarded forward pose. This weakens both pose match and left/right confidence.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 4 / 3 / 4 / 3 / 4
- Acceptable: No.
- Reason: The body is visible and clean, but the upper-body pose is too far from the source pose.

## Best Candidate

- Best candidate: Candidate B.
- Reason: Candidate B gives the clearest recoverable whole-body pose: full-body visibility, right-facing side view, forward torso lean, bent knees, and both arms positioned forward. It has flaws in hand shape and sword placement, but it introduces fewer joint ambiguities than Candidate C and matches the pose source much better than Candidates A or D.
- Overall observation: All candidates preserve the character identity reasonably well and keep the body visible. The main failures are upper-limb fidelity and sword-hand consistency. For downstream 3D pose recovery, Candidate B is the least flawed because its skeleton-like structure is the most coherent.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
