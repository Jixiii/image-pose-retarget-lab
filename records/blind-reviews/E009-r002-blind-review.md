# Blind Review: E009/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E009-r002-blind-review.md` and the images linked inside it.
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

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r002/outputs/ai_generate_8268_1.png)

`experiments/E009/runs/r002/outputs/ai_generate_8268_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r002/outputs/ai_generate_8268_2.png)

`experiments/E009/runs/r002/outputs/ai_generate_8268_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r002/outputs/ai_generate_8268_3.png)

`experiments/E009/runs/r002/outputs/ai_generate_8268_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E009/runs/r002/outputs/ai_generate_8268_4.png)

`experiments/E009/runs/r002/outputs/ai_generate_8268_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the low-poly character identity, outfit colors, boots, hair, and sword. The output is full-body, side/profile oriented, and keeps the broad pose structure: forward lean, both arms lifted in front, rear leg trailing to image-left, and bent support/front leg to image-right.
- Problems: The pose is less crouched and less anatomically close to the pose source than ideal. The sword forces the nearer hand into a guarded grip instead of the open curved hand shape, and the trailing boot/ankle is visibly deformed, which weakens downstream foot/joint recovery. The torso silhouette is also bulkier and less clearly aligned to the pose source.
- Failure tags: `pose_mismatch`, `body_deformation`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 4 / 5 / 4 / 3
- Acceptable: Yes, relatively.
- Reason: It gives a readable full-body side pose with mostly correct limb placement, but the rear foot deformation and sword-driven hand pose make it imperfect for 3D recovery.

### Candidate B

- Correct: Keeps the source character identity, palette, outfit, boots, and sword. The view direction is broadly correct, with the character facing image-right and all major limbs visible.
- Problems: The body is too upright and compact compared with the pose source. The front hand becomes a blocky fist rather than an open reaching hand, the sword-side hand/forearm compresses the arm structure, and the lower-body stance is less clear because the trailing foot and ankle are distorted. The pose reads as a generic guarded stance more than the exact crouched reference.
- Failure tags: `pose_mismatch`, `body_deformation`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 4 / 4 / 5 / 4 / 3
- Acceptable: Marginal.
- Reason: Full-body visibility is usable, but pose clarity is weaker than A and D, especially around the arms, hands, and rear foot.

### Candidate C

- Correct: Preserves the character source well and keeps a side-facing, full-body composition. The open forward hand and lifted arms are closer to the pose-source hand attitude than most other candidates.
- Problems: The sword appears awkwardly attached or dangling under the raised hand, creating confusing hand/accessory geometry. The lower body is less reliable for 3D recovery: the rear leg is partly hidden by the tunic silhouette, the stance is more vertical than the pose source, and the support/front leg relationship is less clean. The torso does not lean forward enough.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5 / 4 / 4 / 5 / 3 / 3
- Acceptable: Marginal.
- Reason: The arm gesture has some useful pose-source resemblance, but the accessory/hand confusion and weaker leg readability reduce its value for downstream pose estimation.

### Candidate D

- Correct: Strongly preserves the source character, outfit, hair, boots, and sword. The full body is visible, the side/profile view matches the pose source well, and the main skeleton is readable: torso leans forward, arms are raised in front, the rear leg trails to image-left, and the front/support leg bends to image-right.
- Problems: The hands are not faithful to the pose source; the forward hand becomes a curled fist/claw and the sword-side arm is raised higher and more vertical than the reference. The sword partially occludes the face/upper arm area, and the pose is still a stylized guarded stance rather than an exact transfer.
- Failure tags: `pose_mismatch`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4.5 / 4 / 5 / 4 / 3.5
- Acceptable: Yes, relatively.
- Reason: It has the clearest full-body side-view joint structure among the candidates, with fewer severe limb or foot deformations than the alternatives.

## Best Candidate

- Best candidate: Candidate D
- Reason: Candidate D is the strongest choice for downstream 3D pose recovery because it preserves full-body visibility, side-view orientation, readable arm and leg segmentation, and the reference's main weight-bearing structure better than the other candidates. Candidate A is close, but its trailing foot/ankle deformation is more damaging for recovery. Candidate C has better open-hand resemblance, but its hand/sword geometry and lower-body readability are weaker. Candidate B is the least precise pose match.
- Overall observation: All four outputs keep the character source identity and avoid obvious role swap, but all simplify the pose source into a low-poly guarded stance and fail to reproduce the open, curved hand shapes exactly. For a 3D pipeline, Candidate D is only relatively best rather than fully correct.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
