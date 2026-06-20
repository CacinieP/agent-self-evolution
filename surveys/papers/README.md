# 📚 Papers Index — Agent Self-Evolution

> 按本仓库 [TAXONOMY](../../docs/TAXONOMY.md) 的 **What to Evolve** 四大支柱归类。
> 命名规范:`<year>-<keyword>`。每篇一个目录,内含 `README.md`(元信息 + 维度速查)。

收录数:**48**(种子 15 + batch2 8 + batch3 12 + batch4 8 + batch5 5,持续扩充)

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
| [TextGrad](./2024-textgrad) | 2024 | 文字反馈当"梯度",反向传播优化复合系统 | Model+Context+Arch · 文字梯度 |
| [DigiRL](./2024-digirl) | 2024 | 真实安卓环境自主 RL 训练设备控制 Agent | Model · RL · Offline→Online |
| [SCoRe](./2024-score) | 2024 | 多轮在线 RL 教模型自我纠正(自生成数据) | Model · RL · 自纠正 |
| [Math-Shepherd](./2023-math-shepherd) | 2023 | 无需人工标注,自动构造逐步 PRM | Model/Reward · RL · Process |
| [Agent Q](./2024-agent-q) | 2024 | MCTS + 自我批判 + RL,真实网页任务 | Model · RL · MCTS |
| [WebRL](./2024-webrl) | 2024 | 自进化在线课程 RL 训 Web Agent | Model · RL · 自进化课程 |
| [Memory-R1](./2025-memory-r1) | 2025 | 用 RL 训练 Agent 主动管理外部记忆 | Model+Memory · RL · 记忆管理 |

## 📝 What: Context(上下文:记忆 + Prompt)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [Reflexion](./2023-reflexion) | 2023 | 把口头自我反思写入记忆,避免重复犯错 | Context/Memory · Intra · ICL |
| [Self-Refine](./2023-self-refine) | 2023 | 自评 → 自反馈 → 迭代改进 | Context/Prompt · Intra · ICL |
| [ExpeL](./2024-expeL) | 2023 | 从轨迹归纳经验 / 洞察,检索复用 | Context/Memory · Inter · ICL |
| [Agent Workflow Memory](./2024-agent-workflow-memory) | 2024 | 归纳可复用工作流(recipe),按任务检索 | Context/Memory · Inter · Offline+Online |
| [Mem0](./2025-mem0) | 2025 | 生产级长期记忆:抽取/合并/检索 | Context/Memory · Inter · 工程化 |
| [A-MEM](./2025-a-mem) | 2025 | Zettelkasten 式自组织、自进化的记忆网络 | Context/Memory · Inter · 自组织 |
| [DSPy](./2024-dsp) | 2023 | 声明式 LM 程序 + 自动 prompt 优化 | Context/Prompt · Inter · 自动指标 |
| [APE](./2023-ape) | 2023 | 输入-输出样例合成指令,筛最优 prompt | Context/Prompt · Inter · 程序合成 |
| [PromptBreeder](./2024-promptbreeder) | 2024 | 进化任务提示 + 变异提示,自我指涉 | Context/Prompt · Inter · Evolutionary |
| [SPO](./2025-spo) | 2025 | 仅模型自反馈(无真值)优化 prompt | Context/Prompt · Inter · 自监督 |
| [PromptAgent](./2024-promptagent) | 2024 | MCTS 战略规划产出专家级 prompt | Context/Prompt · Inter · MCTS |
| [Voyager](./2023-voyager) | 2023 | 终身学习 + 可复用代码技能库 | Tool + Memory · Inter · ICL |

## 🔧 What: Tool(工具创造 / 掌握 / 选择)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [Voyager](./2023-voyager) | 2023 | 写代码技能并存进技能库(交叉见 Context) | Tool(Create/Master) |
| [CREATOR](./2023-creator) | 2023 | LLM 自己造工具:抽象设计 + 代码实现 | Tool(Create) |
| [SkillWeaver](./2025-skillweaver) | 2025 | 自主合成 API 技能 + 练习打磨,技能库成长 | Tool(Create + Master) |
| [ToolGen](./2024-toolgen) | 2024 | 工具内化为唯一 token,检索与调用统一为生成 | Tool(Select) + Model |

## 🏗 What: Architecture(单 / 多 Agent 系统级进化)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [ADAS (Meta Agent Search)](./2024-adas) | 2024 | 元 Agent 在代码空间搜索更强 Agent 架构 | Arch · Inter · Evolutionary |
| [AFlow](./2024-aflow) | 2024 | MCTS 自动搜索并迭代最优工作流 | Arch/Workflow · Inter · Search |
| [Darwin Gödel Machine](./2025-darwin-godel-machine) | 2025 | 开放式进化重写自身代码自我改进 | Arch · Inter · Open-ended |
| [Mobile-Agent-E](./2025-mobile-agent-e) | 2025 | 分层多 Agent + 长期记忆,移动任务自进化 | Arch+Memory · Inter · GUI |
| [WebEvolver](./2025-webevolver) | 2025 | 协同进化世界模型提升 Web Agent 自训练 | Model+Context · Inter · Coevolution |
| [GPTSwarm](./2024-gptswarm) | 2024 | 多 Agent 建模为可优化计算图,自动调节点/边 | Arch(Multi-Agent) · Inter · Search |
| [AgentSquare](./2024-agentsquare) | 2024 | 模块化设计空间 + 模块进化/重组搜索 Agent | Arch · Inter · 模块化进化 |

