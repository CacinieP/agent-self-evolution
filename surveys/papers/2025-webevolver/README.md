# WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model

- **作者**: T. Fang et al.
- **发表**: EMNLP 2025 / arXiv:2504.21024
- **链接**: https://arxiv.org/abs/2504.21024
- **代码**: —

## 一句话总结
引入一个与 Agent 协同进化的"世界模型"LLM,提升 Web Agent 自我改进的数据质量与效果。

## 核心方法
Agent 自训练同时,World Model LLM 与之协同进化,为自训练提供更可靠的环境模拟/反馈,缓解自训练中数据与环境受限的瓶颈。

## 关键贡献
在 Mind2Web-Live / WebVoyager / GAIA-web 上比既有自进化 Agent 提升约 10%,是 Web 域自进化的代表。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(World Model)
When:   Inter-test-time × SFT/RL
How:    Population(Coevolution) · Offline-Online · Mixed · Outcome
Where:  Specialized(Web / GUI)
Eval:   Adaptivity, Generalization
```

> 💡 **点评 / 启发**:协同进化的世界模型是亮点——Agent 自训练时,一个建模环境的 LLM 与之共进化,提供更丰富的反馈,缓解自训练数据/环境受限的瓶颈。+10% 的提升说明"世界模型当陪练"有效。
>
> ⚠️ **局限 / 可质疑**:世界模型本身可能学错,错误反馈会带偏 Agent;协同进化若两个模型互相确认偏差,会一起跑偏。增益集中在特定基准。
>
> 📚 **来源**:基于摘要 + EMNLP 2025 转述(未精读全文)。
