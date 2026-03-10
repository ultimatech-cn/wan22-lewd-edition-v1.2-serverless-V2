# Quick Start

如果你要看从拿到客户工作流到交付的完整顺序，先看：

- [SOP_SIMPLE.md](./SOP_SIMPLE.md)

## 1. 先改配置

编辑这两个文件：

- `project-config/custom-nodes.txt`
- `project-config/model-manifest.txt`

## 2. 构建本地镜像

```powershell
docker build --platform linux/amd64 -t runpod-serverless-template:local .
```

## 3. 启动本地环境

```powershell
docker-compose up
```

访问：

- Worker API: <http://localhost:8000/docs>
- ComfyUI: <http://localhost:8188>

## 4. 下载模型到 Network Volume

如果本地或临时 Pod 已挂载 Volume：

```bash
bash scripts/download-models-to-volume.sh /runpod-volume project-config/model-manifest.txt
```

## 5. 部署前最少检查

- 自定义节点已写入 `project-config/custom-nodes.txt`
- 模型清单已写入 `project-config/model-manifest.txt`
- 客户工作流已确认是 API 导出格式
- 至少完成一次本地或测试环境验证
