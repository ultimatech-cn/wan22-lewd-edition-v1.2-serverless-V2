# RunPod Serverless 标准项目模板

这套模板不是给客户看的，而是给你和 AI 协作用的。

目标只有一个：每次接到新的 RunPod Serverless 项目时，都用同一套输入结构和交付结构，让 AI 能快速接手、少走弯路。

## 使用方式

每接一个新项目，建议复制这一整套模板到一个新的项目目录，例如：

```text
projects/
  client-a-2026-03-08/
    00_project-intake.md
    01_workflow-audit.md
    02_dependencies.md
    03_deployment-plan.md
    04_test-and-delivery.md
    AI_TASK_BRIEF.md
    workflow-api.json
```

然后按下面顺序使用：

1. 先填写 `00_project-intake.md`
2. 放入客户的 `workflow-api.json`
3. 用 `AI_TASK_BRIEF.md` 把任务交给 AI
4. AI 根据实际情况更新 `01` 到 `04`
5. 项目交付完成后，这一套文件就成为可追溯档案

## 文件说明

- `00_project-intake.md`
  - 客户需求录入表。先把基本信息、目标效果、交付方式填清楚。
- `01_workflow-audit.md`
  - 工作流审计表。AI 或人工在本地跑通后填写。
- `02_dependencies.md`
  - 模型、自定义节点、环境变量、外部依赖的统一清单。
- `03_deployment-plan.md`
  - 仓库改动点、Volume 规划、部署方案、Endpoint 配置。
- `04_test-and-delivery.md`
  - Postman 测试记录、故障排查、交付信息。
- `AI_TASK_BRIEF.md`
  - 专门给 AI 的任务说明模板，方便快速进入执行。

## 最少必填信息

如果时间紧，至少先补齐这些内容：

- 客户工作流 API JSON
- 客户目标效果图或样例输出
- 模型下载链接
- 自定义节点名称或仓库地址
- 部署偏好：GitHub 或 Docker
- 是否需要 S3

## 使用原则

- 不要在模板里直接写真实密钥
- 不确定的地方标记“待确认”
- 每次项目都复制一份，不要直接改模板原件
- AI 输出应优先回填到这套结构中，而不是散落在聊天记录里
