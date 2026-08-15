# 📚 Papers Index — Agent Self-Evolution

> 按本仓库 [TAXONOMY](../../docs/TAXONOMY.md) 的 **What to Evolve** 四大支柱归类。
> 命名规范:`<year>-<keyword>`。每篇一个目录,内含 `README.md`(元信息 + 维度速查)。

收录数:**124**(目录命名分布:2022 ×1 / 2023 ×12 / 2024 ×82 / 2025 ×29;按论文实际年份见文末速览)

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
| [SCA](./2025-sca) | 2025 | 自对比学习区分好/差决策,无需人工标注 | Model · SFT · 自对比 |
| [AgentGen](./2024-agentgen) | 2024 | Agent 自主生成训练环境,在自生成环境上自训练 | Model(Exp) · SFT · 环境生成 |
| [PAG](./2024-pag) | 2024 | 部分注意力引导高效 Agent 训练,降低计算开销 | Model · RL · 效率优化 |
| [SICA](./2024-sica) | 2024 | 代码辅助中自动测试+自修正,编程能力自进化 | Model+Tool · RL · 代码验证 |
| [DYSTIL](./2025-dystil) | 2025 | 从失败轨迹提取深层洞察,跨任务自我改进 | Model(Exp)+Memory · SFT · 轨迹分析 |
| [Quiet-STaR](./2024-quiet-star) | 2024 | LLM 自主学习在每个 token 前生成内部推理 | Model · SFT/RL · 自教推理 |
| [LADDER](./2024-ladder) | 2025 | Test-time RL 优化推理分布 | Model · RL · TTRL |
| [SELF](./2024-self) | 2024 | 自反馈信号驱动任务间持续改进 | Model · SFT · 自反馈 |
| [ARIA](./2025-aria) | 2025 | 迭代式自对齐优化推理,无需外部验证 | Model · ICL · 内部一致性 |
| [V-STaR](./2024-v-star) | 2025 | 验证器筛选高质量自示范,解决错误示范污染 | Model · SFT · 验证自举 |
| [AdaSTaR](./2024-adastar) | 2024 | 自适应选择最优推理模板,零样本自举 | Model · SFT · 自适应模板 |
| [RISE (Recursive Introspection)](./2024-rise) | 2024 | 多轮在线 RL 训练"递归内省",测试时自我改进 | Model · RL · 递归自省 |
| [CISC](./2024-cisc) | 2024 | 课程驱动自一致推理,减少分布偏移 | Model · SFT · 课程学习 |
| [Self-Adaptive LM (Transformer-Squared)](./2024-self-adaptive-lm) | 2025 | 推理时按任务实时选择/重组权重奇异分量 | Model · 参数自适应 · Test-time |
| [TT-SI](./2024-tt-si) | 2025 | 测试时自我改进,自生成经验提升后续表现 | Model+Context · Test-time · 自评自改 |
| [AutoRule](./2024-autorule) | 2025 | 从推理链提取规则构造奖励,改进偏好学习 | Model · 规则奖励 · 偏好优化 |
| [GENOME](./2024-genome) | 2025 | 遗传/群体进化直接优化 LLM 权重参数 | Model(参数) · Evolutionary · 无梯度 |

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
| [MUSE](./2024-muse) | 2025 | 经验驱动自进化 Agent,层级记忆支撑长时任务 | Context/Memory · Inter · 经验学习 |
| [ReasoningBank](./2024-reasoningbank) | 2024 | 协作学习+验证系统化提升推理能力 | Context(Memory)+Arch · SFT · 协作验证 |
| [MemGen](./2024-memgen) | 2024 | 记忆增强生成:写入-检索-融合完整管线 | Context/Memory · Inter · 记忆管线 |
| [ProTeGi](./2024-protegi) | 2024 | 遗传算法变异/选择/交叉优化 prompt | Context/Prompt · Inter · 遗传编程 |
| [ACE](./2024-ace) | 2024 | 后向推理自动生成高质量思维链 | Context(Prompt)+Model · Intra · ICL · 自修正 |
| [SiriuS](./2024-sirius) | 2024 | 协同指令理解与自我精化,无需外部反馈 | Context(Prompt)+Model · SFT · 协同自精化 |
| [ICRL Prompting (Reward Is Enough)](./2024-icrl) | 2025 | 多轮提示让 LLM 在上下文内做 RL 自我改进 | Context/Prompt · Intra · 上下文 RL |

