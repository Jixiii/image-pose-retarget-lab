# Blind Review: E001/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `gpt image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E001-r001-blind-review.md` and the images linked inside it.
Do not read docs/experiment-results.html notes, run.yaml notes, or any previous blind reviews.
Fill only the Blind Analysis and Best Candidate sections.
Selection priority is downstream 3D pose recovery: pose clarity, full-body visibility, left/right correctness, low deformation, and usable joint structure matter more than aesthetics.
```

## Task

Use the input images and generation prompt below to judge each output candidate. Do not consult existing run notes while filling this file.

### Generation Prompt

```text
生成第一张图的角色做第二张图角色的动作的图片。
```

### Input Role Assumption

- Input 1 is treated as the character source unless the visible record clearly says otherwise.
- Remaining input images are treated as pose/reference sources unless the visible record clearly says otherwise.

## Inputs

### Input 1: Character Source

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/y_bot/renders/Y-bot-Apose-front.png)

`datasets/assets/y_bot/renders/Y-bot-Apose-front.png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-pose1.png)

`datasets/assets/Body-Block/renders/body-block-pose1.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E001/runs/r001/outputs/image_0.png)

`experiments/E001/runs/r001/outputs/image_0.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E001/runs/r001/outputs/image_1.png)

`experiments/E001/runs/r001/outputs/image_1.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E001/runs/r001/outputs/image_2.png)

`experiments/E001/runs/r001/outputs/image_2.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E001/runs/r001/outputs/image_3.png)

`experiments/E001/runs/r001/outputs/image_3.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the Y-bot identity cleanly, shows the whole body, and gives a readable crouched guard stance. The image-left foot is turned outward and the image-right foot stays more front-facing, which is consistent with the main stance asymmetry in the pose source. Limbs are mostly unobscured, so the body silhouette is easy to recover.
- Problems: The raised hands are lower and wider than the pose source, and the torso/head are too upright and simplified compared with the slightly tucked guarded pose. The robot joint structure is visible through body segmentation, but there are fewer explicit rig/joint cues than in the pose source.
- Failure tags: `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 4/5 / 4/5 / 5/5 / N/A / 4.5/5
- Acceptable: Yes, especially if a clean silhouette matters more than exact hand placement.
- Reason: This is the cleanest output with low deformation, but it only approximates the upper-body guard pose.

### Candidate B

- Correct: Full body is visible, the Y-bot identity is mostly preserved, both hands are raised near the face/chest, and the bent-knee stance broadly matches the pose source. The visible rig markers make many joint locations easy to locate.
- Problems: The copied armature/guide geometry crosses the face, torso, hands, and limbs, creating visual clutter for downstream recovery. The image-left foot is stretched and flattened, and the hands/fingers are crowded by extra grey structures. The upper-body guard is close but still too stiff and symmetric.
- Failure tags: `pose_mismatch`, `body_deformation`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 4/5 / 4/5 / 4.5/5 / N/A / 3/5
- Acceptable: Borderline.
- Reason: Pose and joints are readable, but the overlaid guide geometry and foot/hand distortions reduce clean recoverability.

### Candidate C

- Correct: Preserves the character identity and keeps the complete body in frame. The crouched lower-body stance and raised hands are recognizable, with no obvious full left/right reversal.
- Problems: The hands and central armature are the most cluttered of the set, with grey guide parts crossing the face, neck, chest, wrists, and fingers. The image-left foot/ankle area is elongated and messy, and the torso/shoulder line is harder to parse than in A, B, or D.
- Failure tags: `pose_mismatch`, `body_deformation`, `style_drift`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5/5 / 4/5 / 4/5 / 4.5/5 / N/A / 2.5/5
- Acceptable: Borderline to no.
- Reason: The pose is present, but joint recovery would be made harder by the heavy occlusion around the hands, head, and torso.

### Candidate D

- Correct: Best matches the guarded pose structure overall: hands are high near the face, knees are bent, the image-left foot is turned outward, and the image-right foot remains more planted/front-facing. The full body is visible, the Y-bot identity is retained, and the visible rig/joint markers make the limb chain relatively easy to infer.
- Problems: The central guide/armature still crosses the face and torso, and the hands are partially occluded by grey guide parts. The pose is a little too front-facing and stiff compared with the source, and the feet retain minor deformation.
- Failure tags: `body_deformation`, `style_drift`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4/5 / 4/5 / 4/5 / 4.5/5 / N/A / 3.5/5
- Acceptable: Yes, relatively.
- Reason: Despite visual clutter, it provides the strongest combination of pose match, full-body visibility, left/right consistency, and recoverable joint structure.

## Best Candidate

- Best candidate: Candidate D
- Reason: Candidate D is not the cleanest image, but it is the best choice for downstream 3D pose recovery. Compared with A, it keeps the hands closer to the face and the knees/feet closer to the pose source. Compared with B and C, its body structure is slightly easier to parse and less disrupted by local deformation.
- Overall observation: All candidates preserve the Y-bot identity and full-body framing. Candidate A has the cleanest silhouette, while B-D preserve more explicit joint/rig cues. Under the stated priority, D is the strongest relative candidate because pose clarity and joint recoverability outweigh the remaining armature clutter.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
