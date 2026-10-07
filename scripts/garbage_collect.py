"""garbage_collect.py — 垃圾回收：清理 tmp 镜像与过期中间产物（默认预览）。

用法：python scripts/garbage_collect.py [--path <tmp目录>] [--age 天] [--yes]
红线：只清 tmp/缓存，绝不触碰 skill 本体与 resistance/。
"""
from __future__ import annotations

import argparse
import os
import shutil
import time

PROTECT = ("resistance", "update", "SKILL.md", "LICENSE")


def collect(root: str, age_days: float):
    """返回 (可删文件列表, 受保护跳过列表)。"""
    doomed, kept = [], []
    now = time.time()
    if not os.path.isdir(root):
        return doomed, kept
    for dpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in PROTECT]
        for name in files:
            path = os.path.join(dpath, name)
            rel = os.path.relpath(path, root)
            if rel.split(os.sep)[0] in PROTECT:
                kept.append(rel)
                continue
            if age_days <= 0 or (now - os.path.getmtime(path)) / 86400.0 >= age_days:
                doomed.append(rel)
            else:
                kept.append(rel)
    return doomed, kept


def main() -> int:
    ap = argparse.ArgumentParser(description="tmp 垃圾回收")
    ap.add_argument("--path", default=os.path.join(os.getcwd(), "tmp"))
    ap.add_argument("--age", type=float, default=0.0, help="天数阈值，0＝全部")
    ap.add_argument("--yes", action="store_true", help="确认删除（默认只预览）")
    args = ap.parse_args()
    doomed, kept = collect(args.path, args.age)
    print(f"[预览] {args.path}：候选 {len(doomed)} 项，保留 {len(kept)} 项")
    for rel in doomed[:20]:
        print("  待删 " + rel)
    if not args.yes:
        print("[预览] 未加 --yes，不落删除动作")
        return 0
    for rel in doomed:
        os.remove(os.path.join(args.path, rel))
    for dpath, dirs, files in sorted(os.walk(args.path), reverse=True):
        if not os.listdir(dpath) and os.path.basename(dpath) not in PROTECT:
            os.rmdir(dpath)
    print(f"[完成] 已删除 {len(doomed)} 项")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
