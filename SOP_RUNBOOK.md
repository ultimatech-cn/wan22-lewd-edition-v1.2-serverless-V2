# RunPod Serverless SOP（执行版）

这份是执行级 Runbook，覆盖交付链路中的关键细节与常见坑。

## 一、环境边界先确认

先区分三类环境：

- 本地 Windows：只负责改代码、提交流程，不跑 `/runpod-volume` 命令。
- RunPod 临时 Pod：用于预下载模型到 Network Volume。
- RunPod Serverless Endpoint：实际推理服务。

## 二、Network Volume 挂载规则

同一个 Network Volume 在不同容器中的挂载点可能不同：

- 常见临时 Pod：`/workspace`（有时还有 `/workspace/storage`）
- 常见 Endpoint：`/runpod-volume`

脚本已支持自动识别：

- 若 `<VOLUME_ROOT>/storage` 存在，模型目录用 `<VOLUME_ROOT>/storage/models`
- 否则用 `<VOLUME_ROOT>/models`

建议统一做法：

- 临时 Pod 和 Endpoint 都尽量挂到 `/runpod-volume`
- 如果受模板限制只能挂 `/workspace`，也可用同一脚本执行

## 三、标准执行顺序

1. 拿到客户工作流并在本地跑通。
2. 整理模型与节点依赖。
3. 更新项目配置文件。
4. 推 GitHub。
5. 在挂载 Volume 的临时 Pod 中 `git clone` 并下载模型。
6. 创建 Serverless Endpoint（GitHub source）。
7. Postman 回归测试。
8. 根据输出质量替换近似 LoRA。

## 四、依赖文件必须更新

- `project-config/model-manifest.txt`
- `project-config/custom-nodes.txt`
- `templates/serverless-project/02_dependencies.md`

并且必须满足：

- `workflow.json` 内出现的 `.safetensors` 文件名，全部出现在 `model-manifest.txt`。

## 五、临时 Pod 下载模型（必做）

在临时 Pod 里执行：

```bash
git clone <your-github-repo-url> app
cd app
bash scripts/download-models-to-volume.sh /runpod-volume project-config/model-manifest.txt /tmp/download-models-failed.txt
```

如果你的临时 Pod 只挂了 `/workspace`：

```bash
bash scripts/download-models-to-volume.sh /workspace project-config/model-manifest.txt /tmp/download-models-failed.txt
```

## 六、下载失败处理（HF/CAS）

若出现 `401`、`403` 或 HF CAS bridge 相关报错：

1. 先确认 URL 为公开可匿名下载直链。
2. 再尝试带 `HF_TOKEN`：

```bash
export HF_TOKEN=<your-hf-token>
bash scripts/download-models-to-volume.sh /runpod-volume project-config/model-manifest.txt /tmp/download-models-failed.txt
```

3. 仍失败时，人工下载后上传到 Volume 对应目录。

## 七、下载后核对（必做）

```bash
cat /tmp/download-models-failed.txt
find /runpod-volume/models -name '*.safetensors' | sort
```

核对三件事：

- 失败日志为空或可解释。
- 文件名与 `model-manifest.txt` 一致。
- 工作流引用模型都在 Volume 中存在。

## 八、Endpoint 创建检查项

- Source：GitHub
- Repo/Branch：当前版本
- Volume：与临时 Pod 同一个
- Region：一致
- GPU：满足工作流显存需求
- Container Disk：足够
- Env：按项目要求填齐

## 九、Postman 回归顺序

1. `/health`
2. `/runsync`
3. `/run`
4. `/status`

至少测三组输入：

- 最小样例
- 标准样例
- 边界样例

## 十、排错优先级

1. 模型未下载或路径不一致
2. 模型文件名不匹配
3. 自定义节点缺失
4. 节点版本不匹配
5. 环境变量缺失
6. 资源下载失败
7. GPU/显存不足

## 十一、交付清单

- Endpoint 地址
- 调用方式与示例
- 输入输出 JSON 示例
- 环境变量说明
- GitHub 仓库地址
- 已知限制与后续维护说明
