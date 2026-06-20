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

> 个人点评 / 启发 待补充。
