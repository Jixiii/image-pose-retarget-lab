# Image Retarget

这个仓库用于记录 image pose retarget 实验：素材放在统一素材库里，每个实验 case 决定输入角色图和参考姿态图，每次网页模型提交保存为一个 run。

## 快速入口

| 想做的事 | 文件或目录 |
|---|---|
| 填写下一次要记录的实验草稿 | [`experiments/_draft/current.md`](experiments/_draft/current.md) |
| 查看 Markdown 实验总表 | [`docs/experiment-settings.md`](docs/experiment-settings.md) |
| 查看带图片的实验结果网页 | [`docs/experiment-results.html`](docs/experiment-results.html) |
| 查看目录结构和组织规则网页 | [`docs/pose-retarget-structure.html`](docs/pose-retarget-structure.html) |
| 查看或修改某个 case 的输入角色和姿态来源 | `experiments/<case_id>/case.yaml` |
| 查看或修改某次 run 的 prompt、模型、输出数量和备注 | `experiments/<case_id>/runs/<run_id>/run.yaml` |
| 保存某次 run 的输出图 | `experiments/<case_id>/runs/<run_id>/outputs/` |
| 保存素材和渲染输入图 | `datasets/assets/<asset_id>/` |
| 保存过程记录和总结 | [`records/`](records/) |

## 日常记录流程

1. 在 [`experiments/_draft/current.md`](experiments/_draft/current.md) 填写 `target`、`metadata`、`inputs` 和 `prompt`。
2. 在当前对话里发送 `记录`。
3. 记录流程会创建或更新：
   - `experiments/<case_id>/case.yaml`
   - `experiments/<case_id>/runs/<run_id>/prompt.md`
   - `experiments/<case_id>/runs/<run_id>/run.yaml`
   - `experiments/<case_id>/runs/<run_id>/outputs/`
   - `docs/experiment-settings.md`
   - `docs/experiment-results.html`
4. 网页模型生成结果后，把输出图片放进对应的 `outputs/` 文件夹。
5. 再发送 `更新`，把 `outputs/` 里的结果图同步到记录页，并更新 `run.yaml` 里的 `output_count`。

## 记录规则

- 输入图默认只记录路径，不复制到 `experiments/` 目录。
- 素材不按角色拆成 character/pose。角色由每个 `case.yaml` 的 `character_input` 和 `pose_reference` 决定。
- 一个 `case` 表示一组角色输入、姿态参考、视角策略或测试阶段。
- 一个 `run` 表示一次网页模型提交；改 prompt、模型、上传顺序、输入预处理或后处理时，新建 run。
- 同一次提交返回的多张图都放在该 run 的 `outputs/` 目录下。
- `records/` 只放过程记录和总结，不放实验输入图或输出图。
- 如果同时存在 Markdown 和 HTML 记录页，更新实验记录时要同步维护 `docs/experiment-settings.md` 和 `docs/experiment-results.html`。

## 目录说明

```text
datasets/assets/
  <asset_id>/
    asset.yaml
    source/
    blender/
    renders/

experiments/
  _draft/current.md
  _template/case.yaml
  E001/
    case.yaml
    runs/
      r001/
        prompt.md
        run.yaml
        outputs/

docs/
  experiment-settings.md
  experiment-results.html
  pose-retarget-structure.html

records/
  README.md
```

## 命名约定

- `case_id` 使用 `E001`、`E002`、`E003` 这种格式。
- `run_id` 使用 `r001`、`r002`、`r003` 这种格式。
- 临时写成 `run2` 这类名字时，记录时应规范为 `r002`。
- 如果要补写旧实验，在草稿里明确填写 `target.case_id` 和 `target.run_id`，例如 `E001` / `r001`。

## 不放在这里的内容

- 不把外部原始来源路径长期写入素材元数据，除非这次实验明确需要。
- 不默认创建 selected 输出图副本。
- 不默认创建 `negative_prompt.md`。
- 不把实验图片放进 `records/`。
