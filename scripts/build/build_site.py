#!/usr/bin/env python3
"""
构建静态网站 — 将工具目录转换为可搜索的 HTML 网站。
支持有 frontmatter 的 Wiki 文档和无 frontmatter 的评测文档。
"""

import json
import re
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
TOOLS_DIR = BASE_DIR / "tools" / "zh-cn"
OUTPUT_DIR = BASE_DIR / "docs"

def ensure_dirs():
    for d in [OUTPUT_DIR, OUTPUT_DIR / "css", OUTPUT_DIR / "js"]:
        d.mkdir(exist_ok=True)

def parse_frontmatter(content):
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if m:
        for line in m.group(1).split('\n'):
            kv = re.match(r'(\w+):\s*(.+)', line)
            if kv:
                k, v = kv.groups()
                v = v.strip()
                if v.startswith('['):
                    items = re.findall(r"['\"]([^'\"]+)['\"]", v)
                    if not items:
                        inner = v[1:-1]
                        items = [s.strip() for s in inner.split(',') if s.strip()]
                    fm[k] = items
                else:
                    fm[k] = v.strip("'\"")
    return fm

def extract_name_from_body(content):
    m = re.search(r'^#\s+(.+?)(?:\n|$)', content, re.MULTILINE)
    if m:
        return re.sub(r'[（(][^)）]*[)）]', '', m.group(1)).strip()
    return None

def process_tool_file(md_file, category, subcategory=None):
    try:
        content = md_file.read_text(encoding='utf-8')
        fm = parse_frontmatter(content)

        has_fm = bool(fm.get('name'))
        if has_fm:
            name = fm.get('name')
            scenes = fm.get('scenes', [])
            design_stages = fm.get('design_stages', [])
            url = fm.get('url')
            developer = fm.get('developer')
            pricing = fm.get('pricing_model')
            rating = fm.get('rating')
            body = content.split('---', 2)[-1] if '---' in content else content
        else:
            name = extract_name_from_body(content)
            if not name:
                return None
            scenes, design_stages, url, developer, pricing, rating = [], [], None, None, None, None
            body = content

        m = re.search(r'^# .+?\n\n(.+?)(?:\n|$)', body, re.DOTALL)
        desc = m.group(1).strip()[:300] if m else ""

        return {
            "id": md_file.stem,
            "name": name,
            "category": category,
            "subcategory": subcategory,
            "url": url,
            "developer": developer,
            "scenes": scenes,
            "design_stages": design_stages,
            "pricing": pricing,
            "rating": rating,
            "description": desc,
            "filename": md_file.name,
            "_has_frontmatter": has_fm
        }
    except Exception as e:
        print(f"  SKIP {md_file.name}: {e}")
        return None

