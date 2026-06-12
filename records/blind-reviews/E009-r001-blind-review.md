# Blind Review: E009/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E009-r001-blind-review.md` and the images linked inside it.
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

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-noSkeleton-rest-pose1-X.png)

`datasets/assets/native_1/renders/native1-noSkeleton-rest-pose1-X.png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2--X.png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2--X.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r001/outputs/ai_generate_8267_1.png)

`experiments/E009/runs/r001/outputs/ai_generate_8267_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r001/outputs/ai_generate_8267_2.png)

`experiments/E009/runs/r001/outputs/ai_generate_8267_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r001/outputs/ai_generate_8267_3.png)

`experiments/E009/runs/r001/outputs/ai_generate_8267_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r001/outputs/ai_generate_8267_4.png)

`experiments/E009/runs/r001/outputs/ai_generate_8267_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the native character identity and overall outfit colors, keeps a clear full-body standing figure, and matches the general side-facing guarded pose with both arms bent forward.
- Problems: The pose is compressed into a more generic crouched guard rather than the source's cleaner forward lean and leg geometry. The lower-body asymmetry is weaker than the pose reference, and the sword/accessory is completely missing.
- Failure tags: `pose_mismatch`, `view_mismatch`, `accessory_lost`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 4 / 4 / 1 / 4
- Acceptable: Yes
- Reason: Usable for downstream pose recovery because the body is fully visible and structurally coherent, but it loses the accessory and simplifies the target stance.

### Candidate B

- Correct: Keeps the correct character identity, shows the full body clearly, and gives the cleanest limb separation of the four candidates. The side-facing stance, bent arms, and front/back leg split are readable and suitable for pose extraction.
- Problems: The torso is still less aggressively pitched forward than the pose source, and the pose reads as a softened defensive stance rather than a tight match. The sword/accessory is missing.
- Failure tags: `pose_mismatch`, `view_mismatch`, `accessory_lost`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 4 / 4 / 1 / 5
- Acceptable: Yes
- Reason: Best balance of full-body visibility, low deformation, and recoverable joint structure, even though it still underfits the exact reference pose.

### Candidate C

- Correct: Preserves the native character appearance, keeps a full-body uncropped figure, and roughly follows the intended side-view guarded pose with both arms raised.
- Problems: The torso and head read more upright and slightly more front-facing than the pose source, so the reference viewpoint and body lean are diluted. The leg arrangement is cleaner than a failure case but less specific than Candidate B. The sword/accessory is missing.
- Failure tags: `pose_mismatch`, `view_mismatch`, `accessory_lost`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 3 / 4 / 4 / 1 / 5
- Acceptable: Borderline yes
- Reason: Still usable as a coarse pose image, but it drifts toward a generic stance and preserves less of the reference pose structure than A or B.

### Candidate D

- Correct: Full-body framing is intact, and the gross arm/leg layout is still readable as the intended side-facing guarded pose.
- Problems: The square blur over the face is a severe artifact and also suggests contamination from the pose-source image rather than clean preservation of the character source. Head orientation becomes less usable for downstream recovery, and the sword/accessory is missing. The stance is also softened relative to the pose source.
- Failure tags: `pose_mismatch`, `view_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 3 / 4 / 2 / 1 / 2
- Acceptable: No
- Reason: The body is mostly intact, but the face blur is a high-impact artifact and makes this clearly weaker than the other three for downstream 3D pose use.

## Best Candidate

- Best candidate: Candidate B
- Reason: Candidate B is the most usable for downstream 3D pose recovery. It has the cleanest full-body silhouette, the clearest separation between arms, torso, and legs, and low deformation throughout the figure. It still misses the sword and does not perfectly match the source's forward lean, but its joint structure is the easiest to read reliably.
- Overall observation: All four candidates preserve the broad side-facing guarded stance and keep the character identity better than the pose-source identity, but none reproduces the exact pose tightly. The consistent failure pattern is pose simplification plus loss of the sword/accessory. From a pose-recovery standpoint, B is relatively best, A is close behind, C is weaker because the stance is more generic, and D is clearly hurt by the face-blur artifact.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
