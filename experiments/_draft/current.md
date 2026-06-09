# Current Experiment Draft

这个文件是临时草稿。你在这里填写下一次要记录的信息；之后在当前对话里发“记录”或“更新”，我按下面的工作流快速执行，除非你纠正流程。

## Draft

```yaml
target:
  case_id: E008
  run_id: r001

metadata:
  date: 
  # model_tool:nano banana pro
  model_tool:GPT Image2
  notes: 

inputs:
  image_1:
    role: character_input
    path: /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png
  image_2:
    role: pose_reference
    path: /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose6.png
prompt: |
  Image 1 = CHARACTER SOURCE. Image 2 = POSE SOURCE. Do not swap these roles.

  Generate one centered, uncropped, full-body image of the exact character from image 1 performing the pose from image 2.

  Preserve image 1's identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use image 2's character identity, face, outfit, colors, materials, or style.

  Use image 2 only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match image 2's viewing angle and body facing direction.

  Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from image 2: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in image 2.

  Image 1 always controls appearance. Image 2 only controls pose and viewpoint. Do not create a hybrid.
```

```yaml
target:
  case_id: E007
  run_id: r002

metadata:
  date: 
  model_tool:nano banana pro
  # model_tool:GPT Image2
  notes: 

inputs:
  image_1:
    role: character_input
    path: /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png
  image_2:
    role: pose_reference
    path: /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-pose6.png
prompt: |
  Image 1 = CHARACTER SOURCE. Image 2 = POSE SOURCE. Do not swap these roles.

  Generate one centered, uncropped, full-body image of the exact character from image 1 performing the pose from image 2.

  Preserve image 1's identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use image 2's character identity, face, outfit, colors, materials, or style.

  Use image 2 only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match image 2's viewing angle and body facing direction.

  Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from image 2: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in image 2.

  Image 1 always controls appearance. Image 2 only controls pose and viewpoint. Do not create a hybrid.
```



## Workflow

### 当你发“记录”

1. 读取上面的 `Draft`。
2. 如果 `target.case_id` 是 `auto` 或空值，创建下一个 `experiments/E###/runs/r001/outputs/`。
3. 如果 `target.case_id` 和 `target.run_id` 写了具体值，例如 `E001` / `r001`，则更新这条已有记录；若文件夹缺失则创建。
4. 写入或更新：
   - `experiments/<case_id>/case.yaml`
   - `experiments/<case_id>/runs/<run_id>/prompt.md`
   - `experiments/<case_id>/runs/<run_id>/run.yaml`
   - `docs/experiment-settings.md`
   - `docs/experiment-results.html`
5. 创建 `experiments/<case_id>/runs/<run_id>/outputs/`，等待你传入结果图。
6. 输入图只记录路径，不复制到 experiment 目录。

### 当你发“更新”

1. 先读取 `target.case_id` 和 `target.run_id`。
2. 扫描 `experiments/<case_id>/runs/<run_id>/outputs/`，把里面已有结果图补写到记录页，并更新 `run.yaml` 的 `output_count`。
3. 如果草稿里还填写了新的输入图和 prompt，再按“记录”流程创建或更新本次记录。
4. 如果 `outputs.images` 明确列了文件，以列表为准；否则按 outputs 文件夹扫描。

## Fast Defaults

- 默认不复制输入图，只引用 `datasets/assets/.../renders/...` 或你填写的路径。
- 默认不创建 `negative_prompt.md`。
- 默认不创建 selected 拷贝图。
- 默认输出图在 `experiments/<case_id>/runs/<run_id>/outputs/`。
- 默认每次记录只关心：输入 image、prompt、输出 image、路径、model/tool、备注。
- 如果你指定 `E001 r001`，就修改或补全 `E001/r001`，不是新建实验。