def collect_tools():
    tools, categories = [], {}
    for cat_dir in sorted(TOOLS_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        cat_name = cat_dir.name
        cat_tools = []
        for item in sorted(cat_dir.iterdir()):
            if item.is_dir():
                for md in item.glob("*.md"):
                    t = process_tool_file(md, cat_name, item.name)
                    if t:
                        cat_tools.append(t)
            elif item.suffix == ".md":
                t = process_tool_file(item, cat_name)
                if t:
                    cat_tools.append(t)
        if cat_tools:
            categories[cat_name] = {"name": cat_name, "tools": cat_tools, "count": len(cat_tools)}
            tools.extend(cat_tools)
    return tools, categories

# ── HTML generators ──────────────────────────────────────────

CATEGORY_LABELS = {
    "01-方案生成与概念": "方案生成与概念",
    "02-效果图与渲染": "效果图与渲染",
    "03-绘图与手绘": "绘图与手绘",
    "04-AI助手与知识": "AI助手与知识",
    "05-汇报与数据": "汇报与数据",
    "06-绿色与性能": "绿色与性能",
    "07-建模与BIM": "建模与BIM",
    "08-规范审查": "规范审查",
    "09-学术与实验室": "学术与实验室",
    "10-其他": "其他",
}

def tool_card(t):
    scenes_html = "".join(f'<span class="tag">{s}</span>' for s in t["scenes"][:3])
    sub = f'<span class="subcat">{t["subcategory"]}</span>' if t["subcategory"] else ""
    rating = f'<span class="rating">{"★" * int(t["rating"])}</span>' if t.get("rating") else ""
    dev = t.get("developer") or ""
    price = t.get("pricing") or ""
    desc = t.get("description", "")[:200]
    url = t.get("url") or ""
    name_html = f'<a href="{url}" target="_blank" rel="noopener">{t["name"]}</a>' if url else t["name"]

    return f"""
    <div class="tool-card" data-category="{t['category']}" data-scenes="{','.join(t['scenes'])}">
        <div class="tool-header">
            <span class="tool-name">{name_html}</span>
            {rating}
        </div>
        <div class="tool-meta">{sub} {scenes_html} <span class="dev">{dev}</span> <span class="price">{price}</span></div>
        <p class="tool-desc">{desc}</p>
    </div>"""

def build_html(tools, categories):
    cat_nav = ""
    for cid, cinfo in categories.items():
        label = CATEGORY_LABELS.get(cid, cid)
        cat_nav += f'<button class="cat-btn" data-cat="{cid}">{label} <span class="count">{cinfo["count"]}</span></button>\n'

    cards = "\n".join(tool_card(t) for t in tools)

    wiki_count = sum(1 for t in tools if t.get("_has_frontmatter"))
    review_count = len(tools) - wiki_count
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>建筑师 AI 工具目录</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background:#f5f5f5; color:#333; }}
header {{ background:#1a1a2e; color:white; padding:24px 32px; }}
header h1 {{ font-size:1.5rem; }}
header p {{ color:#aaa; margin-top:4px; }}
.stats-bar {{ display:flex; gap:24px; padding:16px 32px; background:#16213e; color:#ccc; font-size:.85rem; }}
.stats-bar strong {{ color:white; }}
.container {{ max-width:1400px; margin:0 auto; padding:24px; }}
.cat-nav {{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:24px; }}
.cat-btn {{ padding:8px 16px; border:1px solid #ddd; border-radius:20px; background:white; cursor:pointer; font-size:.85rem; transition:all .2s; }}
.cat-btn:hover, .cat-btn.active {{ background:#1a1a2e; color:white; border-color:#1a1a2e; }}
.cat-btn .count {{ font-size:.75rem; color:#999; }}
.cat-btn.active .count {{ color:#aaa; }}
.tool-grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(380px, 1fr)); gap:16px; }}
.tool-card {{ background:white; border-radius:8px; padding:16px; border:1px solid #eee; transition:box-shadow .2s; }}
.tool-card:hover {{ box-shadow:0 4px 16px rgba(0,0,0,.08); }}
.tool-card.hidden {{ display:none; }}
.tool-header {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; }}
.tool-name {{ font-weight:600; }}
.tool-name a {{ color:#1a1a2e; text-decoration:none; }}
.tool-name a:hover {{ text-decoration:underline; }}
.tool-meta {{ display:flex; flex-wrap:wrap; gap:4px; align-items:center; margin-bottom:8px; font-size:.8rem; }}
.tag {{ background:#e8f4fd; color:#1976d2; padding:2px 8px; border-radius:10px; font-size:.75rem; }}
.subcat {{ background:#f3e5f5; color:#7b1fa2; padding:2px 8px; border-radius:10px; font-size:.75rem; }}
.dev {{ color:#666; }}
.price {{ color:#888; font-size:.75rem; }}
.rating {{ color:#f39c12; font-size:.85rem; }}
.tool-desc {{ font-size:.85rem; color:#555; line-height:1.5; }}
.search-box {{ width:100%; padding:12px 16px; border:1px solid #ddd; border-radius:8px; font-size:1rem; margin-bottom:16px; }}
.search-box:focus {{ outline:none; border-color:#1a1a2e; }}
.no-results {{ display:none; text-align:center; padding:48px; color:#999; }}
footer {{ text-align:center; color:#999; padding:32px; font-size:.85rem; }}
footer a {{ color:#666; }}
@media (max-width:768px) {{ .tool-grid {{ grid-template-columns:1fr; }} .stats-bar {{ flex-direction:column; gap:8px; }} }}
</style>
</head>
<body>
<header>
    <h1>建筑师 AI 工具目录</h1>
    <p>从海量 AI 工具中筛选出真正对建筑师有用的 — 告诉你怎么选、什么时候用、为什么</p>
</header>
<div class="stats-bar">
    <span>工具总数: <strong>{len(tools)}</strong></span>
    <span>Wiki 工具: <strong>{wiki_count}</strong></span>
    <span>评测文档: <strong>{review_count}</strong></span>
    <span>分类: <strong>{len(categories)}</strong> 个</span>
    <span>更新: <strong>{now}</strong></span>
</div>
<div class="container">
    <input type="text" class="search-box" id="search" placeholder="搜索工具名称、开发者、场景标签...">
    <div class="cat-nav">
        <button class="cat-btn active" data-cat="all">全部 <span class="count">{len(tools)}</span></button>
        {cat_nav}
    </div>
    <div class="tool-grid" id="toolGrid">
        {cards}
    </div>
    <div class="no-results" id="noResults">没有匹配的工具</div>
</div>
<footer>
    <p>建筑师 AI 工具目录 · <a href="https://github.com/deng-yang-dream/directory">GitHub</a> · MIT License</p>
    <p>构建时间: {now}</p>
</footer>
<script>
const search = document.getElementById('search');
const grid = document.getElementById('toolGrid');
const cards = grid.querySelectorAll('.tool-card');
const catBtns = document.querySelectorAll('.cat-btn');
const noResults = document.getElementById('noResults');
let activeCat = 'all';

function filter() {{
    const q = search.value.toLowerCase();
    let visible = 0;
    cards.forEach(c => {{
        const matchCat = activeCat === 'all' || c.dataset.category === activeCat;
        const text = c.textContent.toLowerCase();
        const matchSearch = !q || text.includes(q);
        if (matchCat && matchSearch) {{ c.classList.remove('hidden'); visible++; }}
        else {{ c.classList.add('hidden'); }}
    }});
    noResults.style.display = visible === 0 ? 'block' : 'none';
}}

search.addEventListener('input', filter);

catBtns.forEach(btn => {{
    btn.addEventListener('click', () => {{
        catBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeCat = btn.dataset.cat;
        filter();
    }});
}});
</script>
</body>
</html>"""

def main():
    print("Building static site...")
    ensure_dirs()
    tools, categories = collect_tools()
    print(f"  {len(tools)} tools in {len(categories)} categories")

    html = build_html(tools, categories)
    (OUTPUT_DIR / "index.html").write_text(html, encoding='utf-8')
    print(f"  -> {OUTPUT_DIR / 'index.html'}")

    data = {
        "updated": datetime.now().isoformat(),
        "total": len(tools),
        "categories": {k: {"name": v["name"], "count": v["count"]} for k, v in categories.items()},
        "tools": tools
    }
    (OUTPUT_DIR / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"  -> {OUTPUT_DIR / 'data.json'}")
    print("Done.")

if __name__ == "__main__":
    main()
