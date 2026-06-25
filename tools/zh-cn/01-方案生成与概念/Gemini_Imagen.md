# Gemini Imagen (Nano Banana)

> 文档日期：2026-06-12 | 编辑：待填
> 价格：免费（Google AI 基础层），Pro $19.99/月，Ultra $49.99/月；API 按张 $0.045-0.240 | 上手难度：简单
> (已删除)：★★★★

## 一句话评价
Google 原生多模态图像入口，价值不只在生图，而在图像生成/编辑、多参考融合、文字标注和 Gemini 长上下文推理的组合；建筑结构约束仍不如 ControlNet。

## 推荐与否
推荐 — 对需要多参考图融合、精准文字标注、自然语言改图和长上下文方案约束的建筑师来说，是值得单独测试的 Google 多模态视觉入口。

## 核心优缺点

优点：
1. **文字渲染业界最佳**：多语言字符级文字渲染（中/英/日/韩），效果图标注、展板标题、技术图解中的文字清晰可读，远超纯扩散模型
2. **Thinking Mode 先推理后渲染**：模型先"想清楚"空间布局、光影关系、构图再生成，复杂场景的商业逻辑更合理
3. **多参考图融合**：最多 14 张参考图像输入，可用于风格提取、材质参考、空间氛围拼合
4. **Search Grounding 核实事实**：生成前可选查 Google 检索，生成建筑地标/特定风格时减少"幻觉"
5. **百万 token 上下文窗口**：支持超长 prompt，可输入完整的设计说明/规范条文作为生成约束

缺点/不足：
1. **不支持硬结构约束**：无 ControlNet/Canny/DepthMap 式几何控制，不能直接基于 SU/Rhino 线稿出图
2. 闭源闭生态系统，不可本地部署，不可微调
3. 生成速度受推理深度影响——Thinking High 模式下可能等待较久

## 适合人群
- 推荐给：需要快速探索多风格概念方案的建筑师、需要精准文字标注的效果图负责人
- 不推荐给：需要精确几何结构还原的施工图/改造类项目、数据隐私敏感的大型设计院

## 比同类好在哪
vs GPT-image 2：Nano Banana 胜在多参考图融合上限（14 张 vs 8 张）、Search Grounding 核实地标准确性、百万 token 上下文窗口可输入完整规范条文；GPT-image 胜在语义规划到像素全链路、文字渲染和对话式编辑的深度整合。vs Stable Diffusion：文字渲染和语义理解维度碾压，几何精度和控制力则完全不如。

## 技术栈推测
底层基于 **Gemini 3.1 Flash Image 的 MoE Transformer 架构**（Nano Banana 2），自回归多模态生图——图像 token 和文本 token 在同一语义空间逐 token 预测。与纯扩散模型（SD/Flux）不同，不走"噪声→去噪"路径，而是"像写文本一样写图像"。Imagen 4 分支走传统扩散路线（偏写实摄影），与 Nano Banana 形成互补双线。

## 信息来源与时效性

| 数据点 | 来源 | 可信度 |
|---|---|---|
| Nano Banana 2 基于 Gemini 3.1 Flash Image | [DeepLearning.AI The Batch (2026.5)](https://www.deeplearning.ai/the-batch/nano-banana-2-aka-gemini-3-1-flash-image-makes-edits-easier-and-faster/) | 官方 |
| API 定价 $0.045-0.240/张 | [dev.to Nano Banana Pro Guide (2026)](https://dev.to/akaranjkar08/nano-banana-pro-gemini-3-pro-image-developer-guide-api-2026-104c)、[Google AI Studio](https://aistudio.google.com/) | 官方 |
| 14 参考图、5 角色一致性、4K 分辨率 | [DeepLearning.AI](https://www.deeplearning.ai/the-batch/)、[Google Cloud Blog](https://cloud.google.com/blog/) | 官方 |
| Arena.ai 榜单第 1（1,280 Elo） | [fal.ai 对比](https://fal.ai/learn/tools/gpt-image-2-vs-nano-banana-2) | 可靠 |
| Pro $19.99/月、Ultra $49.99/月 | [melies.co 对比](https://melies.co/compare/nano-banana-vs-pro-vs-2) | 待验证 |
| MoE Transformer + 自回归架构 | 社区逆向分析，Google 未公开完整架构 | 推测 |

⚠️ Google 将 Imagen 品牌拆分——Nano Banana 走 Gemini 原生多模态路线，Imagen 4 走传统扩散路线。两者底层架构完全不同，注意区分。

## 更新记录
- 2026-06-12：初次撰写

---

<!-- 内部评分（不对外） -->
**6维评分（1-5）**：适配 4 | 功能 4 | 质量 5 | 上手 4 | 性价比 4 | 稳定 4 → 加权综合 4.2 → ★★★★
