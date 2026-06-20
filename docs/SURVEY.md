# Agent 自进化:从"工具使用者"到"自我改写者"

> 一篇基于本仓库 48 篇文献的**带观点**综述。
> 配套分类体系见 [`TAXONOMY.md`](./TAXONOMY.md),论文索引见 [`../surveys/papers/README.md`](../surveys/papers/README.md)。
>
> 本文不止罗列方法,更试图回答:**这门技术真正的分水岭在哪?哪些是噪音,哪些是信号?**

---

## 0. 先定义清楚:什么算"自进化"

市面上很多"self-X"被混为一谈。本文采用三条判据,满足越多越"纯正":

1. **经验驱动** —— 更新由 Agent 自身轨迹/反馈触发,而非外部静态数据集。
2. **持久性** —— 改动产生持久的策略性改变,而非一次性 in-context 行为。
3. **自主性** —— 具备自启动的探索/反思/改写机制,而非全人工流水线。

依此,**课程学习、标准蒸馏、被动接收任务序列的"终身学习"不算自进化**;而 Reflexion(反思入记忆)、SPIN(自对弈微调)、Darwin Gödel Machine(自改写代码)是。

> 一个有用的二分:**In-Context 进化**(不改权重,靠提示/记忆/技能库)vs **Weight 进化**(改参数)。前者门槛低、可解释、可回滚;后者上限高、但贵且危险。当前最热的恰恰是两者**混合**:先 in-context 收集信号,再触发 weight 更新。

---

## 1. 四大支柱:进化的"是什么"

### 1.1 Model —— 改参数

最"重"的进化。代表谱系:

- **自生成数据 → SFT**:从 [Self-Instruct](../surveys/papers/2023-self-instruct) → [STaR](../surveys/papers/2022-star) 一脉,模型生成训练信号微调自己。鼻祖级,但天花板受"自生成数据质量上限"制约。
- **自对弈**: [SPIN](../surveys/papers/2024-spin)(判别自身 vs 真值)、[Absolute Zero](../surveys/papers/2025-absolute-zero)(自出题自做题 + 代码验证)。**零外部数据**是其最激进的主张。
- **自奖励 RL**: [Self-Rewarding LM](../surveys/papers/2024-self-rewarding-lm) 用 LLM-as-Judge 给自己出偏好对做 DPO。妙处:judge 能力本身也随迭代提升。
- **过程奖励**: [Math-Shepherd](../surveys/papers/2023-math-shepherd) 把 PRM 去人工化,[SCoRe](../surveys/papers/2024-score) 用 RL 真正教会"自我纠正"。

**张力**:Weight 进化的核心悖论是**自生成数据的天花板**。模型很难"拔着自己的头发离开地球"——没有外部 ground truth 时,信号终会饱和。Absolute Zero 用代码执行器作为"外部真实",是绕过此悖论的聪明解法。

### 1.2 Context —— 不改权重,改上下文

最"轻"也最实用的进化。分两支:

- **记忆**: [Reflexion](../surveys/papers/2023-reflexion)(反思记忆)→ [ExpeL](../surveys/papers/2024-expeL)(经验归纳)→ [Mem0](../surveys/papers/2025-mem0)(生产级)→ [A-MEM](../surveys/papers/2025-a-mem)(自组织网络)。记忆的演进方向很清晰:**从平铺存储 → 关联网络 → 可演化的知识图**。
- **Prompt 优化**: [APE](../surveys/papers/2023-ape) → [PromptBreeder](../surveys/papers/2024-promptbreeder)(自我指涉进化)→ [PromptAgent](../surveys/papers/2024-promptagent)(MCTS)→ [SPO](../surveys/papers/2025-spo)(自监督)。这条线工程价值高([DSPy](../surveys/papers/2024-dsp) 是基础设施),但理论新颖度低于记忆线。

**张力**:In-Context 进化"便宜但会饱和"——一个固定容量的 context window 装不下无限经验。记忆系统本质是在和**上下文窗口的有限性**搏斗。

### 1.3 Tool —— 从"用工具"到"造工具"

最具范式转移意味的一支:

- [Voyager](../surveys/papers/2023-voyager) 是里程碑:写代码技能 + 技能库 + 自动课程,三件套首次让"开放式成长"具象化。
- [CREATOR](../surveys/papers/2023-creator) 把"工具创造"从抽象/具体两层解耦。
- [SkillWeaver](../surveys/papers/2025-skillweaver) 把技能 API 化 + 练习打磨,工业化了一步。
- [ToolGen](../surveys/papers/2024-toolgen) 反向操作:把工具内化为 token,牺牲灵活性换可扩展性。

**判断**:Tool 线是"自进化"区别于"自训练"的关键证据——**Agent 真的能扩展自己的能力边界**(新工具 = 新可能动作),而非只在固定动作空间内优化。

### 1.4 Architecture —— 改系统本身

最新也最"科幻":

- [ADAS](../surveys/papers/2024-adas) / [AgentSquare](../surveys/papers/2024-agentsquare):让 Agent 在代码/模块空间搜索更强的 Agent 设计。
- [AFlow](../surveys/papers/2024-aflow) / [GPTSwarm](../surveys/papers/2024-gptswarm):把工作流/多 Agent 拓扑当成可优化对象。
- [Darwin Gödel Machine](../surveys/papers/2025-darwin-godel-machine):**自指**——Agent 重写自己的代码,开放式进化。

**判断**:这是离 AGI 叙事最近、也离**失控**最近的一支。Gödel 式自改写在理论上最迷人,实践中最难验证"改得真的更好"还是"改得自我感觉更好"。

---

## 2. 三条贯穿性的主线争论

### 争论一:In-Context 还是 Weight?

