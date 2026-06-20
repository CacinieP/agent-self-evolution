#!/usr/bin/env python3
"""
校验 surveys/papers/*/README.md 是否符合论文模板规范。

规则:每个论文 README 必须包含以下关键小节(作为标题或列表项):
  作者 / 发表 / 链接 / 核心方法 / 维度速查

用法:python check_papers.py [papers_root]
退出码:0=全部通过, 非0=存在不合规文件。
"""

from __future__ import annotations

import pathlib
import re
import sys

REQUIRED = ["作者", "发表", "链接", "核心方法", "维度速查"]


def check(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems: list[str] = []
    for key in REQUIRED:
        if key not in text:
            problems.append(f"缺少关键内容: {key}")
    # 链接须是 http(s) 链接
    if not re.search(r"https?://", text):
        problems.append("缺少 http(s) 链接")
    return problems


def main() -> int:
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("surveys/papers")
    if not root.exists():
        print(f"[skip] 目录不存在: {root}")
        return 0

    bad = 0
    for readme in sorted(root.glob("*/README.md")):
        problems = check(readme)
        if problems:
            bad += 1
            print(f"\n❌ {readme}")
            for p in problems:
                print(f"   - {p}")

    total = len(list(root.glob("*/README.md")))
    print(f"\n校验完成:{total - bad}/{total} 个论文 README 合规")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
