#!/usr/bin/env python3
"""
修复脚本：将主分类根目录中被错误放置的文件移到正确的子分类目录。
"""
import os
import re
import shutil
from collections import Counter

TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools', 'zh-cn')

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

SUBCATEGORIES = {
    '01-方案生成与概念': {'方案生成': '方案生成', '概念设计': '概念设计'},
    '02-效果图与渲染': {'AI渲染': 'AI渲染', '图像处理': '图像处理'},
    '04-AI助手与知识': {'AI助手': 'AI助手', '知识问答': '知识问答', '数据分析': '数据分析'},
    '05-汇报与数据': {'汇报输出': '汇报输出', 'PPT演示': 'PPT演示', '城市数据': '城市数据', '数据管理': '数据管理'},
    '06-绿色与性能': {'性能分析': '性能分析', '绿色建筑': '绿色建筑'},
    '07-建模与BIM': {'3D建模': '3D建模', 'BIM建模': 'BIM建模', 'BIM协同': 'BIM协同', '数据交换': '数据交换'},
}

# Files that were originally in category dirs BEFORE reclassification (from 评测数据库)
# These should stay at root level
ORIGINAL_FILES = set()

def parse_frontmatter(content):
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

def classify(scenes):
    for scene in scenes:
        if scene in SCENE_TO_CATEGORY:
            cat = SCENE_TO_CATEGORY[scene]
            sub = None
            if cat in SUBCATEGORIES and scene in SUBCATEGORIES[cat]:
                sub = SUBCATEGORIES[cat][scene]
            return cat, sub
    return None, None

def main():
    # First, collect all original files (already in category dirs before migration)
    for cat_dir in sorted(os.listdir(TOOLS_DIR)):
        cat_path = os.path.join(TOOLS_DIR, cat_dir)
        if not os.path.isdir(cat_path) or cat_dir == '10-其他':
            continue
        for item in os.listdir(cat_path):
            item_path = os.path.join(cat_path, item)
            if os.path.isfile(item_path) and item.endswith('.md'):
                ORIGINAL_FILES.add(item)

    print(f"Original files in category roots: {len(ORIGINAL_FILES)}")
    for f in sorted(ORIGINAL_FILES):
        print(f"  {f}")

    stats = Counter()
    moved = 0

    for cat_dir in sorted(os.listdir(TOOLS_DIR)):
        cat_path = os.path.join(TOOLS_DIR, cat_dir)
        if not os.path.isdir(cat_path) or cat_dir == '10-其他':
            continue

        for item in sorted(os.listdir(cat_path)):
            item_path = os.path.join(cat_path, item)
            if not os.path.isfile(item_path) or not item.endswith('.md'):
                continue

            # Skip original files that should stay at root
            if item in ORIGINAL_FILES:
                continue

            with open(item_path, 'r', encoding='utf-8') as f:
                content = f.read()

            fm = parse_frontmatter(content)
            scenes = fm.get('scenes', [])

            if not scenes:
                print(f"  SKIP {cat_dir}/{item}: no scenes")
                continue

            target_cat, sub = classify(scenes)
            if target_cat is None:
                continue

            if target_cat != cat_dir:
                print(f"  WRONG_CAT {cat_dir}/{item} -> {target_cat}")
                continue

            if sub is None:
                continue  # no subcategory needed, stays at root

            # Move to subcategory
            target_dir = os.path.join(cat_path, sub)
            os.makedirs(target_dir, exist_ok=True)
            target_path = os.path.join(target_dir, item)

            shutil.move(item_path, target_path)
            print(f"  FIX {cat_dir}/{item} -> {cat_dir}/{sub}/{item}")
            stats[f'{cat_dir}/{sub}'] += 1
            moved += 1

    # Also fix files remaining in 10-其他 with valid scenes but marked as no_scenes
    other_dir = os.path.join(TOOLS_DIR, '10-其他')
    remaining_files = [f for f in os.listdir(other_dir) if f.endswith('.md')]
    print(f"\nFiles remaining in 10-其他: {len(remaining_files)}")

    for filename in sorted(remaining_files):
        filepath = os.path.join(other_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm = parse_frontmatter(content)
        scenes = fm.get('scenes', [])
        name = fm.get('name', filename)

        if scenes:
            target_cat, sub = classify(scenes)
            if target_cat and target_cat != '10-其他':
                target_dir = os.path.join(TOOLS_DIR, target_cat)
                if sub:
                    target_dir = os.path.join(target_dir, sub)
                os.makedirs(target_dir, exist_ok=True)
                target_path = os.path.join(target_dir, filename)
                shutil.move(filepath, target_path)
                print(f"  FIX 10-其他/{filename} -> {target_cat}/{sub or ''}")
                stats[f'{target_cat}/{sub}' if sub else target_cat] += 1
                moved += 1
        else:
            print(f"  STAY 10-其他/{filename}: {name}")

    print(f"\n{'='*60}")
    print(f"Total fixes: {moved}")

if __name__ == '__main__':
    main()
