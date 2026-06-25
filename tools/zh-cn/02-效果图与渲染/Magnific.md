# Magnific

> 文档日期：2026-06-15 | 编辑：Claude
> 价格：订阅制 + credits；旧 Magnific Pro $39/月起，Freepik/Magnific 新体系含 Free、Essential、Premium、Premium+、Pro、Business、Enterprise | 上手难度：简单
> 评分：★★★

## 一句话评价
Freepik/Pikaso 体系下的生成式图像增强与放大工具，适合把低清 AI 图、建筑效果图和室内空间图重构为高细节商业视觉图；其官方远程 MCP 已可授权访问，工具清单显示它已从单点 upscaler 扩展为图像、视频、音频、3D、Stock、Spaces/Flows 的创意生产平台。

## 推荐与否
推荐但限场景 — 对 A0 展板、竞赛图、营销封面、AI 生图终稿增强很有价值；对日常方案汇报、施工级表达、需要严格保真的建筑细节不建议依赖。

## 建筑师任务场景
- 任务：当我是建筑可视化/内容运营人员，已有一张低清 AI 建筑效果图时，我想用 Magnific 把它增强为可用于展板、封面或宣传图的高清视觉图。
- 输入：同一张由 EVAI/建筑学长/通用生图工具生成的低清建筑图；统一提示词约束材质、光影和保真程度。
- 期望输出：画面细节、材质和氛围显著提升，同时主体结构、幕墙分缝、文字和关键构件不被明显篡改。
- 实测结果：待 B1-A 统一实测补充。

## 最新功能判断

| 功能 | 对建筑工作的价值 | 使用边界 |
|---|---|---|
| Generative Upscaling | 2x/4x/8x/最高 16x 级别放大，补足石材、木纹、玻璃、植物、灯光细节 | 会主动“脑补”，幕墙分缝、栏杆、文字、logo 需人工复核 |
| Relight | 快速把白天图改为黄昏、夜景、商业灯光、展厅光等氛围版本 | 只适合氛围表达，不能替代物理照明模拟 |
| Style Transfer / Reimagine | 将草图、低清概念图、白模图转成特定视觉风格 | 容易造成结构漂移，适合早期探索不适合最终交付 |
| Precision Mode | 更保真地提升已有渲染图清晰度，适合成熟效果图轻度增强 | 公开资料显示更偏 2x 保真放大，能力边界需实测 |
| Inpainting / Regeneration | 局部修补糊掉的材质、植物、家具、背景 | 局部内容可能不符合真实设计，需要回 PS 修正 |
| Spaces | 在画布中管理生成、放大、Relight、填充、版本与导出 | 更偏内容生产工作流，对建模/渲染主流程是补充 |
| 官方远程 MCP 入口 | `https://mcp.magnific.com` 可通过 OAuth device code 授权访问；初始化返回 serverInfo `pikaso`，tools/list 当前约 71 个工具，覆盖 account、creations、folders、spaces、images、library、3D、video、audio、design、flows、stock | 需要用户登录授权；工具响应中的内部 identifier/session/request id 不应对外暴露，付费生成前应先查 `account_balance` |
| Mystic / Freepik AI 生成 | Freepik + Magnific 生态中的高质量写实图像生成器 | 属于图像生成入口，需与 Magnific 后期增强区分 |

## 核心优缺点

优点：
1. **生成式细节增强**：不是简单插值，而是根据图像语义、提示词和参数重构材质、纹理、光影。
2. **建筑表现适配度高**：室内设计、建筑效果图、景观氛围图、竞赛展板都能受益。
3. **Relight 对建筑表达很有用**：可快速测试夜景、黄昏、暖光、展厅光等视觉氛围。
4. **从单点工具转向工作流**：Freepik/Pikaso Spaces、Mystic、远程 MCP 工具清单使其不再只是 upscaler，而是向 agent 可调用的创意生产链延伸。
5. **跨媒体能力更强**：MCP 工具覆盖图片生成/编辑/放大/重打光、视频生成/放大、音频、3D、Stock、Flows 和 Spaces。
6. **商业视觉质量强**：适合公众号封面、小红书图组、作品集、投标展示图的“最后一公里”。

缺点/不足：
1. **会改写事实细节**：材质、构造、分缝、文字、logo、家具细部都可能被 AI 重绘。
2. **成本不适合低频用户**：旧体系 $39/月起；新体系改为 credits + 套件订阅，仍偏专业用户。
3. **不是渲染器**：不能从模型计算真实光照，也不能替代 Enscape/V-Ray/Corona。
4. **批量试错消耗快**：Creativity、HDR、Resemblance、Prompt Strength 等参数需要多次试，credits 容易被消耗。
5. **公开资料口径混杂**：旧 Magnific 定价、Freepik 套件定价、API/MCP 入口并存，入库价格与 credits 应标注“以官网为准”。

## 适合人群
- 推荐给：建筑可视化设计师、室内设计师、效果图后期、竞赛图/作品集制作者、内容运营、AI 图像创作者。
- 谨慎使用：需要严格保持建筑构造、品牌资产、文字标识、真实材料节点的团队。
- 不推荐给：只做 1080p 屏幕汇报、预算敏感且低频出图的个人用户。

## 建筑工作流建议

