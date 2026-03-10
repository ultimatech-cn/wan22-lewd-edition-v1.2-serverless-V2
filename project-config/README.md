# Project Config

这个目录专门放“每个项目都不同”的配置。

## 文件说明

- `custom-nodes.txt`
  - 自定义节点清单。
- `model-manifest.txt`
  - 模型下载清单。

## 建议原则

- 节点尽量在这里维护，不要直接把每个项目写死到 `Dockerfile`
- 模型尽量通过清单维护，不要写死到下载脚本里
- AI 处理新项目时，优先改这里
