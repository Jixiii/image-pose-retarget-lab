# codex-1 prompt design for E001 pose retarget

## User prompt

帮我想一个合适的 prompt 来做这个任务

## Context checked

- `prompts/templates/pose_retarget_base.md`
- `experiments/E001/case.yaml`
- `experiments/_template/case.yaml`
- `records/README.md`

## Tools used

- `sed` to read the existing prompt template and experiment configuration
- `rg --files` to inspect the workspace file layout
- `find` to pick the next `records/codex-*.md` filename

## Intermediate result

E001 is a pose-retargeting task:

- character input: `datasets/assets/y_bot/renders/Y-bot-Apose-front.png`
- pose reference: `datasets/assets/Body-Block/renders/body-block-pose1.png`

The existing base prompt already captures the core constraint: preserve image 1 character identity and transfer only image 2 pose. The useful improvement is to make the separation between appearance and pose more explicit, and to constrain the output framing.

## Suggested prompt

Use image 1 as the target character and image 2 only as the pose reference.

Preserve the character from image 1 exactly: same identity, robot body design, colors, materials, proportions, face/head shape, limbs, hands, feet, and overall style. Transfer only the full-body pose, joint angles, body orientation, and gesture from image 2.

Generate one clean full-body image of the image 1 character performing the image 2 pose. Keep the character centered, fully visible from head to feet, with no cropping. Do not copy the appearance, body shape, colors, clothing, texture, or identity from image 2. Do not create a hybrid character. Do not change the character design.

## Shorter variant

Keep the exact character from image 1. Use image 2 only as a pose reference. Transfer the full-body pose from image 2 onto the image 1 character while preserving image 1's identity, design, proportions, colors, and materials. Output one centered, uncropped, full-body image. Do not copy the image 2 character or create a hybrid.