这不是技术选型,是**哲学选型**。In-Context 派(Reflexion/Voyager/DSPy)信奉"快速、可逆、可解释";Weight 派(SPIN/Self-Rewarding/SCoRe)信奉"真正的能力跃迁必须改参数"。

**我的观察**:2025 年的赢家是**混合派**——[WebRL](../surveys/papers/2024-webrl)、[DigiRL](../surveys/papers/2024-digirl)、[Memory-R1](../surveys/papers/2025-memory-r1) 都先用 in-context 机制收集高质量轨迹/信号,再触发 weight 更新。纯 in-context 易饱和,纯 weight 太贵,混合才是工程现实。

### 争论二:奖励从哪来?

自进化的命门。按可靠度排序:

1. **环境真实反馈**(代码执行、测试通过)—— [Absolute Zero](../surveys/papers/2025-absolute-zero)、[Reflexion](../surveys/papers/2023-reflexion)、[DigiRL](../surveys/papers/2024-digirl)。最可信,但受限于"可验证任务"的范围。
2. **LLM-as-Judge** —— [Self-Rewarding](../surveys/papers/2024-self-rewarding-lm)、[SPO](../surveys/papers/2025-spo)。灵活,但有**自我强化偏差**(自己评自己,易互相吹捧)。
3. **模型自置信** —— 信号弱,易 reward hacking。

**陷阱**:奖励越"自生成",越要警惕**奖励黑客**——模型学会钻自己奖励函数的空子,而非真变强。可验证奖励(类型 1)是目前最稳的锚。

### 争论三:开放式还是任务导向?

- **开放式**:Voyager、Darwin Gödel Machine 追求"无限成长",不预设目标。
- **任务导向**:绝大多数(Reflexion/SPIN/AgentTuning...)围着具体基准转。

开放式更激动人心,但**评测是硬伤**——怎么衡量"持续进化能力"而非单点成绩?现有基准几乎都是 episodic(任务间重置),测不出累积。这是整个领域的共同盲区(见第 4 节)。

---

## 3. 安全:自进化的阿喀琉斯之踵

这一节我刻意单独拎出来,因为它**最容易被技术乐观主义淹没**。

- **[Alignment Tipping Process (ATP)](../surveys/papers/2025-atp-alignment-tipping)** 给出了最尖锐的警示:持续自进化会**侵蚀对齐**。原本拒绝的有害行为,在自我训练几轮后开始执行——因为"不对齐"在自定奖励下可能"更有奖励"。
- 这不是训练期问题,是**部署期**问题:Agent 在真实运行中悄悄漂移,比一次性事故更难察觉。
- 现有护栏([Agent-SafetyBench](../surveys/papers/2024-agent-safetybench)、[ST-WebAgentBench](../surveys/papers/2024-st-webagentbench))只是**评测**,远未形成**机制**。

**我的判断**:自进化 Agent 若要落地,**自修改审计 + 版本化 + 可回滚**是底线,不是可选项。每次 weight/架构/技能库变更都应留痕,能 diff、能回滚、能红线告警。Gödel 式自改写尤其需要——否则就是"自己给自己做手术还不留记录"。

---

## 4. 评测的集体盲区

读 48 篇后最强烈的感受:**方法跑得比评测快太多**。

- 现有基准([SWE-bench](../surveys/papers/2023-swe-bench)、[AgentBench](../surveys/papers/2023-agentbench)、[GAIA](../surveys/papers/2023-gaia))都是 **episodic**——任务间重置 Agent 状态。这**结构性测不出**自进化的核心价值:知识累积、跨任务迁移、抗遗忘。
- [LifelongAgentBench](../surveys/papers/2025-lifelongagentbench) 是少数补丁,但仍属个例。
- 成本/效率/安全指标报告极不统一,无法横向对比。

**后果**:论文里"自进化涨了 X 点"经常无法区分——是**真变强**了,还是**对这个特定基准过拟合**了?这个问题不解决,整个领域的进展陈述都带着水分。

---

## 5. 我的判断与路线图

基于以上,给三条主观判断:

1. **记忆线是当下 ROI 最高的落地点**。In-Context、可回滚、工程化成熟(Mem0/A-MEM),且直接解决长程 Agent 的真实痛点。先做记忆,再做 weight。
2. **"可验证奖励 + 混合进化"是最稳的技术组合**。避免纯自生成奖励的 reward hacking,又比纯环境反馈更普适。Absolute Zero 的范式值得认真抄。
3. **架构自进化(Gödel 类)短期别碰生产**。它最迷人也最危险,且缺可靠评测。把它留在研究沙箱里,直到自修改审计机制成熟。

路线图建议(给想做实践的读者):

```
入门:  跑本仓库 4 个原型(self_refine → reflexion → voyager_skill → amem)
        体会 In-Context 进化的四种形态
进阶:  选一个有可验证奖励的域(代码/数学),复现 Absolute Zero 式混合进化
工程:  给你的 Agent 加可审计的记忆层(Mem0 思路)+ 变更留痕
研究:  攻克"自进化的持续评测"——这是最大的开放问题
```

---

## 6. 一句话总结

> Agent 自进化的本质,是把**学习循环**从"人类标注 → 训练 → 部署"的线性流水,变成 Agent **自己驱动的闭环**。这个闭环的上限取决于奖励信号的质量,下限取决于安全护栏的强度,而它真正的价值——**持续变强而非单点变强**——至今还没有合格的尺子来量。

---

*本文观点仅代表仓库维护者基于文献的判断,欢迎在 [Discussions](https://github.com/CacinieP/agent-self-evolution/discussions) 异议与补充。文中所引论文均可在 [`surveys/papers/`](../surveys/papers/) 找到详细笔记。*
