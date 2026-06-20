# AgentBench: Evaluating LLMs as Agents

- **作者**: Xiao Liu et al. (Tsinghua / 智谱)
- **发表**: ICLR 2024 / arXiv:2308.03688
- **链接**: https://arxiv.org/abs/2308.03688
- **代码**: https://github.com/THUDM/AgentBench

## 一句话总结
系统化、多环境(OS / DB / Web / 知识图谱 / 卡片游戏等)的 Agent 综合能力评测基准。

## 核心方法
在多类交互环境中部署统一评测协议,衡量 LLM 作为 Agent 在多轮决策 / 工具使用上的表现。

## 关键贡献
提供 LLM Agent 综合能力的横向对比基线,是 Agent 自进化工作常用的泛化评测之一。

## 维度速查 (TAXONOMY)
```
What:   (Benchmark)
When:   —
How:    —
Where:  General
Eval:   Generalization, Adaptivity(综合)
```

> 💡 **点评 / 启发**:8 类交互环境(OS/DB/Web/KG/游戏)的统一评测协议,首次给了 LLM Agent 综合能力的横向标尺。多环境设计本身就在呼吁"别只在一个域上自吹自擂"。
>
> ⚠️ **局限 / 可质疑**:环境覆盖虽广但每个深度有限;仍是 episodic 单点评测,无成长维度。部分环境已略显陈旧(被更专的基准如 SWE-bench/WebArena 超越)。
>
> 📚 **来源**:基于摘要(未精读全文)。
