# Hypar

> 文档日期：2026-06-12 | 编辑：待填
> 价格：免费（最多 3 项目），Pro $25/月或 $250/年，Enterprise $500/座/年（最低 10 座） | 上手难度：中等
> (已删除)：★★★☆

## 一句话评价
云端参数化生成设计——把 Grasshopper 的逻辑封装为可复用、可组合的 Web Function，让建筑师在浏览器里做 AI 辅助的参数化设计。

## 推荐与否
观望 — 对有 Grasshopper 基础的技术型建筑师是极有价值的云端协作工具，但对大多数建筑师上手门槛不低。

## 核心优缺点

优点：
1. **"Function-as-design-logic"范式**：把设计规则编码为可复用的 Function（如 EnvelopeBySketch、LevelsByEnvelope），组合多个 Function 生成完整方案——不是画图而是定义规则
2. **Function 市场**：预制设计逻辑块可复用、可分享，社区贡献降低重复造轮子成本
3. **Revit/Rhino/GH 双向同步**：Hypar Hub 在 Revit 内实时可视化云端生成结果
4. **Pro $25/月定价友好**：对比 Rhino+GH 许可证价格 + 硬件成本，Hypar 的个人入口费极具竞争力

缺点/不足：
1. **需要参数化思维**——没玩过 Grasshopper 的建筑师会觉得抽象，上手有门槛
2. Function 生态仍在早期——相比 GH 插件生态（数万+），Hypar 市场可用 Function 少得多
3. 生成的方案质量取决于 Function 的设计——"垃圾规则进垃圾方案出"

## 适合人群
- 推荐给：有 Grasshopper/Dynamo 基础的技术型建筑师、需要云端多方案生成+团队协作的建筑团队
- 不推荐给：不习惯参数化逻辑的建筑师（学习成本高）、需要复杂自由形态建模的项目（不如 Rhino）

## 为什么不推荐（3.5★）
Hypar 的产品方向——云端参数化生成——代表了体量生成工具向云端服务化演进的趋势。但现阶段 Function 生态单薄，产品仍在积累种子用户。对大部分建筑师而言，Hypar 更像一个"有潜力的实验"而非"你现在就需要"的工具。值得注意的是其定价策略（个人 Pro $25/月 + 免费试用 3 项目）和 Function 作为设计逻辑资产的理念，这种模式在建筑 AI 工具中尚不多见。

## 技术栈推测
基于 **C#/.NET 的后端生成引擎** + Web 前端。每个 Function 是独立的 C# 代码包，通过 API 链式调用（上一个 Function 输出 → 下一个 Function 输入）。生成逻辑在云服务器执行（推测 Azure），结果返回到 Three.js Web Viewer 渲染。Revit 集成通过 Hypar Hub 插件实现云端↔本地双向数据传输。Hypar 2.0 引入了 AI 布局建议功能（推测基于 ML 的布局推荐）。

## 信息来源与时效性

| 数据点 | 来源 | 可信度 |
|---|---|---|
| Pro $25/月、Enterprise $500/座/年 | [Hypar 官方定价页](https://docs.hypar.io/pricing-and-purchasing) | 官方 |
| Function 市场、Revit/Rhino 集成 | [Alberta Construction Magazine](https://www.albertaconstructionmagazine.com/architectural-prompting-hypar-2-0-a-new-era-for-space-design/)、[Hypar Docs](https://docs.hypar.io/) | 可靠 |
| Hypar 2.0 AI 布局建议 | [Alberta Construction Magazine](https://www.albertaconstructionmagazine.com/architectural-prompting-hypar-2-0-a-new-era-for-space-design/) | 可靠 |
| C#/.NET + 云渲染架构 | 基于 Hypar 开发者文档推断 | 推测 |

⚠️ Hypar 2.0 的 AI 布局功能尚在早期阶段，实际可用度未经验证。Function 市场规模未公开披露。

## 更新记录
- 2026-06-12：初次撰写

---

<!-- 内部评分（不对外） -->
**6维评分（1-5）**：适配 3 | 功能 3 | 质量 3 | 上手 2 | 性价比 4 | 稳定 3 → 加权综合 3.1 → ★★★
