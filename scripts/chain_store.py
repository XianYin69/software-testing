"""chain_store.py — 链状态存取（逻辑链/过程链/惩罚计数），一律落用户缓存目录。

红线：缓存文件不得写入 skill 目录；本模块路径由 SMS_HOME 或 %LOCALAPPDATA% 推导。
"""
from __future__ import annotations

import json
import os
import tempfile

CHAINS = ("logic", "process", "penalty")


def cache_root() -> str:
    """返回本技能的缓存目录（不存在则创建）。"""
    home = os.environ.get("SMS_HOME")
    if not home:
        base = os.environ.get("LOCALAPPDATA") or tempfile.gettempdir()
        home = os.path.join(base, "SMS")
    path = os.path.join(home, "cache", "software-testing", "chains")
    os.makedirs(path, exist_ok=True)
    return path


def chain_path(name: str, skill: str = "software-testing") -> str:
    """某条链的 jsonl 文件路径。"""
    if name not in CHAINS:
        raise ValueError(f"未知链名 {name}（可用：{', '.join(CHAINS)}）")
    return os.path.join(cache_root(), f"{skill}-{name}.jsonl")


def append(name: str, entry: dict, skill: str = "software-testing") -> str:
    """追加一条记录（原子：先写 .tmp 再替换不适用，改为逐行 append）。"""
    path = chain_path(name, skill)
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return path


def read(name: str, skill: str = "software-testing") -> list:
    """读全链（缺文件返回空列表）。"""
    path = chain_path(name, skill)
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                out.append({"_broken": line[:120]})
    return out


def replace_last(name: str, entry: dict, skill: str = "software-testing") -> None:
    """以原子写替换末条（用于状态回写：pending→done）。"""
    items = read(name, skill)
    if items:
        items[-1] = entry
    path = chain_path(name, skill)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as handle:
        for item in items:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    os.replace(tmp, path)
