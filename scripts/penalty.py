"""penalty.py — 惩罚计数与熔断（重试达 10 次强制回退或求助用户）。

用法：python scripts/penalty.py hit --target 整体审查 [--reason 说明]
      python scripts/penalty.py reset --target 整体审查
      python scripts/penalty.py status
"""
from __future__ import annotations

import argparse
import os
import time

import chain_store

LIMIT = 10


def _counts() -> dict:
    """汇总各 target 当前计数（取最近一条）。"""
    latest = {}
    for e in chain_store.read("penalty"):
        if isinstance(e, dict) and "target" in e:
            latest[e["target"]] = e.get("count", 0)
    return latest


def cmd_hit(args) -> int:
    """计数一次；达上限即熔断（退出码 2）。"""
    count = _counts().get(args.target, 0) + 1
    chain_store.append("penalty", {"t": round(time.time(), 3), "target": args.target,
                                   "count": count, "reason": args.reason or ""})
    print(f"[惩罚] {args.target} 第 {count}/{LIMIT} 次")
    if count >= LIMIT:
        print("[熔断] 达上限：停止原做法，回退功能分支或 ask_user 求助用户")
        return 2
    return 0


def cmd_reset(args) -> int:
    """清零（仅在校验通过后使用）。"""
    chain_store.append("penalty", {"t": round(time.time(), 3), "target": args.target,
                                   "count": 0, "reason": "reset"})
    print(f"[惩罚] {args.target} 计数清零")
    return 0


def cmd_status(_args) -> int:
    """列出现状。"""
    data = _counts()
    if not data:
        print("[惩罚] 无计数记录")
        return 0
    path = chain_store.chain_path("penalty")
    print(f"[惩罚] 状态文件：{path}（缓存目录，不入 skill）")
    for target, count in sorted(data.items()):
        flag = "（已熔断）" if count >= LIMIT else ""
        print(f"  {target}: {count}/{LIMIT}{flag}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="惩罚计数与熔断")
    sub = ap.add_subparsers(dest="cmd", required=True)
    h = sub.add_parser("hit")
    h.add_argument("--target", required=True)
    h.add_argument("--reason")
    r = sub.add_parser("reset")
    r.add_argument("--target", required=True)
    sub.add_parser("status")
    args = ap.parse_args()
    if os.environ.get("DRY_RUN"):
        print("[惩罚] 预览模式不落盘")
        return 0
    return {"hit": cmd_hit, "reset": cmd_reset, "status": cmd_status}[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
