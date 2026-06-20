#!/usr/bin/env python3
"""
校验 practices/prototypes/*/<main>.py 的 --selftest 能否跑通。

约定:每个原型都支持 `--selftest`,会用内置示例 + 强制 mock 完成一次自测,
退出码 0 表示通过。这样脚本无需关心各原型参数名差异(--task/--inputs/--tasks)。

用法:python check_prototypes.py [prototypes_root]
"""

from __future__ import annotations

import pathlib
import subprocess
import sys


def find_mains(root: pathlib.Path) -> list[pathlib.Path]:
    mains = []
    for d in sorted(root.iterdir()):
        if d.is_dir():
            pys = list(d.glob("*.py"))
            if len(pys) == 1:
                mains.append(pys[0])
    return mains


def main() -> int:
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("practices/prototypes")
    if not root.exists():
        print(f"[skip] 目录不存在: {root}")
        return 0

    mains = find_mains(root)
    if not mains:
        print("未发现原型主程序,跳过。")
        return 0

    bad = 0
    for py in mains:
        proc = subprocess.run(
            [sys.executable, str(py), "--selftest"],
            capture_output=True, text=True, timeout=60,
        )
        ok = proc.returncode == 0
        status = "✅" if ok else "❌"
        try:
            display = py.relative_to(pathlib.Path.cwd())
        except ValueError:
            display = py
        print(f"{status} {display}")
        if not ok:
            bad += 1
            tail = (proc.stderr or proc.stdout).strip().splitlines()[-6:]
            for line in tail:
                print(f"     {line}")

    print(f"\n校验完成:{len(mains) - bad}/{len(mains)} 个原型 --selftest 跑通")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
