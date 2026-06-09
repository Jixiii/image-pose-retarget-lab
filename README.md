# Image Retarget

这个仓库用于记录 image pose retarget 实验：素材放在统一素材库里，每个实验 case 决定输入角色图和参考姿态图，每次网页模型提交保存为一个 run。

## 快速入口

| 想做的事 | 文件或目录 |
|---|---|
| 查看带图片的实验结果网页 | [`docs/experiment-results.html`](docs/experiment-results.html) |
| 查看目录结构和组织规则网页 | [`docs/pose-retarget-structure.html`](docs/pose-retarget-structure.html) |
| 查看或修改某个 case 的输入角色和姿态来源 | `experiments/<case_id>/case.yaml` |
| 查看或修改某次 run 的 prompt、模型、输出数量和备注 | `experiments/<case_id>/runs/<run_id>/run.yaml` |
| 保存某次 run 的输出图 | `experiments/<case_id>/runs/<run_id>/outputs/` |
| 保存素材和渲染输入图 | `datasets/assets/<asset_id>/` |
| 保存过程记录和总结 | [`records/`](records/) |

## 目录说明

```text
datasets/assets/
  <asset_id>/
    asset.yaml
    source/
    blender/
    renders/

experiments/
  _template/case.yaml
  E001/
    case.yaml
    runs/
      r001/
        prompt.md
        run.yaml
        outputs/

docs/
  experiment-results.html
  pose-retarget-structure.html

records/
  README.md
```
