# Image Pose Retarget 实验记录表

当前项目采用统一素材库：

- `datasets/assets/<asset_id>/` 保存素材本身，包括 FBX、Blender 文件和渲染图。
- `experiments/<case_id>/case.yaml` 决定某个 asset 在本次实验里扮演 `character_input` 还是 `pose_reference`。
- `experiments/<case_id>/runs/<run_id>/` 保存一次网页模型提交的原始输出。
- 一次提交返回多张图时，保存到 `outputs/cand_*.png`。
- `docs/experiment-results.html` 用网页形式横向查看输入图、prompt、不同模型输出和备注。
- `records/` 只放过程记录和总结，不放实验输入图片。

## 填写规则

| 项 | 规则 |
|---|---|
| asset 何时新建 | 新下载一个 FBX、导入一个独立图片素材、或有一个需要单独管理的角色/姿态来源 |
| case 何时新建 | 改变 character_input、pose_reference、源视角、参考视角、输出视角策略、测试阶段时 |
| run 何时新建 | 改变 prompt、网页模型、上传顺序、输入预处理、后处理时 |
| candidate 何时新建 | 同一次网页提交返回多张候选图时 |
| 输入图如何记录 | 默认只在 `case.yaml` 引用 `datasets/assets/.../renders/...` 路径，不复制、不软连接 |
| 选择结果 | 不复制 selected 图，在 `docs/experiment-results.html` 的备注或分析中标记 |

## Asset 素材登记

| asset_id | asset_type | topology | source_file | blender_scene | render_groups | notes | ready |
|---|---|---|---|---|---|---|---|
| y_bot | fbx | biped humanoid | datasets/assets/y_bot/source/Y Bot.fbx | datasets/assets/y_bot/blender/Y-bot.blend | apose_front | Y Bot FBX copied into project | ready |
| Body-Block | fbx | block body | datasets/assets/Body-Block/source/Body Block.fbx |  | body_block_pose1, body_block_pose2 | Body Block FBX copied into project | ready |
| native_1 | glb | humanoid | datasets/assets/native_1/source/model.glb |  | native1_pose1 | Native 1 GLB copied into project | ready |
| A002 |  |  |  |  |  |  |  |

## Render 索引

| render_id | asset_id | render_path | pose_state | view | used_as | notes |
|---|---|---|---|---|---|---|
| R001 | y_bot | datasets/assets/y_bot/renders/Y-bot-Apose-front.png | apose | front | character_input or pose_reference | E001 r001/r002 character image |
| R002 | Body-Block | datasets/assets/Body-Block/renders/body-block-pose1.png | pose1 | front | character_input or pose_reference | E001 r001/r002 pose reference |
| R003 | Body-Block | datasets/assets/Body-Block/renders/body-block-pose2.png | pose2 | front | character_input or pose_reference | E002 r001 image 2; E003 r001 image 1 |
| R004 | native_1 | datasets/assets/native_1/renders/native1-pose1.png | pose1 | front | character_input or pose_reference | E002 r001 image 1; E003 r001 image 2 |
| R005 | Body-Block | datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png | pose2_no_skeleton | -Y | character_input or pose_reference | E002 r002/r003 image 2; E003 r002 image 1; E004 r001 image 1; E005 r001/r002 image 1 |
| R006 | native_1 | datasets/assets/native_1/renders/native1-noSkeleton-pose1.png | pose1_no_skeleton | front | pose_reference | E005 r003/r004 image 2 |
| R007 | Body-Block | datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png | rest_pose1_no_skeleton | -Y | character_input | E006 r001/r002 image 1 |

## Case 结果总表

| case_id | stage | character_asset | character_render | pose_asset | pose_render | output_view_policy | run_ids | selected_run | selected_candidate | pose_match | identity_keep | style_keep | artifact_level | failure_tags | notes |
|---|---|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|---|
| E001 | stage_0_sanity | y_bot | datasets/assets/y_bot/renders/Y-bot-Apose-front.png | Body-Block | datasets/assets/Body-Block/renders/body-block-pose1.png |  | r001, r002 |  |  |  |  |  |  |  | 使用 R001 + R002 |
| E002 | stage_1_pose_transfer | native_1 | datasets/assets/native_1/renders/native1-pose1.png | Body-Block | datasets/assets/Body-Block/renders/body-block-pose2.png | centered_uncropped_full_body | r001, r002, r003 |  |  |  |  |  |  |  | r002/r003 使用 run.yaml 中的输入图 |
| E003 | stage_1_pose_transfer | Body-Block | datasets/assets/Body-Block/renders/body-block-pose2.png | native_1 | datasets/assets/native_1/renders/native1-pose1.png | centered_uncropped_full_body | r001, r002 |  |  |  |  |  |  |  | r002 使用 run.yaml 中的输入图 |
| E004 | stage_1_pose_transfer | Body-Block | datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png | native_1 | datasets/assets/native_1/renders/native1-pose1.png | match_pose_reference_viewpoint_centered_uncropped_full_body | r001 |  |  |  |  |  |  |  | 更改描述，固定视角 |
| E005 | stage_1_pose_transfer | Body-Block | datasets/assets/Body-Block/renders/body-block-noSkeleton-pose2-(-Y).png | native_1 | datasets/assets/native_1/renders/native1-pose1.png | match_pose_reference_viewpoint_no_left_right_swap_centered_uncropped_full_body | r001, r002, r003, r004 |  |  |  |  |  |  |  | r003/r004 使用 no-skeleton reference pose |
| E006 | stage_1_pose_transfer | Body-Block | datasets/assets/Body-Block/renders/body-block-noSkeleton-rest-pose1-(-Y).png | native_1 | datasets/assets/native_1/renders/native1-noSkeleton-pose1.png | match_pose_reference_viewpoint_no_left_right_swap_centered_uncropped_full_body | r001, r002 |  |  |  |  |  |  |  | 输入角色改为 rest pose |

