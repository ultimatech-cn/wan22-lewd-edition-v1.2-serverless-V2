# WAN 2.2 Today Deploy（执行清单）

今天目标：先稳定跑通，不追求一次性最优画质。

## 1. 本地改完后先推 GitHub

```powershell
git add .
git commit -m "wan22 deploy update"
git push
```

## 2. 开临时 Pod（必须挂载同一个 Volume）

- 优先 mount 到 `/runpod-volume`
- 若模板限制只能挂 `/workspace` 也可执行

## 3. 在临时 Pod 内拉代码并下载模型

```bash
git clone <your-github-repo-url> app
cd app
bash scripts/download-models-to-volume.sh /runpod-volume project-config/model-manifest.txt /tmp/download-models-failed.txt
```

如果 Volume 在 `/workspace`：

```bash
bash scripts/download-models-to-volume.sh /workspace project-config/model-manifest.txt /tmp/download-models-failed.txt
```

## 4. 下载失败时处理

出现 `401/403/CAS`：

```bash
export HF_TOKEN=<your-hf-token>
bash scripts/download-models-to-volume.sh /runpod-volume project-config/model-manifest.txt /tmp/download-models-failed.txt
```

仍失败就人工下载并上传对应路径。

## 5. 下载后强制核对

```bash
cat /tmp/download-models-failed.txt
find /runpod-volume/models -name '*.safetensors' | sort
```

核对：

- 失败日志是否为空
- `workflow.json` 与 `model-manifest.txt` 是否一致
- Volume 中文件是否齐全

## 6. 创建 Endpoint 并回归

- Source 选 GitHub
- 挂载同一个 Volume
- 检查 Region/GPU/Container Disk/Env
- Postman 依次测 `/health`、`/runsync`、`/run`、`/status`
