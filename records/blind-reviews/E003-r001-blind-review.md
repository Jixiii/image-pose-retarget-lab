# Blind Review: E003/r001

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E003-r001-blind-review.md` and the images linked inside it.
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

![Input 1: Character Source](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-pose2.png)

`datasets/assets/Body-Block/renders/body-block-pose2.png`

### Input 2: Pose Source 1

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose1.png)

`datasets/assets/native_1/renders/native1-pose1.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E003/runs/r001/outputs/image_0.png)

`experiments/E003/runs/r001/outputs/image_0.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E003/runs/r001/outputs/image_1.png)

`experiments/E003/runs/r001/outputs/image_1.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E003/runs/r001/outputs/image_2.png)

`experiments/E003/runs/r001/outputs/image_2.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the main character identity well: orange sweatshirt, denim shorts, yellow shoes, human proportions, and frontal framing. The sword/held-object arm is on the same image side as the pose source, the opposite arm hangs down, and the whole body is visible.
- Problems: The pose is softened into a generic walking/standing pose. The shoulder, elbow, wrist, hip, knee, and ankle landmarks are not visually explicit, which reduces usefulness for downstream 3D pose recovery. The lower-body step is only approximate and the knee/foot relationship is less clear than in the pose source. The pose-source sword/object is copied into the character even though it is not part of the character source.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 4 / 4 / 5 / 3 / 4
- Acceptable: Marginal.
- Reason: Visually clean and full-body, but the usable joint structure is weak for pose recovery because the limbs are smoothed and the target pose is only broadly approximated.

### Candidate B

- Correct: Keeps the character clothing and body identity while adopting the pose-source structure more directly. The body is frontal and full-body visible. Major joint markers are present on the shoulders, elbows, wrists, torso, hips, knees, ankles, and feet, making the pose easier to recover. The held-object arm and hanging arm are on the expected image sides.
- Problems: Large copied pose-source markers and the pelvis/origin object obscure the hip and crotch area. The feet and ankle area are partly cluttered by the origin/gizmo. The torso and shoulders are wider and more rigid than the pose source, and the legs are somewhat straightened, so the weight-bearing relationship is not fully faithful.
- Failure tags: `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 4 / 4 / 3 / 3
- Acceptable: Yes, with artifact caveats.
- Reason: The copied joint markers are visually intrusive, but for downstream 3D pose recovery they make the skeleton much more legible than Candidate A.

### Candidate C

- Correct: Best balance of character preservation and recoverable pose structure. The figure is frontal, centered, and full-body visible. Joint markers are clear across the upper body, torso, hips, knees, ankles, and feet. The held-object arm remains on the pose-source side, the opposite arm hangs down, and the stepping leg structure is more readable than in Candidate B.
- Problems: The large pelvis/origin marker still occludes the hip region, and the copied joint-marker overlay is not part of the clean character identity. The held object is simplified into a tube-like prop, and the lower legs remain slightly stylized rather than exactly matching the blocky pose source.
- Failure tags: `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 4 / 4 / 3 / 4
- Acceptable: Yes.
- Reason: It has the clearest recoverable full-body joint layout among the candidates while keeping left/right arrangement and body visibility usable.

## Best Candidate

- Best candidate: Candidate C.
- Reason: Candidate C is the most useful for downstream 3D pose recovery: full body is visible, the frontal viewpoint is stable, left/right arm roles are preserved, and the joint-marker layout gives the clearest shoulder-to-foot structure. Candidate B is close, but its lower-body and hip area are more cluttered and slightly less readable. Candidate A is cleaner aesthetically but weaker for pose recovery because the skeleton and target pose landmarks are less explicit.
- Overall observation: All candidates preserve the character source better than the pose-source identity, but they also copy the pose-source held object and/or marker artifacts. Under the stated priority, the marker-heavy candidates are more useful than the clean image because the task favors pose recoverability over aesthetics.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
