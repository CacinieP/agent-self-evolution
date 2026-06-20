# Automate Strategy Finding with LLM in Quant Investment (QuantAgent)

- **作者**: (量化研究团队)
- **发表**: arXiv:2409.06289 (2024)
- **链接**: https://arxiv.org/abs/2409.06289
- **代码**: —

## 一句话总结
风险感知的三阶段多 Agent 框架,用 LLM 自动发现量化交易策略:信号抽取 → 组合构建 → 风险对齐。

## 核心方法
三阶段:LLM 提取金融信号 → 组合构建 → 风险感知的多 Agent 系统迭代优化策略;将 LLM 能力扩展到量化交易的可扩展架构。

## 关键贡献
金融域 LLM Agent 自进化的代表,展示从信号到组合的端到端自动化策略发现。

## 维度速查 (TAXONOMY)
```
What:   Architecture(Multi-Agent) + Context(策略记忆)
When:   Inter-test-time × ICL
How:    Reward-based(回测收益/风险) · Online · On-policy · Outcome
Where:  Specialized(Finance / Quant)
Eval:   Adaptivity(回测表现), Efficiency
```

> 💡 **点评 / 启发**:三阶段(信号抽取→组合→风险对齐)把量化研究的流程 Agent 化,风险感知的多 Agent 设计点出了金融域的关键约束——不只看收益,要看风险调整后收益。
>
> ⚠️ **局限 / 可质疑**:量化策略极易过拟合历史数据,自进化生成的策略在样本外是否有效是核心疑问,论文需更多 out-of-sample 证据。金融域回测可信度历来存疑。
>
> 📚 **来源**:基于摘要(未精读全文)。
