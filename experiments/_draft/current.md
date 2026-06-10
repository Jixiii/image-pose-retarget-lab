# Current Experiment Draft

这个文件是临时草稿。你在这里填写下一次要记录的信息；之后在当前对话里发“记录”或“更新”，我按下面的工作流快速执行，除非你纠正流程。

## Draft

```yaml
target:
  case_id: E012
  run_id: r001

metadata:
  date: 
  model_tool:nano banana pro
  # model_tool:GPT Image2
  notes: 输出 2、4 视角不对，输出 1，3 还行。

inputs:
  image_1:
    role: character_input
    path: 
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-X).png
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-Y.png
  image_2:
    role: pose_reference
    path: 
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-X.png
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11--Y.png
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-Y.png
prompt: |
  Images 1-3 = CHARACTER SOURCES. Images 4-6 = POSE SOURCES. Do not swap these roles.

  Use Images 1-3 as references for the same character. Image 1 is the primary character source; the other character images provide additional appearance details and views.

  Use Images 4-6 as references for the same pose. Image 4 is the primary pose source and controls the final camera viewpoint, body facing direction, and framing.

  Generate one centered, uncropped, full-body image of the exact character from the character sources performing the pose from the pose sources.

  Preserve the character sources' identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use the pose sources' character identity, face, outfit, colors, materials, or style.

  Use the pose sources only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match image 4's viewing angle and body facing direction.

  Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from the pose sources: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in the pose sources.

  The character sources always control appearance. The pose sources only control pose and viewpoint. Do not create a hybrid.
```


```yaml
target:
  case_id: E012
  run_id: r002

metadata:
  date: 
  # model_tool:nano banana pro
  model_tool:GPT Image2
  notes: 输出视角都不对，输出 4 是左手拿剑；输出 1、2 下肢左右反了。

inputs:
  image_1:
    role: character_input
    path: 
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-X).png
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-Y.png
  image_2:
    role: pose_reference
    path: 
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-X.png
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11--Y.png
      /Users/daiminyue/Desktop/study/research/investigate/image-retarget/datasets/assets/native_1/renders/native1-frame11-Y.png
prompt: |
  Images 1-3 = CHARACTER SOURCES. Images 4-6 = POSE SOURCES. Do not swap these roles.

  Use Images 1-3 as references for the same character. Image 1 is the primary character source; the other character images provide additional appearance details and views.

  Use Images 4-6 as references for the same pose. Image 4 is the primary pose source and controls the final camera viewpoint, body facing direction, and framing.

  Generate one centered, uncropped, full-body image of the exact character from the character sources performing the pose from the pose sources.

  Preserve the character sources' identity, face, hairstyle, body proportions, outfit, colors, materials, accessories, and design details. Do not use the pose sources' character identity, face, outfit, colors, materials, or style.

  Use the pose sources only for the full-body pose, anatomical limb arrangement, body orientation, camera viewpoint, and framing. Match image 4's viewing angle and body facing direction.

  Do not mirror, flip, or left-right swap the pose. Preserve the exact limb correspondence from the pose sources: left arm to left arm, right arm to right arm, left leg to left leg, right leg to right leg. Keep which limb is forward, behind, raised, lowered, bent, straight, crossed, or weight-bearing exactly as shown in the pose sources.

  The character sources always control appearance. The pose sources only control pose and viewpoint. Do not create a hybrid.
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