## Run 输出分组

| run_id | case_id | date | model/tool | upload_order | output_count | outputs_dir | notes |
|---|---|---|---|---|---:|---|---|
| r001 | E001 |  | gpt image2 | character_image, pose_reference | 4 | experiments/E001/runs/r001/outputs/ | 输出相对稳定，但是输出 1 缺失骨架 |
| r002 | E001 |  | nanobanana pro | character_image, pose_reference | 3 | experiments/E001/runs/r002/outputs/ | 输出相对稳定 |
| r001 | E002 | 2026-06-08 | nano banana pro | character_image, pose_reference | 3 | experiments/E002/runs/r001/outputs/ | 输出不同稳定，输出3 没有实现 pose retarget；输出 1 没有佩剑 |
| r002 | E002 | 2026-06-08 | nano banana pro | character_image, pose_reference | 3 | experiments/E002/runs/r002/outputs/ | 参考 pose 的骨架去掉之后稳定一些，但是在佩剑方式上有歧义，且输出 2 没有骨架，视角改变 |
| r003 | E002 | 2026-06-08 | nano banana pro | character_image, pose_reference | 3 | experiments/E002/runs/r003/outputs/ | 同 E002r002 |
| r001 | E003 | 2026-06-08 | GPT Image2 | character_image, pose_reference | 3 | experiments/E003/runs/r001/outputs/ | 骨架改变为ref pos的骨架形式，相对稳定，后脚的动作生成结果不稳定 |
| r002 | E003 | 2026-06-08 | nano banana pro | character_image, pose_reference | 4 | experiments/E003/runs/r002/outputs/ | 生成结果不稳定，输出 1、2 角色选择错误；输出 4 视角改变；输出 3 动作不对，左右腿反了 |
| r001 | E004 | 2026-06-08 | nano banana pro | character_image, pose_reference | 4 | experiments/E004/runs/r001/outputs/ | 更改描述，固定视角。输出 1 的下肢左右反了；输出 234 角色不对，输出 2、3 出现两个右肢，输出4 参考角色和参考 pose 反了 |
| r001 | E005 | 2026-06-08 | nano banana pro | character_image, pose_reference | 4 | experiments/E005/runs/r001/outputs/ | 更改了 prompt，强调角色和参考 pose，强调不要调换左右，强调摄像机视角和构图。输出 1 下肢左右反了；输出 2 视角改变；输出 3 剑的朝向不对，下肢左右反了；输出 4 还可以 |
| r002 | E005 | 2026-06-08 | GPT Image2 | character_image, pose_reference | 4 | experiments/E005/runs/r002/outputs/ | 测试 gpt image2。输出 1 动作不协调，输出 2 动作非常不协调，输出 1、2 都把 ref pose 的左手识别为了个棍子；输出 3 pose 也不太自然；输出 4 还是识别为了左手拿棍子 |
| r003 | E005 | 2026-06-08 | GPT Image2 | character_image, pose_reference | 4 | experiments/E005/runs/r003/outputs/ | 测试 ref pose 没有骨架。输出 1 差不多；输出 2 剑的方向不对，姿势有点怪；输出 3 姿势很怪；输出 4 还可以。 |
| r004 | E005 | 2026-06-08 | nano banana pro | character_image, pose_reference | 4 | experiments/E005/runs/r004/outputs/ | 测试 nanobanana。输出 1 剑的方向不对，下肢左右反了；输出 2视角不对；输出 3 视角不对，动作幅度有点大了；输出 4 ok |
| r001 | E006 | 2026-06-09 | nano banana pro | character_image, pose_reference | 4 | experiments/E006/runs/r001/outputs/ | 测试输入的参考角色是 rest pose。效果感觉好了不少，角色图本身的干扰减少了。输出 1、2、4 都还行（需不需要输出剑有歧义，输出与否都接受），输出 3 的视角改变且动作反了。 |
| r002 | E006 | 2026-06-09 | GPT Image2 | character_image, pose_reference | 4 | experiments/E006/runs/r002/outputs/ | 测试 gpt。角色扭曲的情况改善。输出 4 剑的朝向改变 pose 改变；输出 2 pose 稍显别扭一点；输出 1、3 都正常 |

## Candidate 评价

| case_id | run_id | candidate | output_path | pose_match | identity_keep | style_keep | artifact_level | selected | notes |
|---|---|---|---|---:|---:|---:|---:|---|---|
|  | r001 | cand_01 | outputs/cand_01.png |  |  |  |  |  |  |
|  | r001 | cand_02 | outputs/cand_02.png |  |  |  |  |  |  |

## Failure Tags

| tag | 含义 |
|---|---|
| pose_mismatch | 目标姿态没对上 |
| identity_drift | 角色身份改变 |
| style_drift | 画风、材质或颜色改变 |
| accessory_lost | 配件丢失 |
| accessory_deformed | 配件变形或漂移 |
| extra_limb | 多肢体 |
| missing_limb | 少肢体 |
| topology_confusion | 双足/四足结构混淆 |
| view_mismatch | 输出视角不符合设定 |
| left_right_flip | 左右翻转 |
| over_humanized | 非人类角色被人类化 |
| background_pollution | 背景污染或无关物体被保留 |
