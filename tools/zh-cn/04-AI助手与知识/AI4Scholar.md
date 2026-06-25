# AI4Scholar

> 文档日期：2026-06-13 | 编辑：待填
> 价格：注册送 50 积分，会员三档（轻量/标准/专业）+ 积分包（具体金额官网 `/pricing` JS 渲染未索引） | 上手难度：中等
> (已删除)：★★★☆

## 一句话评价
从文献检索进化为完整学术工作站——3.0 打通找/读/写/引/画/出 PPT 全流程，MCP 生态集成 Claude Code/Cursor，但定价仍不透明且非建筑专用。

## 推荐与否
观望 — 3.0 版本完成度显著提升，PPT 生成、学术前沿（News）和读/写/引闭环是实打实的效率增益，MCP 生态降低了 Agent 集成门槛，但定价方案仍不透明、团队背景待验证、且是完全通用的学术工具（非建筑行业适配），建筑师的直接使用场景有限。

## 核心优缺点

优点：
1. **完整学术工作流闭环**（3.0 新增）：找文献 → 读论文（GROBID 解析 + AI 笔记）→ 写作（TipTap 编辑器 + Auto-Cite 自动引用）→ 科研绘图（Nano）→ PPT 生成（.pptx 可编辑），五个环节一站完成
2. **PPT 生成**（3.0 新增）：上传论文/网页/文本自动生成可编辑 .pptx（原生 DrawingML），双 Agent 架构（Strategist 设计规范 + Executor 逐页生成），四套风格（学术/顶级咨询/普通咨询/通用），单页 30 秒重生成，失败自动退积分
3. **学术前沿（News）**（3.0 新增）：聚合 76 个顶级期刊 X（Twitter）账号最新论文动态，每小时自动更新，按学科和热度排序
4. **Auto-Cite 自动引用标注**：粘贴论文段落自动插入真实引用（支持 IEEE/APA/Vancouver/Nature 格式），引用均来自真实学术数据库而非 AI 编造，是目前少有的"防幻觉引用"工具
5. **六大学术源统一 API**：整合 Semantic Scholar（2 亿篇）、PubMed（3600 万篇）、arXiv、bioRxiv、medRxiv、Google Scholar，一次认证、统一返回格式；3.0 新增中文文献补充入口
6. **MCP 原生集成**：提供 `ai4scholar` npm 包和 `ai4scholar-mcp` Python 包，支持 Claude Desktop/Claude Code/Cursor/Cherry Studio/OpenClaw 等 AI Agent 客户端，34-36 个学术工具自然语言驱动
7. **国内部署优化**：服务部署在国内，访问无需科学上网
8. **会员体系**（3.0 新增）：轻量/标准/专业三档订阅 + 双轨积分（月度积分按月重置优先消耗 + 积分包永久有效），邀请好友双方各得 50 积分

缺点/不足：
1. **定价方案仍不透明**：3.0 已上线三档会员（轻量/标准/专业），但官网 `/pricing` 页面内容通过 JS 渲染，搜索引擎无索引，三档具体价格和积分消耗单价均未公开可查；微信宣传文也未提及具体金额
2. **团队背景待验证**："Nature 一作团队"为自述，未关联具体论文 DOI
3. **非建筑专用**：通用学术工具，没有建筑规范/建筑类型学/材料构造等建筑领域数据库，建筑师直接使用场景有限
4. **竞争激烈赛道**：Elicit、Consensus、SciSpace、Semantic Scholar 自身 API、Perplexity 等均有类似文献检索+AI 分析能力；3.0 新增的 PPT 生成和学术前沿功能在部分竞品中也有覆盖
5. **Google Scholar 依赖代理**：非官方 API，可用性和稳定性存疑
6. **中文文献仅为补充**：3.0 中文文献入口定位为"必要补充"，主力仍在英文文献侧，国内建筑行业用户的中文文献检索体验待验证

## 适合人群
- 推荐给：需要文献综述自动引用标注的研究者（硕博/高校教师），或想在自己的 AI Agent 中集成学术检索能力的开发者
- 不推荐给：只需日常查阅建筑规范/案例的建筑师——Dimensions.com + 建筑曲奇导航 + ChatGPT 更直接

## 为什么不推荐（★ 评级说明）
非"不推荐"，而是"观望"：3.0 版本将产品从"分散功能模块"升级为"完整学术工作站"，找/读/写/引/画/出 PPT 全流程闭环 + 会员体系搭建完成，产品化程度显著提升。Auto-Cite 和 MCP 集成方向正确，但定价模糊 + 非建筑专用使其在建筑AI工具目录中的直接推荐价值有限。建议 4-6 个月后重新评估（3.0 刚上线，需观察运营数据）。

