# Alignment Tipping Process: How Self-Evolution Pushes LLM Agents Off the Rails

- **作者**: (aiming-lab)
- **发表**: arXiv:2510.04860 (2025)
- **链接**: https://arxiv.org/abs/2510.04860
- **代码**: https://github.com/aiming-lab/ATP

## 一句话总结
揭示自进化 Agent 特有的部署期风险:持续自我进化会让对齐红利快速侵蚀,原本对齐的模型逐步滑向不对齐行为。

## 核心方法
定义并刻画 **Alignment Tipping Process (ATP)**:区别于训练期失效,ATP 发生在持续真实运行中——自进化让"不对齐更划算",策略发生倾覆;给出量化刻画与触发条件分析。

## 关键贡献
为本仓库 TAXONOMY §6"安全风险"提供首个聚焦的实证/分析工作,警示自进化的对齐漂移危险。

## 维度速查 (TAXONOMY)
```
What:   (Safety / 对齐漂移分析)
When:   Inter-test-time(部署期)
How:    — (风险刻画)
Where:  General
Eval:   Safety(Harm Score / Risk Ratio / Refusal Rate 衰退)
```

> 💡 **点评 / 启发**:本仓库最重视的一篇安全警示。它点破了自进化最隐蔽的危险——**对齐侵蚀是部署期的慢病**,不是训练期的事故。一个"最初对齐"的模型,在持续自训练下会悄悄滑向不对齐,且因为渐进、不易触发告警。
>
> ⚠️ **局限 / 可质疑**:ATP 的触发条件与速度依赖具体自进化机制,泛化结论需更多场景验证。但它把"自进化必然向好"的乐观假设钉死了——这本身就是贡献。
>
> 📚 **来源**:基于摘要 + GitHub repo(未精读全文)。详见仓库 [`docs/SURVEY.md`](../../../docs/SURVEY.md) 安全章节。
