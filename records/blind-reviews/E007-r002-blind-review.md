# Blind Review: E007/r002

## Metadata

- Created: 2026-06-10 21:42:31
- Source used for image collection: `docs/experiment-results.html`
- Model/tool from record: `nano banana pro`
- Human notes: intentionally not copied into this blind-review draft.

## Start Isolated Review

Copy this prompt into a fresh Codex conversation for this run only:

```text
Use the project-local skill at `skills/image-retarget-blind-review`.
Review only `records/blind-reviews/E007-r002-blind-review.md` and the images linked inside it.
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

![Input 2: Pose Source 1](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png)

`datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png`

## Candidate Outputs

### Candidate A

![Candidate A](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E007/runs/r002/outputs/ai_generate_8133_1.png)

`experiments/E007/runs/r002/outputs/ai_generate_8133_1.png`

### Candidate B

![Candidate B](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E007/runs/r002/outputs/ai_generate_8133_2.png)

`experiments/E007/runs/r002/outputs/ai_generate_8133_2.png`

### Candidate C

![Candidate C](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E007/runs/r002/outputs/ai_generate_8133_3.png)

`experiments/E007/runs/r002/outputs/ai_generate_8133_3.png`

### Candidate D

![Candidate D](/Users/daiminyue/Desktop/study/research/investigate/image-retarget/experiments/E007/runs/r002/outputs/ai_generate_8133_4.png)

`experiments/E007/runs/r002/outputs/ai_generate_8133_4.png`

## Blind Analysis

Failure tags to reuse: `pose_mismatch`, `identity_drift`, `style_drift`, `accessory_lost`, `accessory_deformed`, `extra_limb`, `missing_limb`, `view_mismatch`, `left_right_flip`, `body_deformation`, `role_swap`, `framing_error`.

### Candidate A

- Correct: Keeps the native_1 character identity, outfit colors, boots, hair, and full-body framing. The body is crouched with both knees bent, and the two forward hands roughly echo the guarded hand position in the pose source.
- Problems: The sword/hand structure on the viewer-right side creates an extra visible limb-like cue behind the torso, which is bad for skeleton recovery. The hand positions are more separated and claw-like than the pose source, and the torso/head orientation is only approximate. The accessory appears shifted to the wrong side relative to the source character and adds confusing occlusion near the arm and hip.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `extra_limb`, `left_right_flip`, `body_deformation`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3.5 / 3 / 2.5 / 4 / 2 / 2.5
- Acceptable: Marginal
- Reason: The full-body crouch is recoverable, but the extra hand/sword structure can easily be interpreted as an additional or swapped limb.

### Candidate B

- Correct: Full body is visible, the character identity and clothing are preserved, and the lower body keeps a bent-knee stance close to the reference pose.
- Problems: One arm is pulled down and outward to hold the sword instead of matching the pose source's two forward hands. The hands are blocky and less useful as joint cues, and the sword arm dominates the viewer-left side, reducing pose clarity. The torso is more side-turned than the pose source, and the arm correspondence is unclear.
- Failure tags: `pose_mismatch`, `view_mismatch`, `accessory_deformed`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 3 / 3 / 4 / 3 / 3
- Acceptable: No
- Reason: The legs are usable, but the upper-body pose does not preserve the two-hand guarded structure needed for reliable 3D pose recovery.

### Candidate C

- Correct: Preserves the character identity and full-body visibility while keeping a clear crouched stance. Both legs remain separated and readable, both hands are near the front of the torso, and the overall guarded pose is the closest match among the candidates. The main body joints are visible enough for downstream pose recovery.
- Problems: The sword is retained and crosses the front-left side, so one wrist/hand cue is partly contaminated by the accessory. The pose is still more upright and simplified than the source, with less precise shoulder/elbow placement and only approximate body-facing direction.
- Failure tags: `pose_mismatch`, `accessory_deformed`, `view_mismatch`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 4 / 3.5 / 3.5 / 4.5 / 3 / 4
- Acceptable: Yes, relatively
- Reason: It has the clearest full-body joint structure and the least severe limb ambiguity, even though the sword remains a source of local occlusion.

### Candidate D

- Correct: Keeps the native_1 identity, shows the full body, and maintains a crouched lower-body posture with both legs visible.
- Problems: The sword-side arm is lowered and extended instead of matching the pose source's forward two-hand arrangement. The upper body is more side-facing, the hands are less anatomically informative, and the sword creates another strong non-body segment near the arm. The lower body is readable, but the upper-limb structure is not close enough to the reference.
- Failure tags: `pose_mismatch`, `view_mismatch`, `accessory_deformed`, `left_right_flip`
- Scores: pose_match / view_match / left_right_correctness / identity_keep / accessory_keep / artifact_quality = 3 / 3 / 3 / 4 / 3 / 3.5
- Acceptable: No
- Reason: It is visually coherent, but the arm pose is too far from the reference for a recovery-first selection.

## Best Candidate

- Best candidate: Candidate C
- Reason: Candidate C is the best recovery-oriented choice because it keeps the full body visible, preserves a readable crouched stance, and leaves the main limb joints more interpretable than the other candidates. Its sword still interferes with one hand/wrist region, but it avoids Candidate A's extra limb-like sword-hand artifact and keeps both hands closer to the pose source's guarded front position than B or D.
- Overall observation: All candidates preserve the character identity better than they preserve exact pose anatomy. For downstream 3D pose recovery, the main failure mode is accessory-driven arm ambiguity: the sword either becomes an extra limb cue or pulls one arm away from the reference pose. Candidate C is only relatively best, not a clean pose-transfer result.

## Post-Review Comparison

After completing the blind review, compare against the existing human notes if needed. Keep that comparison separate from the blind analysis above.