## 比同类好在哪
- vs **Elicit/Consensus**：AI4Scholar 的 Auto-Cite 功能直接在论文段落中标注引用位置，而非仅检索文献列表；3.0 新增 PPT 生成和学术前沿（76 期刊聚合），功能覆盖面更广；提供 MCP 协议集成，可嵌入 AI Agent 工作流
- vs **Semantic Scholar 官方 API**：AI4Scholar 统一了 6 个数据源接口（含中文文献补充入口），语义搜索支持中文自然语言查询
- vs **Perplexity**：学术文献检索精度更高，返回结构化数据（含 BibTeX/RIS 导出）；3.0 读/写/引/下载闭环在学术场景下比通用搜索工具效率更高

## 3.0 版本要点（2026.06.12 上线）
1. **PPT 生成**：上传论文自动生成可编辑 .pptx，双 Agent 架构，四套风格，单页重生成
2. **学术前沿（News）**：聚合 76 个顶级期刊 X 账号，每小时更新
3. **工作流闭环**：找/读/写/引/下载五环节一站完成，中间无需复制粘贴
4. **会员订阅**：轻量/标准/专业三档 + 双轨积分（月度优先消耗 + 积分包永久有效）
5. **中文文献入口**：作为英文文献的补充搜索通道
6. **邀请好友**：双方各得 50 积分，无邀请上限

## 技术栈推测
Next.js（前端框架，页面 JS 渲染）+ Python 后端（`ai4scholar-mcp` Python 包）。PPT 生成推测使用 python-pptx 或自建 DrawingML 渲染引擎（双 Agent：Strategist + Executor）。文献解析使用 GROBID。科研绘图模块（Nano）推测集成 SD/Flux 类模型进行 text-to-diagram 生成。MCP server 实现推测基于 `mcp` Python SDK。会员积分计费系统实现细节未知。

## 信息来源与时效性

| 数据点 | 来源 | 可信度 |
|---|---|---|
| 3.0 版本全部新功能（PPT/News/会员/工作流闭环/中文文献/邀请好友） | [微信公众号 3.0 发布文](https://mp.weixin.qq.com/s/aI5g8UipuqRLc2ajN7t3bQ)（2026.06.12，Chrome CDP 抓取全文） | 官方 |
| 产品功能、六大文献源、Auto-Cite | [官网](https://ai4scholar.net) + [微信公众号介绍](http://mp.weixin.qq.com/s?__biz=Mzk3NTAwODg0Mw==&mid=2247483821&idx=1&sn=67e33201278695c6ac7a246dc4174c68) | 官方 |
| MCP 集成、34 学术工具、OpenClaw 支持 | [npm ai4scholar](https://www.npmjs.com/package/ai4scholar) + [PyPI ai4scholar-mcp](https://pypi.org/project/ai4scholar-mcp/0.2.3/) + [OpenClaw 教程](http://mp.weixin.qq.com/s?__biz=Mzk2NDMzMzc1MQ==&mid=2247483885&idx=1&sn=d96e16521cbff223b8f414daa2933bab) | 可靠 |
| 注册送 50 积分、邀请好友双方各得 50 积分 | 多篇微信宣传文一致 | 可靠 |
| 科研绘图 (Sci-Draw/Nano) | [微信公众号](http://mp.weixin.qq.com/s?__biz=Mzk3NTAwODg0Mw==&mid=2247484063&idx=1&sn=5fa19ffd5d25aa15c45ee08cc6ee6c23) + 3.0 发布文 | 官方 |
| 会员三档（轻量/标准/专业）存在，但具体金额未公开 | 3.0 发布文确认三档结构，官网 `/pricing` JS 渲染无索引 | **缺失** |
| "Nature 一作团队" | 微信公众号自述，未关联具体 DOI | 待验证 |
| 国内部署、访问无需科学上网 | 微信公众号自述 + 官网可访问性推断 | 推测 |
| MCP SSE 端点 `mcp.ai4scholar.net/sse` | [LobeHub MCP 目录](https://lobehub.com/mcp/literaf-ai4scholar-plugin-codex) | 可靠 |

## 更新记录
- 2026-06-13：初次撰写，定价和用户量数据缺失待后续补充
- 2026-06-13（同日）：基于官方 3.0 发布文（`aI5g8UipuqRLc2ajN7t3bQ`）补充 PPT 生成、News 学术前沿、会员体系、工作流闭环、中文文献入口、邀请好友等 8 项新功能，更新竞品对比和评分依据

---

<!-- 内部评分（不对外） -->
**6维评分（1-5）**：适配 2 | 功能 4 | 质量 3 | 上手 3 | 性价比 2 | 稳定 3 → 加权综合 2.9 → ★★★☆
