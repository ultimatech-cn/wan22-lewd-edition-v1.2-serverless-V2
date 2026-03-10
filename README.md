# RunPod Serverless Template

这是一个新的精简模板项目，目标不是保留旧项目的历史内容，而是提供一套以后可以重复使用的标准骨架。

它保留了成熟的运行时能力：

- `handler.py`：沿用现有成熟版本
- `src/start.sh`：沿用现有启动与 Network Volume 挂载逻辑
- RunPod Serverless 兼容结构
- 本地 Docker 测试能力

同时把最容易变化的部分改成“配置清单驱动”：

- 自定义节点：`project-config/custom-nodes.txt`
- 模型下载：`project-config/model-manifest.txt`
- AI 协作模板：`templates/serverless-project/`
- 傻瓜式流程：`SOP_SIMPLE.md`

## 适合什么场景

适合你以后每次接新的 RunPod Serverless 项目时，作为起始项目复制一份，然后让 AI 在这份新项目上继续加工。

## 项目结构

```text
runpod-serverless-template/
  .runpod/
  project-config/
  scripts/
  src/
  templates/
  tests/
  Dockerfile
  docker-compose.yml
  handler.py
  QUICK_START.md
  README.md
  requirements.txt
```

## 核心思路

### 1. 运行时尽量稳定

这些文件通常不需要大改：

- `handler.py`
- `src/start.sh`
- `requirements.txt`

### 2. 可变内容尽量配置化

以后大多数项目差异，优先落到这些文件：

- `project-config/custom-nodes.txt`
- `project-config/model-manifest.txt`
- `templates/serverless-project/00_project-intake.md`
- `templates/serverless-project/AI_TASK_BRIEF.md`

### 3. 模型默认走 Network Volume

默认推荐：

- 自定义节点装进镜像
- 模型下载到 `/runpod-volume/models`

这样更适合 RunPod Serverless 的长期维护。

## 新项目标准用法

如果你要按最简单的交付顺序走，先看：

- [SOP_SIMPLE.md](./SOP_SIMPLE.md)

### 第一步：复制这份模板项目

建议按客户项目复制成新目录，例如：

```text
d:\01_Projects\Runpod\projects\client-a-runpod-serverless
```

### 第二步：填写项目资料

优先填写：

- `templates/serverless-project/00_project-intake.md`
- `templates/serverless-project/AI_TASK_BRIEF.md`

然后放入：

- 客户工作流 JSON
- 模型链接
- 节点信息

### 第三步：修改配置清单

编辑：

- `project-config/custom-nodes.txt`
- `project-config/model-manifest.txt`

### 第四步：本地验证

参考：

- [QUICK_START.md](./QUICK_START.md)

### 第五步：部署到 RunPod

可走两条路：

- GitHub 集成部署
- Docker 镜像部署

`.runpod/hub.json` 已保留为模板，可按项目改名和改参数。

## 自定义节点清单格式

`project-config/custom-nodes.txt` 支持两种格式：

```text
# registry 节点
registry:comfyui-kjnodes

# git 仓库，支持可选 branch
git:https://github.com/Comfy-Org/ComfyUI-Manager.git
git:https://github.com/kijai/ComfyUI-KJNodes.git|main
```

## 模型清单格式

`project-config/model-manifest.txt` 使用以下格式：

```text
相对目录|文件名|下载链接|动作
```

动作支持：

- `file`：普通文件下载
- `unzip`：下载后解压 zip
- `untar`：下载后解压 tar 包

示例：

```text
checkpoints/SDXL|model.safetensors|https://example.com/model.safetensors|file
insightface/models|antelopev2.zip|https://example.com/antelopev2.zip|unzip
```

## AI 协作入口

如果要把新项目直接交给 AI，优先给它这两个文件：

- `templates/serverless-project/AI_TASK_BRIEF.md`
- `templates/serverless-project/00_project-intake.md`

## 当前保留的内容

从旧项目复制并保留的“真正有用的部分”主要是：

- 成熟的 `handler.py`
- 成熟的 `start.sh`
- RunPod 基础配置结构
- 标准化项目模板包

旧项目里的历史文档、具体模型下载脚本、特定项目文案没有带过来。
