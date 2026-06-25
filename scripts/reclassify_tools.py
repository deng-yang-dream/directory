#!/usr/bin/env python3
"""
重分类脚本：将 10-其他 中的工具按 scenes 迁移到正确的主分类/子分类目录。
"""

import os
import re
import shutil
import json
from collections import Counter

TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools', 'zh-cn')

# 场景→主分类映射（优先级从上到下，取第一个匹配）
SCENE_TO_CATEGORY = {
    '方案生成': '01-方案生成与概念',
    '概念设计': '01-方案生成与概念',
    'AI渲染': '02-效果图与渲染',
    '图像处理': '02-效果图与渲染',
    '绘图': '03-绘图与手绘',
    '手绘': '03-绘图与手绘',
    'AI助手': '04-AI助手与知识',
    '知识问答': '04-AI助手与知识',
    '数据分析': '04-AI助手与知识',
    'PPT演示': '05-汇报与数据',
    '汇报输出': '05-汇报与数据',
    '城市数据': '05-汇报与数据',
    '数据管理': '05-汇报与数据',
    '绿色建筑': '06-绿色与性能',
    '性能分析': '06-绿色与性能',
    '3D建模': '07-建模与BIM',
    'BIM建模': '07-建模与BIM',
    'BIM协同': '07-建模与BIM',
    '数据交换': '07-建模与BIM',
    '施工协同': '07-建模与BIM',
    '规范审查': '08-规范审查',
    '学术与实验室': '09-学术与实验室',
    'API/服务': '10-其他',
    '文档管理': '10-其他',
}

# 子分类目录（按需创建）
SUBCATEGORIES = {
    '01-方案生成与概念': {'方案生成': '方案生成', '概念设计': '概念设计'},
    '02-效果图与渲染': {'AI渲染': 'AI渲染', '图像处理': '图像处理'},
    '04-AI助手与知识': {'AI助手': 'AI助手', '知识问答': '知识问答', '数据分析': '数据分析'},
    '05-汇报与数据': {'汇报输出': '汇报输出', 'PPT演示': 'PPT演示', '城市数据': '城市数据', '数据管理': '数据管理'},
    '06-绿色与性能': {'性能分析': '性能分析', '绿色建筑': '绿色建筑'},
    '07-建模与BIM': {'3D建模': '3D建模', 'BIM建模': 'BIM建模', 'BIM协同': 'BIM协同', '数据交换': '数据交换'},
}

def parse_frontmatter(content):
    """Extract frontmatter as dict."""
    fm = {}
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        for line in match.group(1).split('\n'):
            kv = re.match(r'(\w+):\s*(.+)', line)
            if kv:
                key, val = kv.groups()
                val = val.strip()
                # Parse list
                if val.startswith('['):
                    items = re.findall(r"['\"]([^'\"]+)['\"]", val)
                    fm[key] = items
                else:
                    fm[key] = val.strip("'\"")
    return fm

def classify(scenes):
    """Return (category_dir, subcategory_name) for given scenes list."""
    for scene in scenes:
        if scene in SCENE_TO_CATEGORY:
            cat = SCENE_TO_CATEGORY[scene]
            sub = None
            if cat in SUBCATEGORIES and scene in SUBCATEGORIES[cat]:
                sub = SUBCATEGORIES[cat][scene]
            return cat, sub
    return '10-其他', None

def main():
    source_dir = os.path.join(TOOLS_DIR, '10-其他')
    files = sorted(os.listdir(source_dir))
    stats = Counter()
    moved = 0
    errors = []

    for filename in files:
        if not filename.endswith('.md'):
            continue

        filepath = os.path.join(source_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm = parse_frontmatter(content)
        scenes = fm.get('scenes', [])

        if not scenes:
            print(f"  SKIP {filename}: no scenes field")
            stats['no_scenes'] += 1
            continue

        category, subcategory = classify(scenes)

        # Target path
        if subcategory:
            target_dir = os.path.join(TOOLS_DIR, category, subcategory)
        else:
            target_dir = os.path.join(TOOLS_DIR, category)

        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, filename)

        # Move file
        shutil.move(filepath, target_path)
        print(f"  {filename}: {', '.join(scenes)} -> {category}/{subcategory or '.'}")
        stats[f'{category}/{subcategory}' if subcategory else category] += 1
        moved += 1

    print(f"\n{'='*60}")
    print(f"Total moved: {moved}")
    remaining = len([f for f in os.listdir(source_dir) if f.endswith('.md')])
    print(f"Files remaining in 10-其他: {remaining}")
    print(f"\nCategory distribution:")
    for k, v in stats.most_common():
        print(f"  {k}: {v}")

    if errors:
        print(f"\nErrors:")
        for e in errors:
            print(f"  {e}")

    # Write stats JSON
    stats_json = {}
    for cat in sorted(os.listdir(TOOLS_DIR)):
        cat_path = os.path.join(TOOLS_DIR, cat)
        if os.path.isdir(cat_path) and cat != '10-其他':
            total = 0
            subs = {}
            for item in sorted(os.listdir(cat_path)):
                item_path = os.path.join(cat_path, item)
                if os.path.isdir(item_path):
                    count = len([f for f in os.listdir(item_path) if f.endswith('.md')])
                    subs[item] = count
                    total += count
                elif item.endswith('.md'):
                    total += 1
            stats_json[cat] = {'total': total, 'subcategories': subs} if subs else {'total': total}

    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    stats_path = os.path.join(scripts_dir, '..', 'tools', 'classification_stats.json')
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats_json, f, ensure_ascii=False, indent=2)

    print(f"\nStats written to tools/classification_stats.json")

if __name__ == '__main__':
    main()
