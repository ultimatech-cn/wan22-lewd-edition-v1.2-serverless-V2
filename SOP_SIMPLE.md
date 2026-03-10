# RunPod Serverless SOP（总览版）

这份是总览流程，不展开细节。  
执行细节请看 `SOP_RUNBOOK.md`。

## 0. 核心约束（不省略）

- `/runpod-volume` 命令只在 RunPod Linux 容器里执行，不在本地 PowerShell 执行。
- 第 5 步后必须先推 GitHub，再在临时 Pod 里 `git clone`。
- 下载模型必须用“显式挂载了 Network Volume 的临时 Pod”。
- `workflow.json` 中所有 `.safetensors` 都必须能在 `model-manifest.txt` 对应到。
- 脚本跑完必须核对失败日志和 Volume 实际文件。

## 1. 收资料

- 工作流（优先 API JSON）
- 客户效果参考
- 输入样例
- 模型来源
- 自定义节点来源

## 2. 本地跑通

- 先在本地 ComfyUI 跑通
- 和客户参考做对比
- 记录缺失模型和缺失节点

## 3. 整理依赖

- 更新 `project-config/model-manifest.txt`
- 更新 `project-config/custom-nodes.txt`
- 更新 `templates/serverless-project/02_dependencies.md`

## 4. 修改模板项目

- 按需改 `Dockerfile`、`handler.py`、`src/start.sh`、`.runpod/hub.json`
- 仅做最小必要改动

## 5. 推 GitHub

- 本地提交后推送仓库

## 6. 准备 Volume

- 创建临时 Pod 并挂载同一个 Network Volume
- 在 Pod 里 `git clone` 后执行下载脚本

## 7. 创建 Endpoint

- Source 选 GitHub
- 挂载同一个 Volume
- 核对 Region、GPU、Disk、环境变量

## 8. Postman 测试

- `/health`、`/runsync`、`/run`、`/status`
- 至少测最小样例、标准样例、边界样例

## 9. 交付

- Endpoint 地址
- 调用示例
- 输入输出 JSON 示例
- 环境变量说明
- 仓库地址

---

执行细节与排错命令见：`SOP_RUNBOOK.md` 和 `DEPLOY_TODAY.md`。
