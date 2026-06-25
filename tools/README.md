# 工具目录索引

## 📊 统计信息
- **总工具数**: 0
- **Wiki工具**: 0
- **评测工具**: 0
- **最后更新**: 2026-06-25

## 📁 目录结构

### 中文文档 (zh-cn)
```
tools/zh-cn/
├── 01-方案生成与概念/     # 方案生成、概念设计
├── 02-效果图与渲染/       # AI渲染、图像生成
├── 03-绘图与手绘/         # 绘图、手绘工具
├── 04-AI助手与知识/       # AI助手、知识问答
├── 05-汇报与数据/         # 汇报输出、PPT演示
├── 06-绿色与性能/         # 绿色建筑、性能分析
├── 07-建模与BIM/          # 3D建模、BIM工具
├── 08-规范审查/           # 规范检查、合规审查
├── 09-学术与实验室/       # 学术机构、AI实验室
└── 10-其他/              # 其他工具、通用工具
```

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
根据工具的主要功能选择适当的分类目录。

### 2. 创建工具文件
```bash
# 中文文档
touch tools/zh-cn/分类目录/工具名称.md

# 英文文档
touch tools/en/category-directory/tool-name.md
```

### 3. 使用标准格式
参考现有工具文件的格式，包含：
- Frontmatter 元数据
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
1. 按分类目录浏览
2. 使用网站搜索功能
3. 查看工具索引文件

## 🆘 问题反馈
如果在使用工具目录时遇到问题，请：
1. 检查文件命名和格式
2. 查看现有工具示例
3. 在GitHub Issues中报告问题
