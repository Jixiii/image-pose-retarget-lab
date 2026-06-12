# Blind Review: E010/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E010-r002-blind-review.md` and the images linked inside it.
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

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r002/outputs/ai_generate_8335_1.png)

`experiments/E010/runs/r002/outputs/ai_generate_8335_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r002/outputs/ai_generate_8335_2.png)

`experiments/E010/runs/r002/outputs/ai_generate_8335_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r002/outputs/ai_generate_8335_3.png)

`experiments/E010/runs/r002/outputs/ai_generate_8335_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r002/outputs/ai_generate_8335_4.png)

`experiments/E010/runs/r002/outputs/ai_generate_8335_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the Body-Block character identity, front-facing camera, full-body framing, outfit colors, cat logo, shorts, shoes, and a readable humanoid structure. The active arm is on the same image-left side as the pose source's more active weapon arm, while the other arm hangs down.
- Problems: The pose is only a rough approximation. The image-left arm is pushed straight forward instead of bent across/down with the hand-held blade shape; the legs remain nearly symmetric and do not reproduce the crossed/stepping weight shift. The pose-source hand objects are not represented, and the stance is much closer to a simple front pose than the source pose.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2 / 4 / 3 / 5 / 5 / 4
- Acceptable: Borderline for coarse 3D pose recovery only; not acceptable as an accurate retarget.
- Reason: Full-body visibility and clean joints are useful, but the target limb arrangement is too simplified.

### Candidate B

- Correct: Preserves the Body-Block character from the back, with the clothing, hair, shorts, shoes, and full body visible. Anatomy is mostly clean.
- Problems: This is essentially a back-view T-pose/rest-pose result, not the front-facing pose source. Both arms are outstretched horizontally, the head and torso face away, the legs do not match the crossed/weight-bearing pose, and left/right correspondence to the front-facing source is unusable.
- Failure tags: `pose_mismatch`, `view_mismatch`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 0 / 0 / 0 / 5 / 5 / 4
- Acceptable: No.
- Reason: The output is clean but recovers the wrong view and wrong pose, making it unsuitable for downstream 3D pose recovery.

### Candidate C

- Correct: Keeps the Body-Block identity, front-facing view, full-body framing, clothing, cat logo, shoes, and a readable head-torso-limb layout. Like the pose source, one image-left arm is active/forward while the opposite arm hangs lower, and the lower body has a slight asymmetry rather than a pure T-pose stance.
- Problems: The target pose is still simplified. The image-left arm is straightened forward instead of bent with the blade-hand structure, the opposite hand hangs in a generic way, and the legs do not clearly reproduce the crossed step or exact weight-bearing relationship. The body proportions are usable but not tightly matched to the pose source.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 2.5 / 4 / 3 / 5 / 5 / 4
- Acceptable: Borderline for coarse 3D pose recovery only; not acceptable as an accurate retarget.
- Reason: It has the clearest relatively relevant full-body structure among the front-facing attempts, but the actual pose is still far from the source.

### Candidate D

- Correct: Preserves the Body-Block character identity, front view, clothing, cat logo, full-body visibility, and clean limb geometry.
- Problems: The result stays in a front-facing T-pose/rest-pose configuration. Both arms are extended sideways, the legs are symmetric, and none of the source pose's arm-down/arm-crossed/stepping structure is transferred.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 0.5 / 4 / 2 / 5 / 5 / 4
- Acceptable: No.
- Reason: Although visually clean, it does not provide the requested target pose for pose recovery.

## Best Candidate

- Best candidate: Candidate C.
- Reason: Candidate C is only relatively best. It keeps the correct character, full-body front view, and clean joint visibility while making at least a partial attempt at the pose-source structure with one active image-left arm and one lowered opposite arm. Candidate A is close, but its stance reads even more like a generic front pose. Candidates B and D are effectively source rest-pose/T-pose outputs.
- Overall observation: All candidates fail the target pose at the level needed for accurate downstream 3D pose recovery. The main failure is pose under-transfer: the generation preserves the Body-Block identity well, but largely ignores the source pose's bent weapon arm, lowered opposite arm, crossed/stepping legs, and weight-bearing structure.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
