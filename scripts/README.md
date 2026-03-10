# Scripts

## 核心脚本

- `download-models-to-volume.sh`
  - 读取 `project-config/model-manifest.txt`
  - 下载模型到 Network Volume
  - 支持失败日志输出
  - 支持 `HF_TOKEN`

## 下载脚本行为

- 参数 1：`VOLUME_ROOT`（默认 `/runpod-volume`）
- 参数 2：`manifest`（默认 `project-config/model-manifest.txt`）
- 参数 3：`fail_log`（默认 `/tmp/download-models-failed.txt`）

目录自动识别：

- 若 `<VOLUME_ROOT>/storage` 存在，使用 `<VOLUME_ROOT>/storage/models`
- 否则使用 `<VOLUME_ROOT>/models`

示例：

```bash
bash scripts/download-models-to-volume.sh /runpod-volume project-config/model-manifest.txt /tmp/download-models-failed.txt
```

```bash
bash scripts/download-models-to-volume.sh /workspace project-config/model-manifest.txt /tmp/download-models-failed.txt
```

## 失败处理

- 脚本结束码为 `0`：全部成功或已存在
- 脚本结束码非 `0`：存在失败项，查看失败日志

```bash
cat /tmp/download-models-failed.txt
```

若 Hugging Face 返回鉴权错误，可先设置：

```bash
export HF_TOKEN=<your-hf-token>
```
