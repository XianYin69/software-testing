"""logic_chain.py — 逻辑链（决策留痕）与正反双链辩论，状态落用户缓存目录。

用法：
    python scripts/logic_chain.py add --from A --to B --why 理由 [--skill 名]
    python scripts/logic_chain.py debate --claim 论断 --pro p1 --pro p2 --con c1
    python scripts/logic_chain.py verify [--skill 名]
"""
from __future__ import annotations

import argparse
import json
import os
import time

import chain_store


def cmd_add(args) -> int:
    """追加一条 frm→to 决策。"""
    entry = {"t": round(time.time(), 3), "frm": args.frm, "to": args.to,
             "why": args.why}
    chain_store.append("logic", entry, skill=args.skill)
    print(f"[逻辑链] {args.frm} → {args.to}（{args.why}）")
    return 0


def cmd_debate(args) -> int:
    """正反双链辩论：列论据、记 verdict（裁决仅供参考）。"""
    pros = list(args.pro or [])
    cons = list(args.con or [])
    if not pros or not cons:
        print("[辩论] 正反论据均不得为空（各至少一条）")
        return 1
    entry = {"t": round(time.time(), 3), "type": "debate", "claim": args.claim,
             "pro": pros, "con": cons, "verdict": args.verdict or "未裁决"}
    chain_store.append("logic", entry, skill=args.skill)
    print(f"[辩论] 论断：{args.claim}")
    print("  正方：" + " / ".join(pros))
    print("  反方：" + " / ".join(cons))
    print(f"  verdict：{entry['verdict']}（仅供参考，终裁在执行者）")
    return 0


def cmd_verify(args) -> int:
    """检查链文件可读且条目齐全。"""
    items = chain_store.read("logic", skill=args.skill)
    broken = [i for i, e in enumerate(items)
              if not isinstance(e, dict) or "t" not in e]
    if broken:
        print(f"[校验] {len(broken)} 条格式异常：{broken[:5]}")
        return 1
    print(f"[校验] 逻辑链 {len(items)} 条，格式合格。")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="逻辑链与双链辩论")
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = {"skill": dict(default="software-testing")}
    a = sub.add_parser("add")
    a.add_argument("--from", dest="frm", required=True)
    a.add_argument("--to", required=True)
    a.add_argument("--why", required=True)
    a.add_argument("--skill", **common["skill"])
    d = sub.add_parser("debate")
    d.add_argument("--claim", required=True)
    d.add_argument("--pro", action="append")
    d.add_argument("--con", action="append")
    d.add_argument("--verdict")
    d.add_argument("--skill", **common["skill"])
    v = sub.add_parser("verify")
    v.add_argument("--skill", **common["skill"])
    args = ap.parse_args()
    return {"add": cmd_add, "debate": cmd_debate, "verify": cmd_verify}[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
