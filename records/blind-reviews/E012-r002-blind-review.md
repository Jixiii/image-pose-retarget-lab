# Blind Review: E012/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E012-r002-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
Images 1-3 = CHARACTER SOURCES. Images 4-6 = POSE SOURCES. Do not swap these roles.

Use Images 1-3 as references for the same character. Image 1 is the primary character source; the other character images provide additional appearance details and views.

Use Images 4-6 as references for the same pose. Image 4 is the primary pose source and controls the final camera viewpoint, body facing direction, and framing.

Generate one centered, uncropped, full-body image of the exact character from the character sources performing the pose from the pose sources.

Preserve the character sources' identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use the pose sources' character identity, face, outfit, colors, materials, or style.

Use the pose sources only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match image 4's viewing angle and body facing direction.

Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from the pose sources: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in the pose sources.

The character sources always control appearance. The pose sources only control pose and viewpoint. Do not create a hybrid.
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

![Input 4: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-X.png)

`datasets/assets/native_1/renders/native1-frame11-X.png`

### Input 5: Pose Source 2

![Input 5: Pose Source 2](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11--Y.png)

`datasets/assets/native_1/renders/native1-frame11--Y.png`

### Input 6: Pose Source 3

![Input 6: Pose Source 3](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-Y.png)

`datasets/assets/native_1/renders/native1-frame11-Y.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E012/runs/r002/outputs/ai_generate_8444_1.png)

`experiments/E012/runs/r002/outputs/ai_generate_8444_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E012/runs/r002/outputs/ai_generate_8444_2.png)

`experiments/E012/runs/r002/outputs/ai_generate_8444_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E012/runs/r002/outputs/ai_generate_8444_3.png)

`experiments/E012/runs/r002/outputs/ai_generate_8444_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E012/runs/r002/outputs/ai_generate_8444_4.png)

`experiments/E012/runs/r002/outputs/ai_generate_8444_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character-source identity, hair, yellow sweatshirt, shorts, shoes, and overall body proportions well. The body is full-frame and mostly unoccluded, with readable head, torso, arms, knees, feet, and a clear side-walking silhouette.
- Problems: The pose only loosely matches the pose source. It adopts a side-view walking pose instead of the primary pose source's more front-facing camera, and the leg action is wrong: both feet are effectively grounded and the rear/raised-leg structure from the pose source is lost. The free arm is relaxed rather than matching the source limb arrangement, and the sword/object copied from the pose source adds appearance leakage and partially occludes the hip/hand area.
- Failure tags: `pose_mismatch`, `view_mismatch`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 2/5 / 3/5 / 5/5 / 3/5 / 4/5
- Acceptable: Marginal.
- Reason: For downstream 3D pose recovery, this is the cleanest skeleton-like candidate because most joints and both feet are visible with low deformation, but the target pose is only approximate.

### Candidate B

- Correct: Keeps the character-source appearance strongly and provides a full-body image. The sword is straight and the output has a readable walking stride.
- Problems: The body orientation is inconsistent with the primary pose source and appears closer to a mirrored/alternate side reference. The legs cross heavily, making hip, knee, and foot correspondence ambiguous for 3D recovery. The front/back limb order is hard to trust, the non-sword hand is weakly posed, and the copied sword creates pose-source accessory leakage while occluding the hand/shorts area.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`, `style_drift`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3/5 / 2/5 / 2/5 / 5/5 / 3/5 / 3/5
- Acceptable: No.
- Reason: It is visually coherent, but the crossed legs and uncertain left/right limb assignment make it weaker than Candidate A for recoverable joint structure.

### Candidate C

- Correct: Preserves the character-source identity, clothing, face, and full-body framing. The side-facing direction and sword-holding action are broadly related to the pose references.
- Problems: The lower body is too occluded and compressed: the legs cross through each other, one thigh/knee relationship is hard to read, and the pose no longer has the clear lifted/back-leg structure from the source. The arm holding the sword is partly hidden, the free hand is passive, and the copied sword is appearance leakage from the pose source. The viewpoint also follows a side reference rather than the primary pose source.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`, `style_drift`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2/5 / 2/5 / 2/5 / 5/5 / 3/5 / 3/5
- Acceptable: No.
- Reason: The character is clean, but the crossed/merged lower-body structure is not reliable enough for downstream pose recovery.

### Candidate D

- Correct: Full-body visibility is good, the side profile is clean, the sword is straight and readable, and character-source appearance is mostly preserved.
- Problems: The pose is too upright and static compared with the source walking/running pose. The rear/lifted leg structure is missing, both legs are nearly straight, and only one arm is clearly recoverable because the far arm is hidden or fused into the body profile. It also uses the opposite/alternate side-view orientation instead of the primary pose source and copies the sword from the pose source.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`, `style_drift`, `missing_limb`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2/5 / 2/5 / 2/5 / 5/5 / 3/5 / 3/5
- Acceptable: No.
- Reason: The silhouette is clean, but missing/hidden arm information and the simplified leg pose make the joint structure less useful than Candidate A.

## Best Candidate

- Best candidate: Candidate A.
- Reason: Candidate A is only relatively best. It has the clearest full-body joint layout, least limb occlusion, lowest deformation, and the most usable feet/knee/arm visibility for downstream 3D pose recovery. It still fails the exact target pose and primary viewpoint, but the other candidates introduce worse leg crossing, left/right ambiguity, or hidden limb structure.
- Overall observation: All candidates preserve the character-source identity well, but all drift toward side-view walking outputs and copy the sword/object from the pose source. None accurately reproduces the source pose's limb arrangement or primary camera view, so this run should be treated as a weak pose-transfer result even though Candidate A is the most recoverable candidate.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
