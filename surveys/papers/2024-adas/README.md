# Automated Design of Agentic Systems (ADAS / Meta Agent Search)

- **作者**: Shengran Hu, Cong Lu, Jeff Clune (UBC)
- **发表**: ICLR 2025 / arXiv:2408.08435
- **链接**: https://arxiv.org/abs/2408.08435
- **代码**: https://github.com/ShengranHu/ADAS

## 一句话总结
用元 Agent 在"代码空间"里迭代编程出全新的 Agent 系统设计,自动发现比人工更强且可迁移的架构。

## 核心方法
ADAS 三要素:搜索空间(以代码定义 Agent 系统)+ 元 Agent Search(让一个 LLM Agent 在代码空间生成/改进设计)+ 评估;保留发现的 archive 并让 meta-agent 据此进化。

## 关键贡献
把"Agent 架构设计"本身变成可被 Agent 自主优化的对象,是系统级自进化的里程碑。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Single + Multi Agent)
When:   Inter-test-time
How:    Population(Evolutionary) · Online · On-policy
Where:  General
Eval:   Generalization, Adaptivity(跨任务/模型迁移)
```

> 💡 **点评 / 启发**:把"设计 Agent 架构"这件最依赖人类直觉的事,变成可被 Agent 自己搜索的代码空间。范式级启发:**meta-agent 是一个新的进化对象层级**。
>
> ⚠️ **局限 / 可质疑**:搜索空间被"代码即配置"框定,发现的"新架构"多是已知模块的新组合,而非真正新颖的机制。评估用小任务集,发现的架构泛化性存疑。
>
> 📚 **来源**:基于原文摘要 + 方法节精读 + OpenReview 讨论。
