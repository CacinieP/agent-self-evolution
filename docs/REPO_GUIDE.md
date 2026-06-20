# 仓库使用指南 (Repo Guide)

本文件详细说明仓库的目录组织与各类内容的归属。

## 📁 目录详解

### `surveys/` — 调研材料

收集与 Agent 自进化相关的研究材料。

| 子目录 | 用途 | 文件格式 |
|---|---|---|
| `papers/` | 论文整理(每篇一个目录) | `README.md` + 可选 PDF/笔记 |
| `notes/` | 个人阅读笔记 | `*.md` |
| `articles/` | 博客、技术文章、播客转写 | `*.md` 含链接 |

**论文目录命名**:`年份-关键词-短标题`,例如 `2024-self-rewarding-lms`。

### `practices/` — 实践与复现

| 子目录 | 用途 |
|---|---|
| `experiments/` | 正式实验:含目的、方法、脚本、结果 |
| `prototypes/` | 可运行的最小原型 demo |
| `snippets/` | 有用的代码片段、prompt、工具脚本 |

**实验目录规范**:每个实验一个目录,`README.md` 必须包含复现说明(模型、环境、随机种子、依赖)。

### `benchmarks/`

记录相关评测基准:任务说明、排行榜快照、评测脚本、复现结果。

### `resources/`

非论文类资源:会议演讲、slides、视频、相关开源仓库清单。

### `docs/`

长篇文档:技术综述、路线图、术语表、本指南。

### `assets/`

图片、图表、流程图等媒体资源。

## 🏷️ 内容组织建议

- **每篇论文一个目录**,内部含 `README.md` 描述元信息。
- **跨论文主题**用 tag/关键词在文档中标注,方便检索。
- **实验需可复现**:锁定依赖版本、记录随机种子、保留原始日志。

## 🔍 常用检索

在仓库内搜索:
- 自我反思类:`self-refine`, `self-critique`, `reflexion`
- 自对弈/自训练:`self-play`, `self-instruct`, `SPIN`
- 技能记忆:`skill library`, `voyager`, `expel`
- 系统级:`self-improving agent`, `ADAS`, `SE Agent`

## 📝 维护建议

- 定期(如每月)更新 `surveys/` 与 `resources/`,清理失效链接。
- 重要进展在 `docs/` 中写阶段性综述。
- 鼓励在 PR 描述中附上"为什么收录"的简要说明。
