# ToolGen: Unified Tool Retrieval and Calling via Generation

- **作者**: Yuxiang Wang, Mingbao Han et al.
- **发表**: arXiv:2410.03439 (2024)
- **链接**: https://arxiv.org/abs/2410.03439
- **代码**: https://github.com/Reason-Wang/ToolGen

## 一句话总结
把每个工具表示成唯一 token 融进 LLM 参数,让"工具检索"与"工具调用"统一为一次生成,摆脱外部检索模块。

## 核心方法
三阶段训练:① 工具记忆化(每个工具分配并学习一个 token)→ ② 检索训练(学到何时调出对应工具 token)→ ③ Agent 训练(端到端做工具调用 + 语言生成)。

## 关键贡献
把海量工具知识"内化"进模型参数,实现可扩展的工具选择,是 Tool/Select 方向规模化代表。

## 维度速查 (TAXONOMY)
```
What:   Tool(Select) + Model
When:   Inter-test-time × SFT/RL
How:    Imitation + Reward-based · Offline · On-policy · Outcome
Where:  General(工具调用)
Eval:   Adaptivity, Generalization
```

> 个人点评 / 启发 待补充。
