"""context_compress.py — 长文本压缩为摘要卡片（问题/判据/动作），供跨步骤流转。

用法：python scripts/context_compress.py --file <文本> [--chars 400] [--out <卡片.md>]
本技能不接外部模型：按句切分取关键句＋首尾句，产出结构化卡片，人工复核后入链。
"""
from __future__ import annotations

import argparse
import os
import re

SENT_SPLIT = re.compile(r"(?<=[。；;！？!?])\s*")
KEY_MARK = re.compile(r"(必须|禁止|不得|因此|结论|判据|原因|失败|通过)")


def sentences(text: str):
    """切句（去空）。"""
    parts = [s.strip() for s in SENT_SPLIT.split(text) if s.strip()]
    return parts


def pick(parts, limit: int):
    """挑关键句：命中关键词者优先，保留原序，总量受 limit 字符约束。"""
    key = [p for p in parts if KEY_MARK.search(p)]
    if not key:
        key = parts[:1] + parts[-1:]
    out, used = [], 0
    for p in key:
        if used + len(p) > limit and out:
            break
        out.append(p)
        used += len(p)
    return out


def card(text: str, limit: int):
    """生成三段卡片文本。"""
    parts = sentences(text)
    body = pick(parts, limit)
    head = parts[0][:80] if parts else ""
    lines = ["# 压缩卡片", "", f"**问题**：{head}", "",
             "**判据**：", ""]
    lines += [f"- {s}" for s in body] or ["- （无关键句）"]
    lines += ["", "**动作**：按判据执行，结论记 logic_chain.py add，"
              "原文留 tmp 或 references 卡片。", ""]
    return "\n".join(lines), len(parts), len(body)


def main() -> int:
    ap = argparse.ArgumentParser(description="上下文压缩为卡片")
    ap.add_argument("--file", required=True)
    ap.add_argument("--chars", type=int, default=400)
    ap.add_argument("--out")
    args = ap.parse_args()
    with open(args.file, encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    out, total, used = card(text, args.chars)
    print(f"[压缩] 原 {total} 句 → 取 {used} 句（≤{args.chars} 字）")
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(out)
        print(f"[压缩] 卡片写入 {args.out}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
