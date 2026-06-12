# Blind Review: E008/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E008-r002-blind-review.md` and the images linked inside it.
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

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose6.png)

`datasets/assets/native_1/renders/native1-pose6.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E008/runs/r002/outputs/ai_generate_8214_1.png)

`experiments/E008/runs/r002/outputs/ai_generate_8214_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E008/runs/r002/outputs/ai_generate_8214_2.png)

`experiments/E008/runs/r002/outputs/ai_generate_8214_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E008/runs/r002/outputs/ai_generate_8214_3.png)

`experiments/E008/runs/r002/outputs/ai_generate_8214_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E008/runs/r002/outputs/ai_generate_8214_4.png)

`experiments/E008/runs/r002/outputs/ai_generate_8214_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the character source identity, clothing, color scheme, side-view camera, full-body framing, and a clear walking stride with one leg forward and one leg back. The sword is held by the rear/visible-side hand, which broadly matches the pose source role of the weapon arm.
- Problems: The sword angle drops too far downward compared with the more horizontal pose source, and the blade cuts across the leg area in a way that can confuse joint recovery. The free/front arm is present but a little generic and low, and the torso/hip relation is slightly over-arched.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 7 / 9 / 8 / 9 / 8 / 8
- Acceptable: Yes, relatively.
- Reason: The main body skeleton is readable and full-body, but the weapon vector is not faithful enough to be a clean pose cue.

### Candidate B

- Correct: Preserves the source character well and gives the clearest full-body side-profile walking structure: head, torso, hips, both legs, both feet, and both arms are visible enough for downstream pose recovery. The body faces the same direction as the pose source, with the sword carried by the rear hand and the free hand forward.
- Problems: The sword is still angled downward more than the pose source and partially overlaps the thigh region. The weapon styling is more realistic than the pose source, and the grip/guard relation is slightly imprecise.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 8 / 9 / 8 / 9 / 8 / 8
- Acceptable: Yes.
- Reason: It has the most usable whole-body joint structure: side view, readable stride, clear limb separation, and no major body deformation.

### Candidate C

- Correct: Preserves the character source identity and clothing, keeps a side-facing view, and makes the sword much closer to the horizontal direction in the pose source.
- Problems: The walking pose is less dynamic and less faithful than A/B: the legs read more like a mild step than the source's stronger stride, the free arm is compressed near the blade, and the sword/hand area occludes useful arm and hip cues. The body is slightly too upright and static for the pose source.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 7 / 9 / 8 / 9 / 8 / 8
- Acceptable: Yes, but not best.
- Reason: The weapon orientation is good, but the underlying skeleton is less clear for pose recovery than Candidate B.

### Candidate D

- Correct: Keeps the character source identity, full-body visibility, side-view framing, and a readable walking leg structure.
- Problems: The sword arm is substantially wrong: the weapon is raised diagonally forward instead of carried horizontally/backward as in the pose source. This changes the arm pose and produces a different action silhouette. The sword also looks more stylized/rough and no longer provides the intended pose cue.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 5 / 9 / 6 / 9 / 6 / 7
- Acceptable: No.
- Reason: For downstream 3D pose recovery, the incorrect weapon-arm configuration would likely encode the wrong upper-body pose.

## Best Candidate

- Best candidate: Candidate B
- Reason: Candidate B is the best for downstream 3D pose recovery because it gives the clearest full-body, side-profile walking skeleton with visible head, torso, hips, both legs, feet, and both arms. It preserves the source character and keeps the weapon in the correct general hand/side relationship, even though the sword angle is too downward.
- Overall observation: All candidates successfully keep the character identity and side-view framing. The main failure mode is imperfect transfer of the sword-bearing arm and weapon orientation; Candidate C has the best horizontal sword, but Candidate B has the most reliable overall joint structure and pose readability.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
