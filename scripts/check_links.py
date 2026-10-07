"""check_links.py — 扫描本技能全部 markdown，校验相对链接目标存在（悬空链接须为 0）。

用法：python scripts/check_links.py [--root <目录>]
"""
from __future__ import annotations

import argparse
import os
import re

SKIP_DIRS = {".git", "tmp", "__pycache__", ".kilo", ".idea", ".vscode"}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def iter_md(root: str):
    """遍历 root 下的 .md 文件（跳过缓存与临时目录）。"""
    for dpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if name.endswith(".md"):
                yield os.path.join(dpath, name)


def dangling(root: str):
    """返回悬空链接列表：(相对文件, 链接目标)。"""
    bad = []
    for path in iter_md(root):
        with open(path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        for _, target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#", "local://")):
                continue
            if "://" in target:
                continue
            rel = target.split("#", 1)[0]
            if not rel:
                continue
            full = os.path.normpath(os.path.join(os.path.dirname(path), rel))
            if not os.path.exists(full):
                bad.append((os.path.relpath(path, root), target))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description="悬空链接校验")
    ap.add_argument("--root", default=os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()
    bad = dangling(args.root)
    if bad:
        print(f"发现 {len(bad)} 个悬空链接：")
        for src, target in bad:
            print(f"  {src} -> {target}")
        return 1
    print("悬空链接为 0，校验通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