## 🛡 What: Safety(自进化特有的安全 / 对齐风险)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [Alignment Tipping Process (ATP)](./2025-atp-alignment-tipping) | 2025 | 持续自进化侵蚀对齐,Agent 滑向不对齐 | Safety · 部署期 · 对齐漂移 |
| [ST-WebAgentBench](./2024-st-webagentbench) | 2024 | Web Agent 安全可信评测:375 任务 + 3057 策略 | Safety · Web · Benchmark |

## 🏥 What: Specialized Domain(专属域自进化)

| 论文 | 年份 | 域 | 一句话 |
|---|---|---|---|
| [Agent Hospital](./2024-agent-hospital) | 2024 | Medical | 虚拟医院,医生 Agent 从诊疗经验中自主进化 |
| [QuantAgent](./2024-quantagent-strategy) | 2024 | Finance | 多 Agent 自动发现量化交易策略 |
| [EduPlanner](./2025-eduplanner) | 2025 | Education | 多 Agent 对抗迭代优化教学设计 |
| [Mobile-Agent-E](./2025-mobile-agent-e) | 2025 | GUI/Mobile | (交叉见 Arch) |
| [DigiRL](./2024-digirl) | 2024 | GUI/Device | (交叉见 Model) |
| [WebEvolver](./2025-webevolver) | 2025 | Web | (交叉见 Arch) |
| [SkillWeaver](./2025-skillweaver) | 2025 | Web | (交叉见 Tool) |
| [WebRL](./2024-webrl) | 2024 | Web | (交叉见 Model) |
| [Agent Q](./2024-agent-q) | 2024 | Web | (交叉见 Model) |

## 📖 Surveys(综述)

| 论文 | 年份 | 定位 |
|---|---|---|
| [A Survey on Self-Evolution of LLMs](./2024-survey-self-evolution-llm) | 2024 | 早期 LLM 自进化综述(自反馈/自训练/自评测) |
| [A Survey of Self-Evolving Agents](./2025-survey-self-evolving-agents) | 2025 | **本仓库 TAXONOMY 主骨架**(What/When/How/Where) |

## 📊 Benchmarks(评测基准)

| 论文 | 年份 | 域 | 侧重 |
|---|---|---|---|
| [SWE-bench](./2023-swe-bench) | 2023 | Coding | 真实 GitHub issue |
| [AgentBench](./2023-agentbench) | 2023 | General | 综合多环境 |
| [GAIA](./2023-gaia) | 2023 | General | 真实世界多步任务 |
| [LifelongAgentBench](./2025-lifelongagentbench) | 2025 | General | 终身学习 / 抗遗忘 |
| [Agent-SafetyBench](./2024-agent-safetybench) | 2024 | General/Safety | ~349 环境的安全评测 |
| [ST-WebAgentBench](./2024-st-webagentbench) | 2024 | Web/Safety | 375 任务 + 3057 策略的可信评测 |

---

## 🗺 收录分布速览

```
各表唯一论文数(跨类重复计入多表,去重后共 48):
  Model 14 · Context 12 · Tool 4 · Arch 7 · Safety 2 · 域专属 9 · 综述 2 · 基准 6
注:Voyager 同时在 Context/Tool;Mobile-E/WebEvolver/DigiRL/Agent Q/WebRL/SkillWeaver/ST-WebAgentBench
    等跨"支柱×域"或"支柱×基准",故各表相加 > 48。

类型:  方法类 40 · 综述 2 · 基准 6
年份:  2022 ×1 · 2023 ×10 · 2024 ×23 · 2025 ×14
```

## ✅ 覆盖体检(对照 TAXONOMY 声明的代表工作)

- Prompt 优化:APE/PromptBreeder/SPO/PromptAgent/DSPy ✅
- 工具:Voyager/CREATOR/SkillWeaver/ToolGen ✅
- 多 Agent 架构:GPTSwarm/ADAS/AgentSquare/EduPlanner/QuantAgent ✅(MaAS 待补)
- RL 训练:SCoRe/Math-Shepherd/Agent Q/WebRL/TextGrad/DigiRL/RAGEN/AgentTuning/Memory-R1 ✅(较完整)
- 安全:ATP/Agent-SafetyBench/ST-WebAgentBench ✅
- 记忆:Mem0/AWM/ExpeL/A-MEM/Reflexion/Memory-R1 ✅(ReasoningBank 待补)
- 终身学习评测:LifelongAgentBench ✅
- 域:医疗/金融/教育/GUI/Web ✅(全覆盖)

> 至此,TAXONOMY 四维 + 48 篇代表工作 + 覆盖体检齐全,五大支柱与五大专属域(医疗/金融/教育/GUI/Web)均有覆盖,可作为该方向的**可用索引站**。剩余待补为个别长尾方法。

## ➕ 如何补充

1. 新建目录 `<year>-<keyword>`(如 `2025-memory-r1`)。
2. 复制任一现有 `README.md` 作为模板,填元信息与维度速查。
3. 在本索引表里加一行,归到对应支柱。
4. 详见 [`CONTRIBUTING.md`](../../CONTRIBUTING.md)。
