"""check_len.py — 校验 markdown 文本 ≤50 行（脚本 .py/.ps1/.sh/.cmd 不受此限）。

用法：python scripts/check_len.py [--root <目录>] [--limit 50]
"""
from __future__ import annotations

import argparse
import os

SKIP_DIRS = {".git", "tmp", "__pycache__", ".kilo", ".idea", ".vscode"}


def iter_md(root: str):
    """遍历 root 下的 .md 文件。"""
    for dpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if name.endswith(".md"):
                yield os.path.join(dpath, name)


def overlong(root: str, limit: int):
    """返回超限文件：(相对路径, 行数)。"""
    out = []
    for path in iter_md(root):
        with open(path, encoding="utf-8", errors="replace") as handle:
            lines = handle.read().splitlines()
        if len(lines) > limit:
            out.append((os.path.relpath(path, root), len(lines)))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="markdown 行数红线校验")
    ap.add_argument("--root", default=os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--limit", type=int, default=50)
    args = ap.parse_args()
    bad = overlong(args.root, args.limit)
    if bad:
        print(f"{len(bad)} 个 .md 超过 {args.limit} 行：")
        for rel, n in bad:
            print(f"  {rel}: {n} 行")
        return 1
    print(f"全部 .md ≤{args.limit} 行，校验通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
