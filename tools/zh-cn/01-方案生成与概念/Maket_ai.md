# Maket.ai

> 文档日期：2026-06-12 | 编辑：待填
> 价格：免费（1 项目 + 低分辨率），Pro $20-30/月（$24/月 年付），Enterprise ~$1,200/月 | 上手难度：零门槛
> (已删除)：★★★

## 一句话评价
自然语言直出户型的"概念加速器"——住宅方案构思阶段从几周缩到几分钟，但输出仍需建筑师把关空间合理性。

## 推荐与否
观望 — 对住宅方案初期的快速户型比选很有价值，但空间推理稳定性和非标准地块适应性仍不足以放心全自动使用。

## 核心优缺点

优点：
1. **文生户型图零门槛**：输入"1,800 平方英尺、3 卧 2 卫、开放式厨房"秒出 10-15 套带尺寸标注的平面方案，无需 CAD 基础
2. **对话式平面图编辑**：说"把厨房变大"、"加个车库"即刻修改，省去手动重画的时间——对设计迭代频繁的方案阶段极为实用
3. **法规助手（Regulatory Assistant）**：上传分区法规 PDF，用自然语言提问退线/高度/用途限制——ArchLink M4 功能的对标参考
4. **DXF 导出衔接专业流程**：AI 生成草案可导出 DXF 进 AutoCAD/Revit/Rhino 深化，不是"只玩一次的玩具"
5. **$3.4M CAD 种子轮 + 2026 年 V2 发布**：融资验证了产品方向，V2 的 agentic 编辑和多层支持（最高 4 层）能力提升显著

缺点/不足：
1. **空间推理不稳定**：非矩形地块、斜坡基底、复杂多首层场景下房间比例失调、走廊浪费、动线不合理问题频出
2. 仅限住宅场景——商业/综合体/公共建筑不适用
3. Trustpilot 2.3/5（仅 7 评）——用户反馈两极分化，营销承诺和实际输出质量有 gap
4. 无机电专业考虑——给排水/暖通/电气路由不在生成逻辑内，非建筑学专业的结构评估也要靠人工

## 适合人群
- 推荐给：住宅开发商/建造商（快速户型方案比选）、建筑学生对住宅设计的初步探索、小型住宅建筑师做概念阶段的布局启发
- 不推荐给：复杂/非标准地块项目（山地/异形地）、需要施工图交付的设计院、商业/公共建筑设计团队

## 为什么不推荐（3★）
核心原因是可靠性不足。Maket 解决了住宅概念阶段"快"的问题，但"准"——空间比例、动线逻辑、结构合理性——仍需要建筑师人工修正。在 AI 产出需要二次校验的前提下，时间节省没有宣称的那么显著。Plus 住宅建筑师本身做户型的速度已经不慢，Maket 的增量价值在标准矩形地块上显示，复杂场景下反而可能减慢节奏。

## 技术栈推测
底层推测基于 **Transformer + 图神经网络（GNN）** 的混合架构。户型平面生成的核心是将房间拓扑关系建模为图（节点=房间、边=邻接关系），然后通过空间布局优化算法将图转换为矩形分割平面图（rectangular floorplan tiling）。V2 的 agentic editing 推测使用了 LLM 解析自然语言编辑指令 + 约束求解器更新布局。DFX 输出基于标准 CAD 图形库。Regulatory Assistant 为 RAG（检索增强生成）系统——上传 PDF 后做 chunking/embedding → LLM 语义检索 → 回答合规问题。

## 信息来源与时效性

| 数据点 | 来源 | 可信度 |
|---|---|---|
| $3.4M CAD 种子轮、100 万+ 注册用户 | [BetaKit 融资报道](https://betakit.com/maket-secures-3-4-million-to-make-floor-planning-quicker-with-ai/)、Maket 官网 | 可靠 |
| V2 2026.4 发布、agentic editing、多层支持 | [IT Brief 报道](https://itbrief.ca/story/maket-launches-version-2-of-ai-home-design-platform) | 可靠 |
| 定价 Free/$20-30/$1,200 | [Maket 官网](https://www.maket.ai/)、[illustrarch Review 2026](https://illustrarch.com/articles/design-softwares/73352-maket-ai-review.html) | 官方 |
| Trustpilot 2.3/5 | [Trustpilot](https://www.trustpilot.com/) | 可靠 |
| DXF 导出、法规助手、风格预设 | [illustrarch Review](https://illustrarch.com/articles/design-softwares/73352-maket-ai-review.html)、[Archgyan](https://archgyan.com/maket-ai-floor-plan-generation-residential/) | 可靠 |
| Transformer + GNN + RAG 技术栈 | 基于产品功能推测，非官方公开 | 推测 |

⚠️ V2 刚于 2026 年 4 月发布，大部分公开评测基于 V1，V2 改进幅度有待独立验证。Maket 在 Trustpilot 上的正面评价多来自非建筑专业人士（业主/建造商），建筑师群体的评价缺乏大规模采样。

## 更新记录
- 2026-06-12：初次撰写

---

<!-- 内部评分（不对外） -->
**6维评分（1-5）**：适配 3 | 功能 4 | 质量 3 | 上手 5 | 性价比 4 | 稳定 2 → 加权综合 3.4 → ★★★