## 🔧 What: Tool(工具创造 / 掌握 / 选择)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [Voyager](./2023-voyager) | 2023 | 写代码技能并存进技能库(交叉见 Context) | Tool(Create/Master) |
| [CREATOR](./2023-creator) | 2023 | LLM 自己造工具:抽象设计 + 代码实现 | Tool(Create) |
| [SkillWeaver](./2025-skillweaver) | 2025 | 自主合成 API 技能 + 练习打磨,技能库成长 | Tool(Create + Master) |
| [ToolGen](./2024-toolgen) | 2024 | 工具内化为唯一 token,检索与调用统一为生成 | Tool(Select) + Model |
| [Alita](./2024-alita) | 2024 | LLM Agent 自主探索 IoT 设备构建工具集 | Tool(Discovery) · ICL · 自我探索 |
| [CRAFT](./2024-craft) | 2024 | 概念递归激活,Agent 自主分解并工具化子任务 | Tool(Refinement) · Intra · ICL |
| [LearnAct](./2024-learnact) | 2024 | 从成功轨迹中学习生成 Web 操作动作空间 | Tool(Refinement) · Inter · ICL |
| [ToolMem](./2025-toolmem) | 2025 | 工具调用结果编码为可检索记忆 | Tool(Select)+Memory · Inter · ICL |
| [DRAFT](./2024-draft) | 2024 | 动态检索+微调工具描述,优化工具使用策略 | Tool(Refinement) · Intra · ICL |
| [Live-SWE-Agent](./2024-live-swe-agent) | 2024 | 真实环境持续自进化 SWE Agent | Tool+Model · RL · 持续改进 |

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
| [AlphaEvolve](./2024-alphaevolve) | 2025 | 编程 Agent + 进化搜索,科学计算中发现新解 | Arch+Model · RL · 开放发现 |
| [Gödel Agent](./2025-godel-agent) | 2025 | 自我指涉框架,递归式自我改进 | Arch · Inter · 递归自改进 |
| [MemEvolve](./2025-memevolve) | 2025 | 记忆反馈驱动架构自进化,经验→结构闭环 | Arch+Memory · ICL · 记忆驱动 |
| [MaAS](./2024-maas) | 2024 | 可微分架构搜索自动设计多 Agent 协作拓扑 | Arch(Multi) · SFT · 架构搜索 |
| [ScoreFlow](./2024-scoreflow) | 2024 | 评分驱动的多 Agent 工作流自动优化 | Arch(Multi) · ICL · 评分优化 |
| [FlowReasoner](./2024-flowreasoner) | 2024 | 推理中自主优化工作流,动态重路由 | Arch · Intra · ICL · 动态规划 |
| [ReMA](./2024-rema) | 2024 | 记忆增强推理,分层记忆+自优化 | Arch+Memory · ICL · 协同自进化 |
| [GiGPO](./2025-gigpo) | 2025 | 梯度+博弈论多 Agent 策略协同均衡 | Arch(Multi)+Model · RL · 博弈均衡 |
| [Puppeteer](./2024-puppeteer) | 2025 | "提线木偶"中央编排器 RL 训练,动态指挥多 Agent | Arch(Multi) · RL · 编排进化 |
| [MASS](./2024-mass) | 2025 | 联合优化多 Agent 提示与通信拓扑的分阶段搜索 | Arch(Multi) · Search · 提示+拓扑 |
| [AutoFlow](./2024-autoflow) | 2024 | 迭代自动生成并精化自然语言 Agent 工作流 | Arch/Workflow · 迭代生成 |
| [Trace (OptoPrime)](./2024-trace) | 2024 | 工作流当计算图,执行轨迹+反馈做"文字自动微分" | Arch/Workflow · 反馈优化 |
| [MAS-Zero](./2024-mas-zero) | 2025 | 零监督自反思生成多 Agent 系统设计 | Arch(Multi) · 自反思 · 零监督 |

## 🛡 What: Safety(自进化特有的安全 / 对齐风险)

| 论文 | 年份 | 一句话 | 维度速查 |
|---|---|---|---|
| [Alignment Tipping Process (ATP)](./2025-atp-alignment-tipping) | 2025 | 持续自进化侵蚀对齐,Agent 滑向不对齐 | Safety · 部署期 · 对齐漂移 |
| [ST-WebAgentBench](./2024-st-webagentbench) | 2024 | Web Agent 安全可信评测:375 任务 + 3057 策略 | Safety · Web · Benchmark |
| [SPC](./2025-spc) | 2025 | 一致性正则化约束自博弈,防止策略退化 | Model · RL · 一致性正则 |
| [TrustAgent](./2024-trustagent) | 2024 | 预训练/提示/控制三模块全流程安全增强 | Safety · 训练-推理-执行 |

