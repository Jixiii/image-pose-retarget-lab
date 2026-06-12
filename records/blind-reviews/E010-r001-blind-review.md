# Blind Review: E010/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E010-r001-blind-review.md` and the images linked inside it.
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

![Input 4: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-noSkeleton-pose1.png)

`datasets/assets/native_1/renders/native1-noSkeleton-pose1.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r001/outputs/ai_generate_8334_1.png)

`experiments/E010/runs/r001/outputs/ai_generate_8334_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r001/outputs/ai_generate_8334_2.png)

`experiments/E010/runs/r001/outputs/ai_generate_8334_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r001/outputs/ai_generate_8334_3.png)

`experiments/E010/runs/r001/outputs/ai_generate_8334_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r001/outputs/ai_generate_8334_4.png)

`experiments/E010/runs/r001/outputs/ai_generate_8334_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the main Body-Block identity well: orange sweatshirt, white chest graphic, denim shorts, yellow shoes, hair bun, and front-facing full-body framing. The body is centered and mostly readable for skeleton extraction.
- Problems: Pose is only partially transferred. The pose source's stepping structure is weakened because both feet read close to planted and the raised/bent leg is not very distinct. The head is bent downward more than the pose source, and the arms are relaxed instead of matching the source's asymmetric hand/forearm positions. A knife-like prop from the pose source is copied into the character, which is not part of the character source and may confuse hand/joint parsing.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5 / 4 / 3 / 4.5 / 3 / 4
- Acceptable: No
- Reason: Clean enough visually, but the target pose is too softened and the added weapon reduces usefulness for downstream 3D pose recovery.

### Candidate B

- Correct: Strong identity preservation and clean full-body visibility. The torso, hips, knees, ankles, and feet are easy to locate, and the front camera/viewpoint is close to the pose source.
- Problems: The pose collapses toward a neutral standing/walking pose. The pose source's bent/raised leg and asymmetric arm positions are not clearly reproduced. The left/right leg relationship appears ambiguous because the visible forward/crossing foot does not clearly match the pose source's lifted-side structure. A small knife-like prop is introduced from the pose source.
- Failure tags: `pose_mismatch`, `left_right_flip`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 4 / 2.5 / 4.5 / 3 / 4.5
- Acceptable: No
- Reason: This is clean for a generic body estimate, but it is not reliable as a retargeted version of the specific pose.

### Candidate C

- Correct: Keeps the Body-Block identity and full-body framing while giving the clearest lower-body pose among the four candidates. The image-left leg is visibly bent/lifted while the image-right leg is more weight-bearing, which better matches the pose source's readable stepping structure. Torso, shoulders, hips, knees, ankles, and feet remain mostly clean for joint recovery.
- Problems: The upper-body pose is still too neutral: both shoulders and arms hang closer to a relaxed stance than to the pose source's asymmetric arm/hand arrangement. The large blade-like prop is copied from the pose source and is not part of the character source; it may interfere with wrist/hand interpretation. The output is more realistic than the source render but does not fully role-swap.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5 / 4 / 3.5 / 4.5 / 2.5 / 4
- Acceptable: Marginal
- Reason: Still flawed, but it has the most usable target-pose structure for downstream 3D pose recovery, especially in the legs.

### Candidate D

- Correct: Best artifact control: full body is visible, joints are clean, no obvious extra limbs, and the character identity is preserved without importing the pose source's weapon. Viewpoint and centered framing are close to the pose source.
- Problems: Pose transfer is weak. The legs read mostly as a regular standing/walking stance rather than the pose source's clearer lifted/bent-leg structure. Arm asymmetry is also wrong: the image-right hand is raised/curled while the source has a simpler downward arm on that side. Because the pose is under-transferred, left/right limb correspondence is hard to verify.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 4 / 3 / 4.5 / 4.5 / 4.5
- Acceptable: Marginal
- Reason: Very clean for pose extraction, but less faithful to the requested target pose than Candidate C.

## Best Candidate

- Best candidate: Candidate C
- Reason: Candidate C is only relatively best. For downstream 3D pose recovery, it offers the clearest matching lower-body structure: one side is visibly lifted/bent while the other remains more weight-bearing, and the full body is centered with readable major joints. Candidate D has better artifact control and no weapon leakage, but its pose is closer to a neutral walk/stand and under-transfers the target leg structure. Candidate C's main drawback is the copied blade-like prop, which should be treated as non-character artifact and may need masking or filtering before pose recovery.
- Overall observation: All candidates preserve the character identity better than they preserve the exact pose. None fully reproduces the pose source's asymmetric arm arrangement, and several import the pose-source weapon despite the role instruction. The run is usable only as a rough pose candidate, with Candidate C preferred for pose geometry and Candidate D as the cleaner fallback if prop leakage is more damaging to the downstream estimator.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
