#!/usr/bin/env python3
"""Validate tool document format and completeness"""
import os, re, sys, json
from pathlib import Path
from datetime import datetime

TOOLS_DIR = Path(__file__).parent.parent / "tools" / "zh-cn"
REQUIRED_CATEGORIES = [
    "01-方案生成与概念", "02-效果图与渲染", "03-绘图与手绘",
    "04-AI助手与知识", "05-汇报与数据", "06-绿色与性能",
    "07-建模与BIM", "08-规范审查", "09-学术与实验室", "10-其他",
]

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
                    # Try quoted format first: ['val1', 'val2']
                    items = re.findall(r"['\"]([^'\"]+)['\"]", v)
                    if not items:
                        # Fallback: unquoted format [val1, val2]
                        inner = v[1:-1]
                        items = [s.strip() for s in inner.split(',') if s.strip()]
                    fm[k] = items
                else:
                    fm[k] = v.strip("'\"")
    return fm

def check_file(filepath):
    """Return (errors, warnings) lists"""
    errors, warnings = [], []
    rel = filepath.relative_to(TOOLS_DIR)
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [f"{rel}: cannot read - {e}"], []

    fm = parse_frontmatter(content)
    is_wiki = bool(fm.get('name'))

    if is_wiki:
        if not fm.get('scenes'):
            errors.append(f"{rel}: missing scenes field")
        if not fm.get('url'):
            warnings.append(f"{rel}: url field missing or null")
    else:
        if not re.search(r'^#\s+', content, re.MULTILINE):
            errors.append(f"{rel}: review doc missing title")

    if ' ' in filepath.name:
        errors.append(f"{rel}: filename contains spaces")

    return errors, warnings

def main():
    print("=" * 60)
    print("Tool Document Validation")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    all_errors, all_warnings = [], []
    stats = {"total": 0, "wiki": 0, "review": 0, "categories": {}}

    for cat in REQUIRED_CATEGORIES:
        cat_path = TOOLS_DIR / cat
        cat_count = 0
        if cat_path.is_dir():
            for md in cat_path.rglob("*.md"):
                stats["total"] += 1
                cat_count += 1
                content = md.read_text(encoding='utf-8')
                if parse_frontmatter(content).get('name'):
                    stats["wiki"] += 1
                else:
                    stats["review"] += 1
                errs, warns = check_file(md)
                all_errors.extend(errs)
                all_warnings.extend(warns)
        else:
            all_errors.append(f"{cat}: category dir missing")
        stats["categories"][cat] = cat_count

    print(f"\nTotal: {stats['total']} tools (Wiki {stats['wiki']} + Review {stats['review']})")
    print(f"Categories: {len(stats['categories'])}")
    for cat, count in stats["categories"].items():
        print(f"  {cat}: {count}")

    if all_errors:
        print(f"\n[ERRORS] ({len(all_errors)}):")
        for e in all_errors:
            print(f"  - {e}")

    if all_warnings:
        print(f"\n[WARNINGS] ({len(all_warnings)}):")
        for w in all_warnings[:20]:
            print(f"  - {w}")
        if len(all_warnings) > 20:
            print(f"  ... and {len(all_warnings) - 20} more")

    if not all_errors and not all_warnings:
        print("\n[OK] All files validated")

    report = {
        "timestamp": datetime.now().isoformat(),
        "stats": stats,
        "errors": len(all_errors),
        "warnings": len(all_warnings),
    }
    report_path = Path(__file__).parent.parent / "validation_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"\nReport saved: {report_path}")

    return 0 if not all_errors else 1

if __name__ == "__main__":
    sys.exit(main())