### 1. 效果图终稿增强
V-Ray/Enscape/Corona 输出中等分辨率图 → PS 基础调色裁切 → Magnific 低 Creativity + 高 Resemblance / Precision → 回 PS 检查结构、文字、logo、材料。

### 2. 早期概念图强化
Midjourney / SD / DALL-E / Mystic 生成空间氛围 → Magnific 用 prompt 指定材质与光影 → 多版本筛选 → 作为设计方向参考，不直接作为设计依据。

### 3. Relight 氛围测试
输入已有室内/建筑图 → 用文字或参考图指定 golden hour、gallery lighting、night commercial lighting 等 → 输出多组氛围方案 → 仅用于视觉沟通。

### 4. 材质细节探索
白模/低清材质图 → 指定 rough concrete、travertine、brushed metal、walnut veneer 等 → 生成 moodboard 或汇报辅助图，不作为真实 PBR 材质。

## 比同类好在哪
Topaz Gigapixel / Photo AI 更偏摄影保真和本地后期，Magnific 更擅长“漂亮地补细节”；Upscayl / Real-ESRGAN 成本低但创意细节弱；Clarity AI / ComfyUI 可复刻部分生成式放大能力但部署门槛高。Magnific 的优势是上手简单、商业视觉冲击强、与 Freepik 创意套件整合更深。

## 技术栈判断
公开资料普遍将 Magnific 归为生成式 AI upscaler：在放大过程中以原图结构为条件，通过扩散/深度学习模型重建纹理、光影和细节。具体底层模型未完全公开，Stable Diffusion / latent diffusion 相关说法应标为推测，不应写成确定事实。

## 信息来源与时效性

| 数据点 | 来源 | 可信度 |
|---|---|---|
| Freepik/Magnific 新套餐含 Free、Essential、Premium、Premium+、Pro、Business、Enterprise | [Magnific Plans and pricing](https://www.magnific.com/ai/docs/plans-and-pricing) | 高 |
| Freepik 已将 Magnific 纳入 AI 创意套件，支持最高 10K 图像增强 | [Freepik](https://jp.freepik.com)、[Freepik](https://it.freepik.com/) | 高 |
| 旧 Magnific Pro $39/月、Premium $99/月、Business $299/月 | [The Paper](https://www.thepaper.cn/newsDetail_forward_25441037)、[UIED](https://www.uied.cn/62636.html)、[ToolJunction](https://www.tooljunction.io/ai-tools/magnific-ai) | 中 |
| 16x 放大、Creativity/HDR/Resemblance、Prompt 引导 | [ToolJunction](https://www.tooljunction.io/ai-tools/magnific-ai)、[UIED](https://www.uied.cn/62636.html) | 中高 |
| Relight 支持提示词、参考图、Lightmap 改光 | [新浪看点](https://k.sina.cn/article_5648162302_m150a81dfe033016vbw.html)、[CSDN](https://blog.csdn.net/m0_46163918/article/details/140134143) | 中 |
| Freepik + Magnific 推出 Mystic 图像生成器 | [电子发烧友](https://m.elecfans.com/article/5328170.html)、[Toolify](https://www.toolify.ai/zh/ai-news-cn/mystic-ai%E5%9B%BE%E5%83%8F%E7%94%9F%E6%88%90%E5%99%A8%E5%92%8Chotshot-ai%E8%A7%86%E9%A2%91%E5%88%B6%E4%BD%9C%E5%99%A8%E6%B7%B1%E5%BA%A6%E8%AF%84%E6%B5%8B-3819906) | 中 |
| API 侧支持 Freepik AI Upscaler Magnific | [RapidAPI](https://rapidapi.com/freepik-company-freepik-company-default/api/freepik-ai-upscaler-magnific) | 中 |
| 官方 MCP 入口要求 Bearer token，保护资源元数据指向 Magnific OIDC 授权服务器，scope 含 `openid profile email mcp:custom-audience` | [Magnific MCP](https://mcp.magnific.com)、[Magnific OAuth metadata](https://mcp.magnific.com/.well-known/oauth-authorization-server)、[Magnific protected resource metadata](https://mcp.magnific.com/.well-known/oauth-protected-resource) | 高 |
| 授权后 MCP 初始化返回 serverInfo `pikaso`，tools/list 约 71 个工具，含 `images_upscale`、`images_relight`、`video_upscale`、`spaces_*`、`flows_*`、`stock_*` 等 | 2026-06-15 本地 OAuth device code 授权后 tools/list 实测 | 高 |

⚠️ 当前处于 Freepik/Magnific/Pikaso 品牌、套餐与 agent 接入形态迁移期，价格、credits、功能入口、MCP 可调用工具需以官网实时页面和登录后客户端返回为准。

## 更新记录
- 2026-06-15：补充 Freepik 整合后最新功能、Relight、Spaces、Mystic、官方 MCP 入口、价格体系迁移与建筑工作流边界
- 2026-06-12：初次撰写

---

<!-- 内部评分（不对外） -->
**6维评分（1-5）**：适配 3 | 功能 4 | 质量 5 | 上手 4 | 性价比 2 | 稳定 3 → 加权综合 3.5 → ★★★
**任务评分（待实测）**：任务完成度_ | 建筑语义理解_ | 控制能力_ | 修改成本_ | 汇报可用度_
