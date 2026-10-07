"""lint_deps.py — 校验 dependence/deps.json：每条依赖必附原始链接 source_url。

用法：python scripts/lint_deps.py [--root <skill目录>]
本地技能 source_url 形如 local://<skill-id>；缺字段即判不合格并退出码 1。
"""
from __future__ import annotations

import argparse
import json
import os
import sys

REQUIRED = ("name", "source_url", "license", "version", "install", "checked_at")
SCHEMES = ("http://", "https://", "local://", "file://")


def load_deps(path: str):
    """读 deps.json，返回 (条目列表, 错误列表)。"""
    if not os.path.exists(path):
        return None, [f"{path}: 缺失（每条依赖须登记 deps.json）"]
    try:
        with open(path, encoding="utf-8-sig") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        return None, [f"{path}: JSON 解析失败 {exc}"]
    if isinstance(data, dict):
        data = data.get("dependencies") or data.get("deps") or []
    if not isinstance(data, list):
        return None, [f"{path}: 顶层须为数组或 {dependencies:[...]}"]
    return data, []


def lint(root: str):
    """返回错误列表（空＝合格）。"""
    path = os.path.join(root, "dependence", "deps.json")
    deps, errs = load_deps(path)
    if deps is None:
        return errs
    for i, entry in enumerate(deps):
        name = entry.get("name", "?") if isinstance(entry, dict) else "?"
        tag = f"deps.json[{i}] {name}"
        if not isinstance(entry, dict):
            errs.append(f"{tag}: 条目须为对象")
            continue
        for key in REQUIRED:
            if key not in entry:
                errs.append(f"{tag}: 缺字段 {key}")
        url = (entry.get("source_url") or "").strip()
        if not url:
            errs.append(f"{tag}: 缺 source_url（原始链接·缺即不合格）")
        elif not url.startswith(SCHEMES):
            errs.append(f"{tag}: source_url 非原始链接 {url}")
        status = entry.get("source_url_status")
        if status not in (None, "verified", "unverified"):
            errs.append(f"{tag}: source_url_status 仅 verified/unverified")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description="依赖原始链接 lint")
    ap.add_argument("--root", default=os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()
    errs = lint(args.root)
    if errs:
        print(f"依赖 lint 不合格（{len(errs)} 项）：")
        for line in errs:
            print("  " + line)
        return 1
    print("依赖 lint 通过：每条依赖均附 source_url 原始链接。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
