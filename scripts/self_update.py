"""self_update.py — 本技能唯一写盘通道：tmp 镜像 → compare → release → clean。

用法：
    python scripts/self_update.py report --error 描述 [--repro 复现]
    python scripts/self_update.py compare --tmp <镜像> --target <skill目录>
    python scripts/self_update.py release --tmp <镜像> --target <skill目录> [--yes]
    python scripts/self_update.py clean --tmp <镜像> [--yes]
红线：不得静默写盘（release 默认预览）；resistance/ 既有条目只增不删。
"""
from __future__ import annotations

import argparse
import filecmp
import os
import shutil
import time

import chain_store

SKIP = ("state", "updates", ".git", "__pycache__", ".kilo", ".idea", ".vscode")


def _log(entry: dict) -> None:
    """运行记录落用户缓存目录（不写进 skill）。"""
    stamp = round(time.time(), 3)
    entry["t"] = stamp
    chain_store.append("process", {"t": stamp, "step": "self_update",
                                   "status": entry.get("type", "info"),
                                   "data": entry})


def _diff(tmp: str, target: str):
    """列镜像与目标的差异（新增或内容不同）。"""
    out = []
    for dpath, dirs, files in os.walk(tmp):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for name in files:
            src = os.path.join(dpath, name)
            rel = os.path.relpath(src, tmp)
            dst = os.path.join(target, rel)
            if not os.path.exists(dst) or not filecmp.cmp(src, dst, shallow=False):
                out.append(rel)
    return out


def cmd_report(args) -> int:
    """登记一次技能错误，等待纠正流程。"""
    _log({"type": "error", "error": args.error, "repro": args.repro or ""})
    print("[自更新] 错误已登记（缓存目录），待纠正流程处理")
    return 0


def cmd_compare(args) -> int:
    """比对镜像与目标。"""
    diff = _diff(args.tmp, args.target)
    _log({"type": "compare", "diff": diff})
    print(f"[自更新] 差异 {len(diff)} 项：" + ", ".join(diff[:10]))
    return 0


def cmd_release(args) -> int:
    """比对通过后释放镜像到目标目录（默认预览）。"""
    diff = _diff(args.tmp, args.target)
    print(f"[预览] 将写入 {len(diff)} 项到 {args.target}")
    for rel in diff[:20]:
        print("  " + rel)
    if not args.yes:
        print("[预览] 未加 --yes，不写盘")
        return 0
    for rel in diff:
        src = os.path.join(args.tmp, rel)
        dst = os.path.join(args.target, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    _log({"type": "release", "to": args.target, "count": len(diff)})
    print(f"[自更新] 已释放 {len(diff)} 项")
    return 0


def cmd_clean(args) -> int:
    """释放后删除镜像目录（默认预览）。"""
    if not os.path.isdir(args.tmp):
        print("[自更新] 镜像不存在，无需清理")
        return 0
    if not args.yes:
        print(f"[预览] 将删除 {args.tmp}（加 --yes 执行）")
        return 0
    shutil.rmtree(args.tmp)
    _log({"type": "clean", "path": args.tmp})
    print(f"[自更新] 已删除 {args.tmp}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="自更新接口")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report")
    r.add_argument("--error", required=True)
    r.add_argument("--repro")
    for name in ("compare", "release", "clean"):
        s = sub.add_parser(name)
        s.add_argument("--tmp", required=True)
        if name != "clean":
            s.add_argument("--target", required=True)
        if name in ("release", "clean"):
            s.add_argument("--yes", action="store_true")
    args = ap.parse_args()
    table = {"report": cmd_report, "compare": cmd_compare,
             "release": cmd_release, "clean": cmd_clean}
    return table[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
