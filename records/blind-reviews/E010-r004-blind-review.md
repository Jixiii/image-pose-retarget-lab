# Blind Review: E010/r004

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `GPT Image2`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E010-r004-blind-review.md` and the images linked inside it.
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

![Input 4: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose6.png)

`datasets/assets/native_1/renders/native1-pose6.png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r004/outputs/ai_generate_8337_1.png)

`experiments/E010/runs/r004/outputs/ai_generate_8337_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r004/outputs/ai_generate_8337_2.png)

`experiments/E010/runs/r004/outputs/ai_generate_8337_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r004/outputs/ai_generate_8337_3.png)

`experiments/E010/runs/r004/outputs/ai_generate_8337_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E010/runs/r004/outputs/ai_generate_8337_4.png)

`experiments/E010/runs/r004/outputs/ai_generate_8337_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Preserves the character-source identity, hairstyle, orange sweatshirt, shorts, and shoes. The body is full-frame and facing right in a side walking stance, with a clear forward/back leg separation close to the pose source.
- Problems: The sword is copied from the pose source, which is a role-separation error because it is not part of the character source. The front/free arm drops naturally but does not match the compact arm structure of the pose source. The stride is more human-realistic and elongated than the source pose, and the torso is slightly more three-quarter than the pose source.
- Failure tags: `pose_mismatch`, `style_drift`, `accessory_deformed`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 4 / 4 / 2 / 4
- Acceptable: Marginal.
- Reason: Good full-body walking silhouette for pose recovery, but the added sword and arm mismatch make the joint structure less clean than the best output.

### Candidate B

- Correct: Keeps the character-source appearance and a right-facing side-view walk. Both legs and feet are visible, and the sword-bearing arm gives a readable horizontal arm line similar to the pose source.
- Problems: The sword is again incorrectly imported from the pose source. The opposite arm is partly hidden and not very useful for joint recovery. The body is slightly tight against the lower frame, and the hip/thigh area is partly occluded by the sword, reducing clarity.
- Failure tags: `style_drift`, `accessory_deformed`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 4 / 4 / 4 / 2 / 4
- Acceptable: Marginal.
- Reason: The pose is readable, but the lower-body and arm occlusions make it weaker than Candidate D for downstream skeleton recovery.

### Candidate C

- Correct: Preserves the character-source identity and keeps the right-facing side orientation. The walking direction and approximate forward/back leg relation match the pose source.
- Problems: The sword is copied from the pose source. The rear/occluded leg is less cleanly separated from the front leg, and the pelvis/shorts region looks compressed by the sword and stride. The visible arm structure is not as close to the source pose, so the shoulders, elbows, and hands are less reliable for pose recovery.
- Failure tags: `pose_mismatch`, `style_drift`, `accessory_deformed`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 4 / 4 / 4 / 2 / 3
- Acceptable: No.
- Reason: Full body is present, but limb separation and hip/arm readability are weaker than the other candidates.

### Candidate D

- Correct: Best preserves the right-facing side-view walking pose with a clear full-body silhouette. Both legs and feet are visible with strong forward/back separation, the body is centered and uncropped, and the limb proportions are mostly coherent for 3D pose recovery. Character-source identity, hair, sweatshirt, shorts, and shoes are retained.
- Problems: The sword is copied from the pose source and should not be present for strict appearance preservation. The non-sword arm is mostly hidden/occluded, so one upper-limb chain is less recoverable. The torso is more realistic-human than the low-poly pose source, but that is acceptable for using the pose only as pose/reference.
- Failure tags: `style_drift`, `accessory_deformed`, `pose_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 5 / 4 / 4 / 4 / 2 / 5
- Acceptable: Yes, with the sword-leakage caveat.
- Reason: It has the clearest full-body, side-view joint structure and the lowest deformation among the four candidates.

## Best Candidate

- Best candidate: Candidate D.
- Reason: Candidate D is the most useful for downstream 3D pose recovery: it has the cleanest full-body side-view silhouette, the clearest leg separation, good foot visibility, stable body proportions, and no obvious mirror flip in the visible walking direction. Its main flaw is the copied sword accessory from the pose source, but the body joints are more recoverable than in A, B, or C.
- Overall observation: All candidates preserve the character-source person reasonably well but fail strict role separation by importing the pose source sword. For this run, the candidates are better as pose-recovery references than as clean appearance-only retargets; D is relatively best because its joint structure is the least ambiguous.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
