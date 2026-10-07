"""deps_check.py — 本地依赖可达性自检：local://<skill-id> 指向的技能目录是否存在。

用法：python scripts/deps_check.py [--root <skill目录>] [--home <skills目录>]
"""
from __future__ import annotations

import argparse
import json
import os

FIELDS = ("name", "source_url", "license", "version", "install", "checked_at")


def default_home() -> str:
    """推断 SMS skills 根目录。"""
    env = os.environ.get("SMS_HOME")
    if env:
        return os.path.join(env, "skills")
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.dirname(root)


def read_deps(path: str):
    """读 deps.json 条目（容错：缺文件返回空）。"""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig") as handle:
        data = json.load(handle)
    if isinstance(data, dict):
        data = data.get("dependencies") or data.get("deps") or []
    return data if isinstance(data, list) else []


def check(root: str, home: str):
    """返回 (ok 列表, 问题列表)。"""
    ok, issues = [], []
    for entry in read_deps(os.path.join(root, "dependence", "deps.json")):
        if not isinstance(entry, dict):
            issues.append("条目非对象")
            continue
        name = entry.get("name", "?")
        missing = [k for k in FIELDS if k not in entry]
        if missing:
            issues.append(f"{name}: 缺字段 {missing}")
        url = (entry.get("source_url") or "").strip()
        if url.startswith("local://"):
            skill = url[len("local://"):]
            path = os.path.join(home, skill)
            if os.path.isdir(path):
                ok.append(f"{name} -> 存在 {path}")
            else:
                issues.append(f"{name}: 本地技能目录不存在 {path}")
        elif url.startswith(("http://", "https://")):
            ok.append(f"{name} -> 远端待联网核验（须网络授权）")
        else:
            issues.append(f"{name}: source_url 无法识别 {url!r}")
    return ok, issues


def main() -> int:
    ap = argparse.ArgumentParser(description="依赖可达性自检")
    ap.add_argument("--root", default=os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--home", default=default_home())
    args = ap.parse_args()
    ok, issues = check(args.root, args.home)
    for line in ok:
        print("[OK] " + line)
    for line in issues:
        print("[问题] " + line)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
