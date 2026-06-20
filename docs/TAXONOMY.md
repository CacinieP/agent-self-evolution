# Agent 自进化 — 技术分类体系 (Taxonomy)

本文件用于梳理 Agent Self-Evolution 领域的技术脉络,便于归类论文与实践。

> 🚧 这是一个**活文档**,会随调研进展持续更新。

---

## 一、按"进化机制"分类

### 1. 自我反思与改进 (Self-Reflection & Refinement)
Agent 对自身输出进行批判并迭代改进,**不更新模型权重**。

- 代表:Self-Refine, Self-Critique, Reflexion, CRITIC
- 关键:反馈信号来自模型自身或外部工具

### 2. 自生成数据与微调 (Self-Generated Data & Fine-tuning)
Agent 生成训练数据并用于自我微调,**更新模型权重**。

- 代表:Self-Instruct, SPIN (Self-Play Fine-Tuning), Self-Rewarding LM
- 关键:数据质量过滤、迭代训练循环

### 3. 自我对弈 (Self-Play)
Agent 与自己(或多个副本)对弈,从对抗中学习。

- 代表:SPIN, Self-Play in reasoning/games, Debate
- 关键:对手强度匹配、探索-利用平衡

### 4. 技能与记忆积累 (Skill & Memory Accumulation)
Agent 将经验沉淀为可复用的技能 / 记忆库。

- 代表:Voyager (Minecraft), ExpeL, Generative Agents
- 关键:技能抽象、检索、复用、遗忘

### 5. Agent 训练循环 (Agent Training Loop)
端到端地从 Agent 轨迹中学习策略。

- 代表:RLHF / RLAIF, Agent Trajectory Learning, FireAct, AgentTuning
- 关键:奖励建模、轨迹采样、策略优化

### 6. 系统级自进化 (System-level Self-Evolution)
Agent 自动改进自身**架构 / 工具 / 提示词 / Agent 本身**。

- 代表:Self-Improving Agent, ADAS (Automated Design of Agentic Systems), GPTSwarm
- 关键:元学习、自动搜索、组合优化

---

## 二、按"反馈来源"分类

| 来源 | 说明 | 代表场景 |
|---|---|---|
| 内部自评 (Self) | 模型自身打分/批判 | Self-Refine, Self-Rewarding |
| 工具/环境 (Tool/Env) | 代码执行、搜索、仿真反馈 | Reflexion, Voyager |
| 模型间互评 (Multi-Agent) | 多个 Agent 互相反馈 | Debate, Multi-agent critique |
| 人类反馈 (Human) | 人工标注/偏好 | RLHF |
| AI 反馈 (AI Feedback) | 更强模型作为裁判 | RLAIF, Constitutional AI |

---

## 三、按"是否更新权重"分类

- **In-Context 进化**:不改权重,靠提示/记忆/技能库改进 → Reflexion, Voyager
- **Weight 更新进化**:改权重,需训练 → SPIN, Self-Rewarding, AgentTuning
- **混合**:先 In-Context 收集,再触发 Weight 更新 → Self-Improving Agent

---

## 四、典型评测基准

| 基准 | 侧重点 |
|---|---|
| AgentBench | 综合 Agent 能力 |
| SWE-bench | 真实软件工程任务 |
| GAIA | 通用助手真实世界问题 |
| WebArena / VisualWebArena | 网页交互 |
| ToolBench / API-Bank | 工具调用 |
| MINT | 多轮工具 + 语言交互 |
| AppWorld | 真实 App 自动化 |

---

## 五、开放问题 (Open Problems)

- ❓ 自进化如何避免**奖励黑客 / 模式坍缩**?
- ❓ 自生成数据的**质量上限**在哪里?
- ❓ In-Context 进化 vs Weight 更新,**何时该训练**?
- ❓ 如何衡量"持续进化"能力(而非单点成绩)?
- ❓ **安全性**:自进化 Agent 如何保持对齐?

---

> 欢迎在 PR 中补充分类维度或修正归类。
