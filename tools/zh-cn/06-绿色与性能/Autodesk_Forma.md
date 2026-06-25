# Autodesk Forma (Forma Site Design)

> 文档日期：2026-06-12 | 编辑：待填
> 价格：$185-190/月（独立版），AEC Collection 内含（$430-460/月）；30 天免费试用，学生免费 | 上手难度：中等
> (已删除)：★★★★

## 一句话评价
ArchLink 场地分析模块的终极对标——云端 AI 实时日照/风速/噪音分析 + 体量自动生成，但价格让小型事务所望而却步。

## 推荐与否
推荐 — 对中大型建筑事务所在城市级/多栋项目的早期场地分析阶段，是目前最成熟的 AI 驱动工具。小型事务所建议先从免费试用开始评估 ROI。

## 核心优缺点

优点：
1. **AI 实时环境分析**：日照时数、风舒适度（AI 模式秒出 + CFD 详细模式）、噪音、微气候（UTCI 指标）、隐含碳——五大分析同时跑，改一下体量参数结果即时更新
2. **约束驱动的生成式设计**：设定高度、退线、密度目标后 AI 自动生成多个体量方案，按环境性能排序——概念阶段一周的工作压缩到一小时
3. **Revit 双向同步**：场地地理位置和体量数据自动带进 Revit，风分析可在 Revit 内直接运行——无需导出/导入循环
4. **浏览器即开即用**：纯云端运行，不依赖本地硬件，合作方可直接浏览器查看
5. **已获行业认可**：Architectural Record 2025 年度最佳建筑产品、Baker Barrios 事务所报告 40 小时任务压缩至 4 小时

缺点/不足：
1. **价格对小团队不友好**：独立版 $185-190/月，远比国产 AI 工具贵——除非已订阅 AEC Collection
2. 建模能力不如 Rhino/SketchUp——复杂自由形态曲面不支持，更适合方盒子体量
3. 云端依赖——网络不稳定时体验差，国内访问速度可能受限
4. 风/噪音分析为早期近似值，不能替代专业顾问的详细评估

## 适合人群
- 推荐给：中大型建筑事务所（已有 AEC Collection 订阅）、城市设计/多栋住宅开发的方案团队、房地产开发商前期可行性研究
- 不推荐给：小型事务所或个人建筑师（价格过高）、网络环境不稳定地区、需要复杂非线性体量的项目

## 比同类好在哪
vs Archistar：Forma 胜在 Autodesk 生态整合（Revit 双向同步、Dynamo 插件）和环境分析的实时性，Archistar 胜在合规校验维度更多。vs TestFit：Forma 的 AI 生成式设计更偏"探索多种可能性+环境排序"，TestFit 更偏"地产排布效率+户型经济性"——两者在概念设计的不同阶段互补。

## 技术栈推测
底层为 **云原生 WebGL/Three.js 渲染引擎 + 自研 AI 模型矩阵**。分析引擎分为两档：Rapid 模式推测基于预训练的代理模型（surrogate model，在大量 CFD/日照模拟数据上训练的神经网络），实现秒级近似结果；Detailed 模式基于传统物理模拟（CFD/Ray-tracing）。生成式设计模块推测使用进化算法或强化学习在约束空间内搜索帕累托最优解。前身为 2020 年以 ~$2.4 亿收购的 Spacemaker，AI 能力是整合了 Autodesk 内部 AI 研究后的产出。

## 信息来源与时效性

| 数据点 | 来源 | 可信度 |
|---|---|---|
| 独立版 $185-190/月、AEC Collection 内含 | [Autodesk 官网定价页](https://www.autodesk.com/products/forma-site-design/overview) | 官方 |
| AI 实时日照/风/噪音/微气候/碳分析 | [illustrarch Forma Review 2026](https://illustrarch.com/articles/design-softwares/73363-autodesk-forma-review.html)、[Archgyan](https://archgyan.com/autodesk-forma-ai-site-planning-architects/) | 可靠 |
| 生成式设计（Site Automation）、Neural CAD demo | [illustrarch Review](https://illustrarch.com/articles/design-softwares/73363-autodesk-forma-review.html) | 可靠 |
| Revit 双向同步、Forma Board | Autodesk 官方文档 + [illustrarch Review](https://illustrarch.com/articles/design-softwares/73363-autodesk-forma-review.html) | 可靠 |
| AR 2025 年度最佳产品 | Architectural Record 2025 年度评选 | 可靠 |
| Spacemaker 收购 $240M (2020) | Autodesk 投资者公告 | 可靠 |
| 代理模型 + 物理模拟混合架构 | 基于 Autodesk 官方技术博客和行业做法推测 | 推测 |

⚠️ 2026 年新增 "Forma Building Design" 产品线（LoD 200-300 模式设计），独立于 Site Design，定价可能不同。国内用户需评估云端访问速度和 Revit 工作流的实际契合度。

## 更新记录
- 2026-06-12：初次撰写

---

<!-- 内部评分（不对外） -->
**6维评分（1-5）**：适配 4 | 功能 5 | 质量 4 | 上手 3 | 性价比 2 | 稳定 4 → 加权综合 3.8 → ★★★★