## 🏥 What: Specialized Domain(专属域自进化)

| 论文 | 年份 | 域 | 一句话 |
|---|---|---|---|
| [Agent Hospital](./2024-agent-hospital) | 2024 | Medical | 虚拟医院,医生 Agent 从诊疗经验中自主进化 |
| [QuantAgent](./2024-quantagent-strategy) | 2024 | Finance | 多 Agent 自动发现量化交易策略 |
| [EduPlanner](./2025-eduplanner) | 2025 | Education | 多 Agent 对抗迭代优化教学设计 |
| [MedAgentSim](./2024-medagentsim) | 2024 | Medical | 虚拟医院环境,Agent 从诊疗经验自主进化 |
| [EvoPatient](./2024-evopat) | 2024 | Medical | 动态演化患者档案,提升诊断泛化 |
| [DoctorAgent-RL](./2024-doctort-agent-rl) | 2024 | Medical | RL 训练医疗 Agent,优化诊断决策 |
| [OriGene](./2024-origene) | 2025 | Medical | 自进化"虚拟疾病生物学家",自动发现治疗靶点 |
| [AgentCoder](./2024-agentcoder) | 2024 | Coding | 多 Agent 协作生成+测试驱动自修正 |
| [Adaptive Self-Improvement](./2024-adaptive-self-improvement) | 2024 | Coding | 环境反馈驱动 SWE Agent 自适应自改进 |
| [AutoGUI](./2024-autogui) | 2024 | GUI/Web | GUI 操作自解释执行+自纠正 |
| [WebVoyager](./2024-webvoyager) | 2024 | Web | 真实 Web 自主探索+自学习 |
| [ReAP](./2024-reap) | 2024 | GUI/Web | 推理-动作剪枝,Agent 自优化行动策略 |
| [MobileUse](./2024-mobileuse) | 2025 | GUI/Mobile | 多 Agent 协作+经验共享自进化 |
| [Navi](./2025-navi) | 2025 | GUI/Mobile | 视觉-语言导航,失败中学习策略 |
| [TradingAgents](./2025-trading-agents) | 2025 | Finance | 多角色 Agent 市场模拟,盈亏驱动自进化 |
| [Generative Agents](./2023-generative-agents) | 2023 | General | 25 Agent 小镇模拟,记忆驱动涌现行为 |
| [MobileSteward](./2024-mobilesteward) | 2025 | GUI/Mobile | 分层记忆驱动的移动任务自进化 |
| [EvoMAC](./2024-evomac) | 2024 | Coding | 自然选择式自进化多 Agent 协作网络(软件开发) |
| [STELLA](./2025-stella) | 2025 | Education | 自适应语言学习闭环,自评估自改进 |
| [PACE](./2024-pace) | 2024 | Education | 自适应课程生成,AI Tutor 自进化 |
| [i-VIP](./2024-i-vip) | 2024 | Education | AI 导师交互驱动教学策略自进化 |
| [SEFL](./2024-sefl) | 2025 | Education | 自演化反馈闭环,教育 Agent 自改进 |
| [Arxiv Copilot](./2024-arxiv-copilot) | 2025 | Other | 自主研究 Agent,用户反馈驱动自进化 |
| [Agents-of-Change](./2024-agents-of-change) | 2024 | Other | 生态启发 Agent 系统,系统级自进化 |
| [Richelieu](./2024-richelieu) | 2024 | Other | 创意写作 Agent,读者反馈驱动自进化 |
| [AdaPlanner](./2024-adaplanner) | 2023 | Web | 反馈驱动闭环规划,执行中动态重规划 |
| [MathVC](./2024-mathvc) | 2024 | Education | LLM 模拟师生多角色虚拟数学课堂 |
| [UI-Genie](./2024-ui-genie) | 2025 | GUI/Mobile | 自生成指令+自反思迭代提升移动 GUI Agent |

## 📖 Surveys(综述)

| 论文 | 年份 | 定位 |
|---|---|---|
| [A Survey on Self-Evolution of LLMs](./2024-survey-self-evolution-llm) | 2024 | 早期 LLM 自进化综述(自反馈/自训练/自评测) |
| [A Survey of Self-Evolving Agents](./2025-survey-self-evolving-agents) | 2025 | **本仓库 TAXONOMY 主骨架**(What/When/How/Where) |

