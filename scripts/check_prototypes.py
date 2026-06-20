#!/usr/bin/env python3
"""
校验 practices/prototypes/*/<main>.py 的离线 mock 模式能否跑通。

对每个原型目录:
  - 找到唯一的 *.py 主程序
  - 用 --mock(若支持)尝试运行,期望退出码 0
  - 不支持 --mock 或运行失败则标记

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
        # 先尝试 --mock 自测(各原型参数名不同,只传公共的最小参数)
        proc = subprocess.run(
            [sys.executable, str(py), "--mock", "--task", "test"],
            capture_output=True, text=True, timeout=60,
        )
        ok = proc.returncode == 0
        status = "✅" if ok else "❌"
        # 用 try 保护展示路径,避免相对/绝对路径不兼容
        try:
            display = py.relative_to(pathlib.Path.cwd())
        except ValueError:
            display = py
        print(f"{status} {display}")
        if not ok:
            bad += 1
            # 打印末尾若干行帮助定位
            tail = (proc.stderr or proc.stdout).strip().splitlines()[-6:]
            for line in tail:
                print(f"     {line}")

    print(f"\n校验完成:{len(mains) - bad}/{len(mains)} 个原型 mock 跑通")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
