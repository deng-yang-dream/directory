# 工具目录索引

## 📊 统计信息
- **总工具数**: 221
- **Wiki工具**: 177
- **评测工具**: 44
- **最后更新**: 2026-06-26

## 📁 目录结构

### 中文文档 (zh-cn)
```
tools/zh-cn/
├── 01-方案生成与概念/     # 方案生成、概念设计 (28个工具)
│   ├── 方案生成/          # AI辅助方案构思、体量推敲 (22个)
│   └── [概念设计/]        # 概念方案深化 (暂空)
├── 02-效果图与渲染/       # AI渲染、图像生成 (50个工具)
│   ├── AI渲染/            # AI驱动的效果图生成 (40个)
│   └── [图像处理/]        # 图像增强、风格迁移 (暂空)
├── 03-绘图与手绘/         # 绘图、手绘工具 (1个工具)
├── 04-AI助手与知识/       # AI助手、知识问答 (27个工具)
│   ├── AI助手/            # 通用AI对话、设计助手 (20个)
│   ├── 知识问答/          # 建筑知识库问答 (1个)
│   └── [数据分析/]        # 数据分析工具 (暂空)
├── 05-汇报与数据/         # 汇报输出、PPT演示 (43个工具)
│   ├── 城市数据/          # GIS、城市级数据分析 (30个)
│   ├── 汇报输出/          # 文本/图表汇报工具 (6个)
│   ├── PPT演示/           # PPT/演示文档工具 (1个)
│   └── 数据管理/          # 数据整理工具 (1个)
├── 06-绿色与性能/         # 绿色建筑、性能分析 (9个工具)
│   ├── 绿色建筑/          # 可持续设计工具 (3个)
│   └── [性能分析/]        # 能耗/日照/风环境模拟 (暂空)
├── 07-建模与BIM/          # 3D建模、BIM工具 (36个工具)
│   ├── 3D建模/            # 三维建模工具 (17个)
│   └── BIM协同/           # BIM协作与数据交换 (12个)
├── 08-规范审查/           # 规范检查、合规审查 (18个工具)
├── 09-学术与实验室/       # 学术机构、AI实验室 (8个工具)
└── 10-其他/              # 其他工具、API服务 (1个工具)
```

**说明**：
- `[暂空]` 表示子分类目录已创建但暂无工具
- root 目录包含原始评测数据库文件（44个）
- 子分类目录包含 Wiki 工具文件（177个）

### 英文文档 (en)
```
tools/en/
├── 01-concept-design/     # Concept design tools
├── 02-rendering/          # AI rendering tools
├── 03-drawing-sketching/  # Drawing and sketching tools
├── 04-ai-assistant/       # AI assistant tools
├── 05-presentation-data/  # Presentation and data tools
├── 06-green-performance/  # Green building tools
├── 07-modeling-bim/       # 3D modeling and BIM tools
├── 08-code-review/        # Code review tools
├── 09-academic-labs/      # Academic research labs
└── 10-other/             # Other tools
```

## 🔧 添加新工具

### 1. 选择分类
根据工具的主要功能选择适当的分类目录。请参考 `scenes` 元数据字段进行分类。

### 2. 创建工具文件
```bash
# 中文文档（已建立子分类的类别）
touch tools/zh-cn/分类目录/子分类/工具名称.md

# 中文文档（无子分类的类别）
touch tools/zh-cn/分类目录/工具名称.md

# 英文文档（暂未翻译）
touch tools/en/category-directory/tool-name.md
```

### 3. 使用标准格式
参考现有工具文件的格式，包含：
- Frontmatter 元数据（`scenes` 字段必须）
- 一句话描述
- 详细介绍
- 优缺点分析
- 信息来源

### 4. 提交更改
```bash
git add tools/
git commit -m "feat(tools): 添加新工具 [工具名称]"
git push
```

## 📋 文件命名规范
- 使用小写字母
- 使用连字符分隔单词
- 避免特殊字符
- 保持名称简洁

示例: `midjourney.md`, `stable-diffusion.md`

## 🔍 搜索工具
工具可以通过以下方式查找：
1. 按分类目录浏览（推荐使用子分类导航）
2. 使用网站搜索功能
3. 查看工具索引文件

## 📊 详细统计
完整统计数据请查看 [STATISTICS.md](STATISTICS.md)

## 🛠️ 维护指南

### 分类规则
- 新工具按 `scenes` 字段的首个有效标签归入主分类
- 同一主分类内按 scenes 细分至子分类
- 工具数量超过20个的主分类应建立子分类
- 评测数据库文件保留在 root 目录

### 定期更新
1. 每月检查工具信息准确性
2. 更新过时的链接和价格信息
3. 补充缺失的 scenes 元数据
4. 平衡各子分类的工具数量

## 🆘 问题反馈
如果在使用工具目录时遇到问题，请：
1. 检查文件命名和格式
2. 查看现有工具示例
3. 在GitHub Issues中报告问题

## 🔗 相关链接
- **详细统计**: [STATISTICS.md](STATISTICS.md)
- **项目网站**: https://deng-yang-dream.github.io/directory/
- **GitHub仓库**: https://github.com/deng-yang-dream/directory
- **贡献指南**: ../CONTRIBUTING.md

---

**维护者**: Architect Tools Community  
**许可证**: MIT License  
**最后更新**: 2026-06-26