# 📚 Papers Index — Agent Self-Evolution

> 按本仓库 [TAXONOMY](../../docs/TAXONOMY.md) 的 **What to Evolve** 四大支柱归类。
> 命名规范:`<year>-<keyword>`。每篇一个目录,内含 `README.md`(元信息 + 维度速查)。

收录数:**23**(种子集 15 + 第二批 8,持续扩充)

---

## 🧠 What: Model(模型 / 参数级进化)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [STaR](./2022-star) | 2022 | 生成 rationale,答对的用于自微调,自举推理 | Model · SFT · 自生成数据 |
| [Self-Play Fine-Tuning (SPIN)](./2024-spin) | 2024 | 弱模型与"上一轮的自己"对弈,迭代微调 | Model · SFT/RL · Self-Play |
| [Self-Rewarding Language Models](./2024-self-rewarding-lm) | 2024 | LLM-as-Judge 自奖励 + 迭代 DPO | Model · RL(DPO) · Self-Reward |
| [AgentTuning](./2024-agenttuning) | 2023 | Agent 轨迹 SFT + 通用任务 RL | Model · SFT+RL · 跨任务迁移 |
| [Self-Instruct](./2023-self-instruct) | 2023 | 自生成指令数据微调自身 | Model · SFT · 自生成数据 |
| [RAGEN](./2025-ragen) | 2025 | 多轮多 Agent RL 训练 + 评估框架 | Model+Arch · RL · 信用分配 |
| [Absolute Zero](./2025-absolute-zero) | 2025 | 单模型自出题自做题,代码验证奖励,零数据 | Model · RL · Self-Play + RLVR |

## 📝 What: Context(上下文:记忆 + Prompt)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [Reflexion](./2023-reflexion) | 2023 | 把口头自我反思写入记忆,避免重复犯错 | Context/Memory · Intra · ICL |
| [Self-Refine](./2023-self-refine) | 2023 | 自评 → 自反馈 → 迭代改进 | Context/Prompt · Intra · ICL |
| [ExpeL](./2024-expeL) | 2023 | 从轨迹归纳经验 / 洞察,检索复用 | Context/Memory · Inter · ICL |
| [Agent Workflow Memory](./2024-agent-workflow-memory) | 2024 | 归纳可复用工作流(recipe),按任务检索 | Context/Memory · Inter · Offline+Online |
| [Mem0](./2025-mem0) | 2025 | 生产级长期记忆:抽取/合并/检索 | Context/Memory · Inter · 工程化 |
| [DSPy](./2024-dsp) | 2023 | 声明式 LM 程序 + 自动 prompt 优化 | Context/Prompt · Inter · 自动指标 |
| [Voyager](./2023-voyager) | 2023 | 终身学习 + 可复用代码技能库 | Tool + Memory · Inter · ICL |

## 🔧 What: Tool(工具创造 / 掌握 / 选择)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [Voyager](./2023-voyager) | 2023 | 写代码技能并存进技能库(交叉见 Context) | Tool(Create/Master) |

## 🏗 What: Architecture(单 / 多 Agent 系统级进化)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [ADAS (Meta Agent Search)](./2024-adas) | 2024 | 元 Agent 在代码空间搜索更强 Agent 架构 | Arch · Inter · Evolutionary |
| [AFlow](./2024-aflow) | 2024 | MCTS 自动搜索并迭代最优工作流 | Arch/Workflow · Inter · Search |
| [Darwin Gödel Machine](./2025-darwin-godel-machine) | 2025 | 开放式进化重写自身代码自我改进 | Arch · Inter · Open-ended |
| [Mobile-Agent-E](./2025-mobile-agent-e) | 2025 | 分层多 Agent + 长期记忆,移动任务自进化 | Arch+Memory · Inter · GUI |
| [WebEvolver](./2025-webevolver) | 2025 | 协同进化世界模型提升 Web Agent 自训练 | Model+Context · Inter · Coevolution |

## 📖 Surveys(综述)

| 论文 | 年份 | 定位 |
|---|---|---|
| [A Survey on Self-Evolution of LLMs](./2024-survey-self-evolution-llm) | 2024 | 早期 LLM 自进化综述(自反馈/自训练/自评测) |
| [A Survey of Self-Evolving Agents](./2025-survey-self-evolving-agents) | 2025 | **本仓库 TAXONOMY 主骨架**(What/When/How/Where) |

## 📊 Benchmarks(评测基准)

| 论文 | 年份 | 域 |
|---|---|---|
| [SWE-bench](./2023-swe-bench) | 2023 | Coding(真实 GitHub issue) |
| [AgentBench](./2023-agentbench) | 2023 | General(综合多环境) |

---

## 🗺 收录分布速览

```
支柱:    Model    ████████████ 7
         Context  ██████████████ 7  (Voyager 与 Tool 交叉)
         Tool     ██ 1              (Voyager)
         Arch     ██████████ 5      (ADAS/AFlow/DGM/Mobile-E/WebEvolver)
类型:    方法 19 · 综述 2 · 基准 2
年份:    2022 ×1 · 2023 ×7 · 2024 ×8 · 2025 ×7
```

## ➕ 如何补充

1. 新建目录 `<year>-<keyword>`(如 `2025-mem0`)。
2. 复制任一现有 `README.md` 作为模板,填元信息与维度速查。
3. 在本索引表里加一行,归到对应支柱。
4. 详见 [`CONTRIBUTING.md`](../../CONTRIBUTING.md)。
