# Speckle

> 文档日期：2026-06-12 | 编辑：待填
> 价格：免费（Explore），Team ~$15/编辑/月，Business ~$49/编辑/月；开源版可自托管免费 | 上手难度：较难
> (已删除)：★★★★

## 一句话评价
BIM 世界的 Git——让 Revit/Rhino/Grasshopper/Blender 之间真正实现了版本控制级的实时数据互通，AEC 行业文件式协作的终结者。

## 推荐与否
推荐 — 对有多软件协作需求的设计团队，Speckle 是目前开源生态中唯一做到"你不用学新工具，只在已有工具里协作"的 BIM 数据互操作平台。

## 核心优缺点

优点：
1. **跨 BIM/CAD 软件数据流通**：Revit、Rhino、Grasshopper、Blender、ArchiCAD、AutoCAD、Power BI 等 20+ 连接器，打破格式壁垒
2. **Git 式版本控制**：模型变更可追踪、可回滚、可对比——BIM 世界一直缺的"版本管理"能力
3. **完全开源 + 可自托管**：代码全开源（Apache 2.0），数据不出企业服务器——满足大型设计院的数据安全需求
4. **学生/学术永久免费**：无限制使用所有功能
5. **GraphQL/REST API + Python/JS SDK**：开发者友好，可围绕 Speckle 构建自动化工作流

缺点/不足：
1. **国内 Revit 生态适配未知**——国内设计院主流 Revit 版本的插件是否支持最新 Speckle 需验证
2. 学习曲线陡峭——需要理解"流"（Streams）、"分支"（Branches）、"提交"（Commits）等类 Git 概念
3. 不是 BIM 工具本身——不替代 Revit/Rhino，只是连接和传递数据

## 适合人群
- 推荐给：多软件协作的中型建筑事务所（Rhino 做形态+Revit 做深化+GH 做分析）、开源友好的技术型 BIM 团队
- 不推荐给：只用单一 BIM 工具的团队（Revit 工作共享已够用，不需要额外的互操作层）

## 比同类好在哪
vs BIM 360/ACC：Speckle 胜在跨软件互操作（Revit↔Rhino↔Blender）和开源自托管；Autodesk ACC 胜在 Revit 原生深度集成和施工管理全链路。两者互补——ACC 管理 Revit 内部协作，Speckle 做跨生态连接。vs OpenDataBIM Cloud：Speckle 的开源社区和连接器生态更活跃。

## 技术栈推测
全栈 TypeScript（前端 React + 后端 Node.js）+ PostgreSQL + Redis + 可选 S3 存储。核心是一个"数据 Hub"：各 CAD/BIM 连接器将原生数据转为 Speckle 统一对象模型 → 通过 GraphQL API 推送到 Server → Web Viewer（Three.js）实时渲染 → 其他连接器拉取更新。ChatSpeckle 子项目在以上增加 LLM 层（OpenAI + pandasai）实现 AI 对话查询 3D 模型数据。

## 信息来源与时效性

| 数据点 | 来源 | 可信度 |
|---|---|---|
| 开源、20+ 连接器、Git 式版本控制 | [Speckle 官网](https://speckle.systems/)、[Speckle Docs](https://docs.speckle.systems/) | 官方 |
| Team ~$15/编辑/月、Business ~$49/编辑/月 | [Speckle Community 公告](https://speckle.community/t/announcement-plans-changes-and-new-projects-home/17661) | 官方 |
| 学生/学术永久免费 | [Speckle Docs](https://docs.speckle.systems/) | 官方 |
| ChatSpeckle（AI+3D 查询） | [Speckle GitHub](https://github.com/specklesystems) | 可靠 |
| 国内 Revit 适配 | 未验证 | 推测 |

⚠️ 定价已从 GBP 切换为 USD，2025 年 4 月后采用新的 workspace-based 定价模式。自托管版需自行维护服务器，对非技术团队有运维门槛。

## 更新记录
- 2026-06-12：初次撰写

---

<!-- 内部评分（不对外） -->
**6维评分（1-5）**：适配 4 | 功能 5 | 质量 4 | 上手 2 | 性价比 5 | 稳定 4 → 加权综合 4.2 → ★★★★
