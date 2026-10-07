"""sandbox.py — 未指定目标目录时在固定路径建沙盒作业（默认预览）。

用法：python scripts/sandbox.py create [--name 名] [--yes]
      python scripts/sandbox.py where
      python scripts/sandbox.py remove --path <沙盒> [--yes]
沙盒位置：%LOCALAPPDATA%\\SMS\\sandbox\\software-testing\\<name>
交付：复制到用户指定目标后再 remove。
"""
from __future__ import annotations

import argparse
import os
import shutil


def base() -> str:
    """沙盒根目录（用户缓存区，不入 skill 目录）。"""
    root = os.environ.get("SMS_HOME")
    if not root:
        local = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
        root = os.path.join(local, "SMS")
    return os.path.join(root, "sandbox", "software-testing")


def cmd_create(args) -> int:
    """建沙盒工作区。"""
    path = os.path.join(base(), args.name)
    print(f"[预览] 将创建 {path}（含 tmp/mirror）")
    if not args.yes:
        print("[预览] 未加 --yes，不建目录")
        return 0
    for sub in ("mirror", "tmp"):
        os.makedirs(os.path.join(path, sub), exist_ok=True)
    print(f"[沙盒] 就绪：{path}")
    return 0


def cmd_where(_args) -> int:
    """列现有沙盒。"""
    root = base()
    if not os.path.isdir(root):
        print(f"[沙盒] 无（根目录 {root} 不存在）")
        return 0
    for name in sorted(os.listdir(root)):
        print(os.path.join(root, name))
    return 0


def cmd_remove(args) -> int:
    """删除沙盒（交付后执行）。"""
    print(f"[预览] 将删除 {args.path}")
    if not args.yes:
        print("[预览] 未加 --yes，不删除")
        return 0
    if os.path.isdir(args.path):
        shutil.rmtree(args.path)
        print("[沙盒] 已删除")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="固定路径沙盒")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("create")
    c.add_argument("--name", default="work")
    c.add_argument("--yes", action="store_true")
    sub.add_parser("where")
    r = sub.add_parser("remove")
    r.add_argument("--path", required=True)
    r.add_argument("--yes", action="store_true")
    args = ap.parse_args()
    table = {"create": cmd_create, "where": cmd_where, "remove": cmd_remove}
    return table[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
