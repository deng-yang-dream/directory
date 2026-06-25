#!/usr/bin/env python3
"""
构建静态网站 - 将工具目录转换为 HTML 网站
"""

import os
import json
import yaml
import re
from pathlib import Path
from datetime import datetime

# 配置
BASE_DIR = Path(__file__).parent.parent.parent
TOOLS_DIR = BASE_DIR / "tools" / "zh-cn"
OUTPUT_DIR = BASE_DIR / "docs"
TEMPLATE_DIR = BASE_DIR / "scripts" / "build" / "templates"

def ensure_dirs():
    """确保必要的目录存在"""
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "css").mkdir(exist_ok=True)
    (OUTPUT_DIR / "js").mkdir(exist_ok=True)

def parse_frontmatter(content):
    """解析 frontmatter 元数据"""
    fm = {}
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        for line in match.group(1).split('\n'):
            kv = re.match(r'(\w+):\s*(.+)', line)
            if kv:
                key, val = kv.groups()
                val = val.strip()
                if val.startswith('['):
                    items = re.findall(r"['\"]([^'\"]+)['\"]", val)
                    fm[key] = items
                else:
                    fm[key] = val.strip("'\"")
    return fm

def collect_tools():
    """收集所有工具信息"""
    tools = []
    categories = {}

    for category_dir in sorted(TOOLS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue

        category_name = category_dir.name
        category_tools = []

        # 检查子分类
        for item in sorted(category_dir.iterdir()):
            if item.is_dir():
                # 子分类目录
                subcategory = item.name
                for md_file in item.glob("*.md"):
                    tool = process_tool_file(md_file, category_name, subcategory)
                    if tool:
                        category_tools.append(tool)
            elif item.suffix == ".md":
                # 根目录下的文件
                tool = process_tool_file(item, category_name)
                if tool:
                    category_tools.append(tool)

        if category_tools:
            categories[category_name] = {
                "name": category_name,
                "tools": category_tools,
                "count": len(category_tools)
            }
            tools.extend(category_tools)

    return tools, categories

def process_tool_file(md_file, category, subcategory=None):
    """处理单个工具文件"""
    try:
        content = md_file.read_text(encoding='utf-8')
        fm = parse_frontmatter(content)

        if not fm.get('name'):
            return None

        # 提取工具描述（第一段非 frontmatter 内容）
        body = content.split('---', 2)[-1] if '---' in content else content
        first_para = re.search(r'^# .+?\n\n(.+?)(?:\n\n|$)', body, re.DOTALL)
        description = first_para.group(1).strip() if first_para else ""

        tool = {
            "id": md_file.stem,
            "name": fm.get('name', md_file.stem),
            "category": category,
            "subcategory": subcategory,
            "url": fm.get('url'),
            "developer": fm.get('developer'),
            "scenes": fm.get('scenes', []),
            "design_stages": fm.get('design_stages', []),
            "pricing_model": fm.get('pricing_model'),
            "rating": fm.get('rating'),
            "description": description,
            "file_path": str(md_file.relative_to(BASE_DIR)),
            "filename": md_file.name
        }
        return tool
    except Exception as e:
        print(f"处理文件 {md_file} 时出错: {e}")
        return None

def generate_index_html(tools, categories):
    """生成首页"""
    template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>建筑师 AI 工具目录</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { margin-bottom: 40px; }
        h1 { color: #333; }
        .stats { background: #f5f5f5; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
        .categories { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .category { border: 1px solid #ddd; border-radius: 8px; padding: 20px; }
        .category h3 { margin-top: 0; }
        .tools { margin-top: 40px; }
        .tool { border-bottom: 1px solid #eee; padding: 10px 0; }
        .tool-name { font-weight: bold; }
        .tool-meta { color: #666; font-size: 0.9em; }
        footer { margin-top: 40px; text-align: center; color: #888; }
    </style>
</head>
<body>
    <header>
        <h1>🏗️ 建筑师 AI 工具目录</h1>
        <p>收录 {{ total_tools }} 个对建筑师有用的 AI 工具，按场景分类整理</p>
    </header>

    <div class="stats">
        <h2>📊 统计信息</h2>
        <p>总工具数: {{ total_tools }} | 最后更新: {{ last_updated }}</p>
        <p>数据来源: Wiki工具 {{ wiki_count }} + 评测数据库 {{ review_count }}</p>
    </div>

    <div class="categories">
        {% for cat_id, cat in categories.items() %}
        <div class="category">
            <h3>{{ cat_id }} ({{ cat.count }}个工具)</h3>
            <ul>
                {% for tool in cat.tools[:5] %}
                <li><a href="#{{ tool.id }}">{{ tool.name }}</a></li>
                {% endfor %}
                {% if cat.count > 5 %}
                <li>... 还有 {{ cat.count - 5 }} 个工具</li>
                {% endif %}
            </ul>
        </div>
        {% endfor %}
    </div>

    <div class="tools">
        <h2>所有工具</h2>
        {% for tool in tools %}
        <div class="tool" id="{{ tool.id }}">
            <div class="tool-name">{{ tool.name }}</div>
            <div class="tool-meta">
                分类: {{ tool.category }}{% if tool.subcategory %} / {{ tool.subcategory }}{% endif %} |
                场景: {{ ', '.join(tool.scenes) }} |
                开发者: {{ tool.developer }}
            </div>
            {% if tool.description %}
            <p>{{ tool.description[:200] }}{% if tool.description|length > 200 %}...{% endif %}</p>
            {% endif %}
        </div>
        {% endfor %}
    </div>

    <footer>
        <p>项目开源地址: <a href="https://github.com/deng-yang-dream/directory">GitHub</a></p>
        <p>最后构建时间: {{ build_time }}</p>
    </footer>
</body>
</html>
"""

    # 简单统计
    total_tools = len(tools)
    wiki_count = sum(1 for t in tools if "wiki" in t.get("file_path", "").lower())
    review_count = total_tools - wiki_count

    # 渲染模板
    html = template.replace("{{ total_tools }}", str(total_tools)) \
                   .replace("{{ wiki_count }}", str(wiki_count)) \
                   .replace("{{ review_count }}", str(review_count)) \
                   .replace("{{ last_updated }}", datetime.now().strftime("%Y-%m-%d")) \
                   .replace("{{ build_time }}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # 简单替换 categories 和 tools（实际应该用模板引擎）
    import json
    html = html.replace("{{ categories.items() }}", "categories")

    # 保存
    (OUTPUT_DIR / "index.html").write_text(html, encoding='utf-8')
    print(f"生成首页: {OUTPUT_DIR / 'index.html'}")

def generate_tools_json(tools, categories):
    """生成工具数据 JSON 文件"""
    data = {
        "metadata": {
            "total_tools": len(tools),
            "last_updated": datetime.now().isoformat(),
            "categories_count": len(categories)
        },
        "categories": categories,
        "tools": tools
    }

    (OUTPUT_DIR / "data.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    print(f"生成数据文件: {OUTPUT_DIR / 'data.json'}")

def generate_css():
    """生成基础 CSS"""
    css = """
/* 基础样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f9fa;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    margin-bottom: 40px;
    padding-bottom: 20px;
    border-bottom: 1px solid #dee2e6;
}

h1 {
    color: #212529;
    margin-bottom: 10px;
}

.stats {
    background: #e9ecef;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 30px;
}

.categories {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
}

.category {
    background: white;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 20px;
    transition: box-shadow 0.2s;
}

.category:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.category h3 {
    margin-top: 0;
    color: #495057;
    border-bottom: 1px solid #e9ecef;
    padding-bottom: 10px;
}

.tools {
    background: white;
    border-radius: 8px;
    padding: 20px;
    margin-top: 20px;
}

.tool {
    border-bottom: 1px solid #e9ecef;
    padding: 15px 0;
}

.tool:last-child {
    border-bottom: none;
}

.tool-name {
    font-weight: 600;
    color: #212529;
    margin-bottom: 5px;
}

.tool-name a {
    color: inherit;
    text-decoration: none;
}

.tool-name a:hover {
    text-decoration: underline;
}

.tool-meta {
    color: #6c757d;
    font-size: 0.9em;
    margin-bottom: 8px;
}

footer {
    margin-top: 40px;
    text-align: center;
    color: #6c757d;
    font-size: 0.9em;
    padding-top: 20px;
    border-top: 1px solid #dee2e6;
}

@media (max-width: 768px) {
    .categories {
        grid-template-columns: 1fr;
    }

    body {
        padding: 15px;
    }
}
"""

    (OUTPUT_DIR / "css" / "style.css").write_text(css, encoding='utf-8')
    print(f"生成 CSS 文件: {OUTPUT_DIR / 'css' / 'style.css'}")

def main():
    """主函数"""
    print("开始构建静态网站...")

    ensure_dirs()

    print("收集工具信息...")
    tools, categories = collect_tools()

    print(f"找到 {len(tools)} 个工具，{len(categories)} 个分类")

    print("生成网站文件...")
    generate_css()
    generate_index_html(tools, categories)
    generate_tools_json(tools, categories)

    print("构建完成！")

if __name__ == "__main__":
    main()
