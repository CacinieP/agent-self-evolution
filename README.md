# 🧬 Agent Self-Evolution

> 一个公开收集、整理 Agent(智能体)自进化相关**调研与实践**的仓库。
>
> A public repository for collecting and organizing **research and practice** on Agent Self-Evolution.

本仓库致力于系统性地归档与"Agent 自进化(Self-Evolution)"相关的论文、综述、文章、实验、原型与代码片段,方便研究者与工程师追踪该方向的最新进展,并复现/扩展其中的方法。

---

## 📖 Why this repo?

大模型驱动的 Agent 正从"被动执行工具调用"走向"主动改进自身"。围绕**自我学习、自我改进、自我对弈、自我反思**等能力的自进化方向正在快速演进,但相关工作分散在顶会、arXiv、技术博客与开源项目中。本仓库希望成为这一方向的:

- 📚 **索引站** — 论文、综述、关键文章一站式检索
- 🧪 **复现场** — 关键方法的可运行原型与实验记录
- 🧭 **路标牌** — 梳理技术脉络、分类体系与开放问题

---

## 🗂️ Repository Structure

```
agent-self-evolution/
├── surveys/              # 调研:论文、综述、文章
│   ├── papers/           #   论文 PDF / 链接 / 笔记
│   ├── notes/            #   个人阅读笔记
│   └── articles/         #   博客、技术文章、播客转写
├── practices/            # 实践:实验、原型、片段
│   ├── experiments/      #   正式实验(含数据/脚本/结果)
│   ├── prototypes/       #   可运行的最小原型
│   └── snippets/         #   有用的代码片段/工具
├── benchmarks/           # 评测基准与排行榜记录
├── resources/            # 演讲、slides、视频、相关仓库清单
├── docs/                 # 长文档:技术综述、路线图、术语表
└── assets/               # 图片、图表等资源
```

详细说明见 [`docs/REPO_GUIDE.md`](docs/REPO_GUIDE.md)。

---

## 🚀 Quick Start

1. **浏览**:从 [`surveys/`](surveys) 开始了解领域全貌。
2. **检索**:在仓库内搜索关键词(如 `self-refine`、`self-play`、`skill library`)。
3. **复现**:进入 [`practices/prototypes/`](practices/prototypes) 运行最小原型。
4. **贡献**:欢迎通过 Issue / PR 补充论文、修正笔记、提交复现。详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

---

## 📌 Topics Covered

| 维度 | 关键词 |
|---|---|
| 自我反思与改进 | Self-Refine, Self-Critique, Reflexion |
| 自我对弈 / 自生成数据 | Self-Play, Self-Instruct, SPIN |
| 技能记忆 | Skill Library, Voyager, ExpeL |
| Agent 训练循环 | RLHF, RLAIF, Agent Trajectory Learning |
| 自进化系统 | SE Agent, Self-Improving Agent, ADAS |
| 评测 | AgentBench, SWE-bench, GAIA |

(完整分类见 [`docs/TAXONOMY.md`](docs/TAXONOMY.md))

---

## 🤝 Contributing

欢迎贡献!无论是补充一篇新论文、提交一份复现笔记,还是修正一个错别字。

- 报告问题 / 提建议:[Open an Issue](https://github.com/CacinieP/agent-self-evolution/issues/new)
- 提交内容:[Open a PR](https://github.com/CacinieP/agent-self-evolution/compare)
- 具体流程与规范见 [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## 📄 License(双协议 / Dual License)

本仓库按内容类型采用**双协议**:

| 内容 | 协议 | 文件 |
|---|---|---|
| **代码**(`*.py/js/ts/sh`、脚本、配置) | **MIT License** | [`LICENSE-CODE`](LICENSE-CODE) |
| **文档**(`*.md`、笔记、综述、README、图表) | **CC BY 4.0** | [`LICENSE-DOC`](LICENSE-DOC) |

总览见 [`LICENSE`](LICENSE)。

> 论文 PDF 等第三方材料的版权归原作者所有,本仓库仅用于学习研究目的。

---

## ⭐ Star History

如果这个仓库对你有帮助,欢迎点个 Star 支持一下!⭐