## 📊 Benchmarks(评测基准)

| 论文 | 年份 | 域 | 侧重 |
|---|---|---|
| [SWE-bench](./2023-swe-bench) | 2023 | Coding | 真实 GitHub issue |
| [AgentBench](./2023-agentbench) | 2023 | General | 综合多环境 |
| [GAIA](./2023-gaia) | 2023 | General | 真实世界多步任务 |
| [LifelongAgentBench](./2025-lifelongagentbench) | 2025 | General | 终身学习 / 抗遗忘 |
| [WebArena](./2023-webarena) | 2023 | Web | 真实 Web 长链路任务 |
| [Agent-SafetyBench](./2024-agent-safetybench) | 2024 | General/Safety | ~349 环境的安全评测 |
| [ST-WebAgentBench](./2024-st-webagentbench) | 2024 | Web/Safety | 375 任务 + 3057 策略的可信评测 |
| [MemoryAgentBench](./2024-memoryagentbench) | 2025 | General/Memory | 增量多轮交互评测长期记忆 |
| [TheAgentCompany](./2025-theagentcompany) | 2025 | General | 模拟公司办公环境全流程评测 |
| [MLE-Bench](./2025-mle-bench) | 2025 | Coding | 75 个 Kaggle 竞赛端到端评测 |
| [SwarmBench](./2025-swarmbench) | 2025 | Multi-Agent | LLM 群体智能五类任务评测 |
| [LTMBenchmark (GoodAI)](./2025-ltmbenchmark) | 2024 | General/Memory | 动态对话式长期记忆与持续学习评测 |

---

## 🗺 收录分布速览

```
各表唯一论文数(跨类重复计入多表,去重后):
  Model 31 · Context 19 · Tool 10 · Arch 20 · Safety 4 · 域专属 28 · 综述 2 · 基准 12
注:跨类条目(Voyager/ST-WebAgentBench 等)在多表重复出现,各表相加 > 去重总数。

类型:  方法类 112 · 综述 2 · 基准 12(去重后共 124 篇)
年份:  2022 ×1 · 2023 ×16 · 2024 ×60 · 2025 ×47(按论文实际发表年份)
```

## ✅ 覆盖体检(对照 TAXONOMY 声明的代表工作)

- Prompt 优化:APE/PromptBreeder/SPO/PromptAgent/DSPy/ProTeGi/ACE ✅
- 工具:Voyager/CREATOR/SkillWeaver/ToolGen/Alita/CRAFT/LearnAct/ToolMem/DRAFT/Live-SWE-Agent ✅
- 多 Agent 架构:GPTSwarm/ADAS/AgentSquare/EduPlanner/QuantAgent/MaAS/ScoreFlow/GiGPO/MASS/ReMA/FlowReasoner/Puppeteer/AutoFlow/Trace/MAS-Zero ✅
- RL 训练:SCoRe/Math-Shepherd/Agent Q/WebRL/TextGrad/DigiRL/RAGEN/AgentTuning/Memory-R1/LADDER/RISE/SPC/Self-Adaptive/AutoRule ✅
- 安全:ATP/Agent-SafetyBench/ST-WebAgentBench/SwarmBench/TrustAgent ✅
- 记忆:Mem0/AWM/ExpeL/A-MEM/Reflexion/Memory-R1/ReasoningBank/MemGen ✅
- 终身学习评测:LifelongAgentBench/MemoryAgentBench/LTMBenchmark ✅
- 域:医疗/金融/教育/GUI/Web ✅(全覆盖)
- 基准:WebArena/TheAgentCompany/MLE-Bench/SwarmBench/MemoryAgentBench ✅

> 本索引已对齐 [TAXONOMY.md](../../docs/TAXONOMY.md) 的所有代表工作分类,覆盖体检齐全。全部条目均含已核验的论文链接(arXiv / bioRxiv);其中 OriGene 发表于 bioRxiv。

## ➕ 如何补充

1. 新建目录 `<year>-<keyword>`(如 `2025-memory-r1`)。
2. 复制任一现有 `README.md` 作为模板,填元信息与维度速查。
3. 在本索引表里加一行,归到对应支柱。
4. 详见 [`CONTRIBUTING.md`](../../CONTRIBUTING.md)。
