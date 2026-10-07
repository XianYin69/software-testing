"""process_chain.py — 过程链存取：步骤留痕、中断与恢复。

用法：
    python scripts/process_chain.py save --step 收尾 [--data 摘要]
    python scripts/process_chain.py load [--tail 10]
    python scripts/process_chain.py interrupt --step 整体审查 --reason 原因
    python scripts/process_chain.py resume [--step 整体审查]
"""
from __future__ import annotations

import argparse
import time

import chain_store


def _last_interrupted(step: str | None = None) -> dict:
    """最近一条未闭合中断（可按步骤过滤）。"""
    for e in reversed(chain_store.read("process")):
        if isinstance(e, dict) and e.get("status") == "interrupted":
            if step and e.get("step") != step:
                continue
            return e
    return {}


def cmd_save(args) -> int:
    """记一步完成。"""
    chain_store.append("process", {"t": round(time.time(), 3), "step": args.step,
                                   "status": "done", "data": args.data or ""})
    print(f"[过程链] {args.step} = done")
    return 0


def cmd_load(args) -> int:
    """列最近状态并提示未闭合中断。"""
    items = chain_store.read("process")
    for e in items[-args.tail:]:
        print(f"  {e.get('t')} {e.get('step', '?')} "
              f"[{e.get('status', '?')}] {e.get('reason', '')}")
    pending = _last_interrupted()
    if pending:
        print(f"[过程链] 未处理中断：{pending.get('step')} "
              f"（{pending.get('reason')}）→ 修复后 resume")
        return 1
    print(f"[过程链] 共 {len(items)} 条，无未处理中断。")
    return 0


def cmd_interrupt(args) -> int:
    """记中断（审查失败即中断，修复后 resume 返回）。"""
    chain_store.append("process", {"t": round(time.time(), 3), "step": args.step,
                                   "status": "interrupted", "reason": args.reason})
    print(f"[过程链] 中断：{args.step} ← {args.reason}")
    return 0


def cmd_resume(args) -> int:
    """闭合最近中断（或指定步骤），回原节点继续。"""
    items = chain_store.read("process")
    for i in range(len(items) - 1, -1, -1):
        e = items[i]
        if not isinstance(e, dict) or e.get("status") != "interrupted":
            continue
        if args.step and e.get("step") != args.step:
            continue
        e["status"] = "resumed"
        e["resumed_at"] = round(time.time(), 3)
        chain_store.replace_last("process", e)
        print(f"[过程链] {e.get('step')} 中断已闭合，回该节点续推")
        return 0
    print("[过程链] 无可恢复的中断")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description="过程链存取")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("save")
    s.add_argument("--step", required=True)
    s.add_argument("--data")
    l = sub.add_parser("load")
    l.add_argument("--tail", type=int, default=10)
    i = sub.add_parser("interrupt")
    i.add_argument("--step", required=True)
    i.add_argument("--reason", required=True)
    r = sub.add_parser("resume")
    r.add_argument("--step")
    args = ap.parse_args()
    table = {"save": cmd_save, "load": cmd_load,
             "interrupt": cmd_interrupt, "resume": cmd_resume}
    return table[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
