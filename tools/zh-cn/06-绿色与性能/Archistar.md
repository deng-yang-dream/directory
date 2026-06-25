# Archistar

> 文档日期：2026-06-12 | 编辑：待填
> 价格：免费（2,000m² 以下地块），Basic ~AUD$63-95/月，Professional ~AUD$230-345/月 | 上手难度：简单
> (已删除)：★★★☆

## 一句话评价
澳洲市场的地块分析+生成式设计旗舰——把"这块地能建什么"做到了极致，但只服务澳洲市场。

## 推荐与否
观望 — 在澳洲市场是非常成熟的 AI 地产工具，对中国市场借鉴价值在于规划校验+生成式设计的整合模式，但直接可用性为零。

## 核心优缺点

优点：
1. **规划数据+AI 生成一站式**：自动读取地块的 zoning/FSR/高度限制/退线，AI 在这些硬约束下生成合规的 3D 体量——这个"规划校验→生成"的闭环是 ArchLink M1 的理想形态
2. **eCheck AI 审图**：25+ 市政机构使用，AI 自动对照数字化的区划/建筑规范审查设计合规性——从几周压缩到几分钟
3. **CoreLogic/Nearmap 数据整合**：地块交易记录、高分辨率航拍、开发项目列表一键获取
4. **Revit/Rhino/SketchUp 集成**：合规体量可导出做深化设计

缺点/不足：
1. **仅限澳洲市场**——中国建筑师完全不可用
2. Professional 约 AUD$230-345/月，中等偏高定价
3. Capterra 评分显示"性价比"维度低至 2.0/5——部分用户认为功能与价格匹配度不高

## 适合人群
- 推荐给：研究建筑 AI 产品方向的产品经理（规检+生成的整合模式值得研究）、有澳洲项目的建筑师/开发商
- 不推荐给：中国国内建筑师（无数据覆盖）

## 为什么不推荐（3.5★）
对中国建筑师而言，Archistar 是一面"镜子"——展示了规划校验+AI 体量生成的理想产品形态，但数据壁垒（澳洲规划数据、CoreLogic 房产数据）使其无法复制到中国市场。要实现类似的"地块选点→规划分析→体量生成"闭环，关键难点在于接入中国的控规数据和地图 POI，而非简单照搬 Archistar 的路子。

## 技术栈推测
底层为 **GIS 数据引擎 + 参数化生成 + 规则引擎** 的混合架构。规划数据层：结构化存储各州/市的 zoning maps、FSR、高度限制等空间化规划规则 → 规则引擎自动提取选地的约束条件 → 参数化生成引擎在约束空间内生成合规体量 → eCheck 反向验证。AI 成分推测在视觉层面（Nearmap 航拍分析）和规则解析层面（NLP 解析规划文本），生成式设计部分更偏确定性算法。

## 信息来源与时效性

| 数据点 | 来源 | 可信度 |
|---|---|---|
| 定价 $63-595 AUD/月、免费 2000m² 限制 | [Capterra](https://www.capterra.com/p/213621/Archistar/)、[Feasly 指南 (2026)](https://www.feasly.com.au/guides/property-development-apps-digital-tools-australia) | 可靠 |
| eCheck AI 审图、25+ 市政机构 | [RankMyAI](https://www.rankmyai.com/tools/64d4dbbc-3756-47e5-9211-e0cf0b3bd3d6/archistar) | 可靠 |
| CoreLogic/Nearmap 数据整合 | [creativetoolsai.com](https://www.creativetoolsai.com/architecture-ai-tool/archistar/) | 可靠 |
| Capterra 性价比 2.0/5 | [Capterra 用户评价](https://www.capterra.com/p/213621/Archistar/#reviews) | 待验证（仅少量评价） |

⚠️ 本评测关注 Archistar 的产品模式和架构，作为 ArchLink M1 场地分析+体量生成方向的对照参考。中国市场数据未覆盖，不推荐国内用户直接使用。

## 更新记录
- 2026-06-12：初次撰写

---

<!-- 内部评分（不对外） -->
**6维评分（1-5）**：适配 1 | 功能 4 | 质量 4 | 上手 3 | 性价比 3 | 稳定 4 → 加权综合 3.0 → ★★★
