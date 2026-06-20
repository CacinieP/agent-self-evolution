# Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks

- **作者**: (多机构)
- **发表**: NeurIPS 2025 / arXiv:2501.11733
- **链接**: https://arxiv.org/abs/2501.11733
- **代码**: —

## 一句话总结
分层多 Agent 移动助手,通过长期记忆从过往经验中自我进化,完成复杂长程手机任务。

## 核心方法
分层多 Agent 协作(Manager / Decision / Actuator / Reflector / Notetaker)+ 长期记忆系统:把洞察与短期反思沉淀进记忆,后续任务复用经验自适应校准行为。

## 关键贡献
在复杂、长程移动任务上超越此前 SOTA,是"应用域(移动 GUI)+ 记忆进化"自进化的代表。

## 维度速查 (TAXONOMY)
```
What:   Context(Memory) + Architecture(Multi-Agent)
When:   Inter-test-time × ICL
How:    Imitation(经验沉淀) · Online · On-policy · Outcome
Where:  Specialized(GUI / Mobile)
Eval:   Adaptivity, Retention
```

> 💡 **点评 / 启发**:分层多 Agent(Manager/Decision/Actuator/Reflector/Notetaker)+ 长期记忆,把"复杂长程任务"拆解为角色分工 + 经验沉淀,是 GUI 域自进化的成熟工程方案。
>
> ⚠️ **局限 / 可质疑**:多 Agent 协作的通信开销大;角色划分是人工预设的,未必最优。移动 GUI 的碎片化(Android 版本/厂商定制)限制泛化。
>
> 📚 **来源**:基于摘要 + NeurIPS 2025 转述(未精读全文)。
