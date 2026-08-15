# Agent 自进化 — 技术分类体系 (Taxonomy)

> 本分类体系以 2025 年权威综述 **《A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve》**([arXiv:2507.21046](https://arxiv.org/abs/2507.21046)) 为骨架,辅以若干独立综述与开源清单,作为本仓库收录论文/实践时的**统一归类标准**。
>
> 这是一个**活文档**,会随调研进展持续修订。每个维度后标注了**对应收录目录**,方便归档。

---

## 0. 核心定义

**自进化 Agent (Self-Evolving Agent)** 指能够**基于自身轨迹或反馈信号,修改其内部参数、上下文状态、工具集或架构拓扑,并显式以"提升未来表现"为目标的 Agent**。

三条判据(满足任意程度即可纳入):

| 判据 | 含义 | 排除项 |
|---|---|---|
| **经验驱动** | 更新由轨迹/自生成数据/环境反馈触发,针对策略边界 | 与历史无关的通用数据合成 |
| **持久性** | 更新产生持久的策略性改变,而非一次性指令跟随 | 纯 in-context 临时行为 |
| **自主探索** | 具备自启动的探索/反思/结构改写机制 | 完全静态的人工流水线(如标准蒸馏) |

形式化:Agent 系统 $\Pi = (\Gamma, \{\psi_i\}, \{C_i\}, \{\mathcal{W}_i\})$,自进化策略 $f(\Pi, \tau, r) = \Pi'$,目标 $\max_f \sum_j U(\Pi_j, \mathcal{T}_j)$。其中 $\Gamma$=架构,$\psi_i$=模型,$C_i$=上下文(prompt+memory),$\mathcal{W}_i$=工具。

> 与之相邻但不等同的范式:**课程学习**(静态数据集排序)、**终身学习**(被动接收任务序列)、**模型编辑/遗忘**(局部参数修改)。自进化 Agent 的独特性在于:可改非参数组件 + 可改架构 + 主动探索 + 自我反思评估。

---

## 1. What to Evolve — 进化什么?(四大支柱)

> 📁 收录时:按主进化对象归类到 `surveys/papers/<year>-<keyword>/`,在 README 中标注主要支柱。

### 1.1 模型 (Models) — 参数级进化
让模型参数基于自生成监督/执行轨迹/环境反馈被持续改写。

| 子类 | 代表工作 |
|---|---|
| **Policy**(策略微调) | SCA (Self-Challenging Agent)、Self-Rewarding LM、SCoRe、PAG、TextGrad、AutoRule |
| **Experience**(从交互/环境构造经验) | AgentGen、Reflexion、Self-Refine、SICA、RAGEN、DYSTIL |

### 1.2 上下文 (Context) — 不改权重的进化
> 包含两个常被混用的方向:**记忆进化**(存什么/忘什么/检索什么)与 **Prompt 优化**(如何组织指令)。

| 子类 | 代表工作 |
|---|---|
| **记忆进化** | Mem0、A-Mem、Memory-R1、Agent Workflow Memory、Expel、MUSE、ReasoningBank、MemGen |
| **Prompt 优化 (PO)** | APE、PromptBreeder、SPO、ProTeGi、PromptAgent、DSPy、Trace、TextGrad、ACE、MASS、MAS-Zero |

### 1.3 工具 (Tools) — 从"工具使用者"到"工具创造者"
| 子类 | 代表工作 |
|---|---|
| **发现与创造** | Voyager、Alita、CREATOR、SkillWeaver、CRAFT、Live-SWE-Agent |
| **迭代精炼(掌握)** | LearnAct、DRAFT、(信用分配 + docstring 修正) |
| **规模化管理与选择** | ToolGen(工具 token 化)、ToolMem、AgentSquare、Darwin Gödel Machine |

### 1.4 架构 (Architecture) — 系统/协作结构级进化
| 子类 | 代表工作 |
|---|---|
| **单 Agent 架构优化** | TextGrad(节点级)、AgentSquare(模块搜索)、Darwin Gödel Machine、AlphaEvolve、Gödel Agent、MemEvolve |
| **多 Agent 系统优化** | AutoFlow、GPTSwarm、ADAS、AFlow(MCTS)、MaAS、ScoreFlow、FlowReasoner、ReMA、GiGPO |

---

## 2. When to Evolve — 何时进化?(时间维度)

> 区分进化发生在**任务执行中**还是**任务之间**,并对应三大学习范式 ICL / SFT / RL。

### 2.1 Intra-test-time(任务内实时进化)
反馈与优化耦合于当前任务实例,**在线**进行。
- **ICL**:Reflexion、Self-Refine、AdaPlanner、TrustAgent(反思/计划修正)
- **SFT**:TT-SI
- **权重自适配(免训练)**:Self-Adaptive LM(Transformer-Squared,推理时实时重组权重)
- **RL**:LADDER(test-time RL / TTRL,即时而学)

### 2.2 Inter-test-time(任务间回顾式进化)
任务完成后,从历史轨迹中学习,**回顾式**进行。
- **ICL**:Agent Workflow Memory、In-Context RL (ICRL)
- **SFT**:SELF、STaR、Quiet-STaR、SiriuS、ARIA(自生成数据 + 自评估迭代)
- **RL**:RAGEN、DYSTIL、WebRL、DigiRL(大规模环境交互 + 课程设计)

---

## 3. How to Evolve — 如何进化?(方法族 + 横切维度)

### 3.1 三大方法族

| 方法族 | 核心机制 | 代表 | 适用 / 权衡 |
|---|---|---|---|
| **Reward-based**(奖励驱动) | 文本反馈 / 内部置信度 / 外部奖励 / 隐式奖励 | Reflexion、Self-Rewarding LM、CISC、Math-Shepherd、"Reward Is Enough"、Puppeteer(编排器 RL) | 灵活但敏感于奖励设计,易 reward hacking |
| **Imitation / Demonstration**(模仿示教) | 自生成或跨 Agent 的高质量完整示教 | STaR、V-STaR、AdaSTaR、SiriuS、RISE、Explore-to-Evolve | 高样本效率,但受示教质量/多样性限制 |
| **Population-based / Evolutionary**(种群进化) | 选择/变异/交叉/竞争,群体并行 | DGM、SPIN、Absolute Zero、GENOME、EvoMAC、SPC | 多样性与开放式发现,但算力高、可解释性弱 |

### 3.2 三大横切维度(任意方法族都适用)

| 维度 | 取值 | 说明 |
|---|---|---|
| **Online / Offline** | 在线(实时交互)/ 离线(预收集数据) | Voyager/AdaPlanner(在线) vs Self-Instruct/OS-Genesis(离线) |
| **On / Off-policy** | 同策略(自身轨迹)/ 异策略(历史/他者/人类) | Reflexion/GRPO(同) vs DPO/经验库(异) |
| **奖励粒度** | Outcome(最终结果)/ Process(逐步)/ Hybrid | DPO/DigiRL(结果) vs Math-Shepherd/Agent Q(过程) vs GiGPO/SPA-RL(混合) |

> 其他可记录维度:**反馈类型**(scalar / 语言 / 置信度 / 适配度)、**数据来源**、**样本效率**、**稳定性**、**可扩展性**。

---

## 4. Where to Evolve — 在哪里进化?(应用域)

> 📁 域专属内容可放入 `practices/experiments/<domain>/`。

### 4.1 通用域进化 (General Domain)
三大机制:**记忆机制**、**课程驱动训练**、**模型-Agent 协同进化**。
- 代表:Mobile-Agent-E、MobileSteward、Generative Agents、UI-Genie、WebEvolver、Absolute Zero、WebRL、Voyager

### 4.2 专属域进化 (Specialized Domain)
| 领域 | 代表 |
|---|---|
| **Coding** | SICA、EvoMAC、AgentCoder、Adaptive Self-Improvement(ML 库构建) |
| **GUI / Web** | AutoGUI、WebVoyager、ReAP、MobileUse、Navi(WindowsAgentArena)、AutoGUI |
| **金融** | QuantAgent、TradingAgents |
| **医疗** | Agent Hospital、MedAgentSim、EvoPatient、DoctorAgent-RL、OriGene、STELLA |
| **教育** | PACE、MathVC、i-vip、EduPlanner、SEFL |
| **其他** | Arxiv Copilot、Agents-of-Change(策略游戏)、Richelieu(AI 外交) |

---

## 5. 评测 (Evaluation)

> 📁 评测材料放入 `benchmarks/`。当前评测正从"单次打分"转向"轨迹式、成本感知"评估。

### 5.1 五大评测目标与指标
| 目标 | 关键指标 | 代表基准 |
|---|---|---|
| **Adaptivity**(适应性) | Success Rate by Iteration、Adaptation Speed | SWE-bench、WebArena、GAIA、AgentBench |
| **Retention**(保持/抗遗忘) | FGT、BWT | LTMBenchmark、LifelongAgentBench、MemoryAgentBench |
| **Generalization**(泛化) | Aggregate Performance、OOD Performance | AgentBench、TheAgentCompany、MLE-Bench |
| **Efficiency**(效率) | Token / Step / Time / Tool calls、Tool Productivity、Cost-per-Gain | TheAgentCompany、MLE-Bench |
| **Safety**(安全) | Safety Score、Harm Score、CuP、Risk Ratio、Refusal Rate、Leakage Rate | Agent-SafetyBench、ST-WebAgentBench、SwarmBench |

### 5.2 三种评测范式(按时间尺度)
1. **Static Assessment** — 固定任务单点评测(建立基线、组件级)
2. **Short-horizon Adaptive** — 增强传统基准加时间维度,或内建动态评测(ADAS、AWM、MemoryAgentBench TTL)
3. **Long-horizon Lifelong Learning** — 跨任务持续学习,衡量保持/泛化/遗忘(LifelongAgentBench、LTMBenchmark、TRACE、Benchmark Self-Evolving)

> ⚠️ 现状缺口:大多数基准采用 episodic 评测(任务间重置状态),无法测出知识累积/退化;latency/cost/safety 报告不一致,难做 apples-to-apples 对比。

---

## 6. 开放问题与风险 (Open Problems & Risks)

> 📁 相关讨论可放 `surveys/articles/` 或 `docs/`。

### 6.1 风险(自进化特有)
- **行为漂移 / Misevolution**:自训练导致安全对齐"灾难性遗忘",拒绝过的有害指令又开始执行
- **奖励黑客**:利用自定奖励漏洞(如"无理由退款换好评")
- **Alignment Tipping Process (ATP)**:发现"不对齐更有奖励"而导致策略倾覆
- **自创/外采工具安全**:生成含漏洞代码、无法识别恶意外部工具、PII 泄露

### 6.2 护栏方向
- 工具/代码沙箱 + 自动安全验证(SAST/依赖扫描)
- 自修改审计轨迹 + 版本化 + 可回滚
- 长期漂移的持续监控 + 红队
- 高风险动作审批门 + 隐私保护(数据最小化、PII 脱敏)

### 6.3 研究方向
个性化 Agent(冷启动 + 治理)、泛化与抗遗忘、安全可控、多 Agent 协同进化生态

---

## 7. 归档速查(方法 → 维度 → 目录)

收录一篇论文/实践时,建议在它的 `README.md` 里填这张小表:

```
What:   [Model(Policy/Experience) / Context(Memory/Prompt) / Tool(Create/Master/Select) / Arch(Single/Multi)]
When:   [Intra-test / Inter-test] × [ICL / SFT / RL]
How:    [Reward-based / Imitation / Population] × [Online/Offline, On/Off-policy, Outcome/Process/Hybrid]
Where:  [General / Coding / GUI / Finance / Medical / Education / Other]
Eval:   [Adaptivity / Retention / Generalization / Efficiency / Safety]
```

填好后,把条目放到 `surveys/papers/<year>-<keyword>/`(调研)或 `practices/experiments/<domain>/`(复现)。

---

## 参考文献(核心综述与清单)

- **A Survey of Self-Evolving Agents** (arXiv:2507.21046, 2025) — 本体系主骨架,[GitHub](https://github.com/CharlesQ9/Self-Evolving-Agents)
- **A Systematic Survey of Self-Evolving Agents: From Model-Centric to Environment-Driven Co-Evolution** (TechRxiv, 2025)
- **Awesome-Self-Evolving-Agents** — [XMUDeepLIT 维护的论文/基准清单](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents)
- **A Survey on Self-Evolution of Large Language Models** (arXiv:2404.14387, 2024) — 早期 LLM 自进化综述
- **Advances and Challenges in Foundation Agents** (arXiv:2504.01990, 2025)

> 欢迎在 PR 中补充分类维度、修正归类,或补充新综述。
