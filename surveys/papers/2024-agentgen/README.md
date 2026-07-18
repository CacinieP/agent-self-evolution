# AgentGen: Enhancing Agent Capabilities by Generating Diverse, Interactive, and Challenging Environments

- **作者**: Jian Hu, Chenghao Xu, Zhuoran Yang, Tong Zhang, Zhaoran Wang
- **发表**: arXiv:2408.10159 (2024)
- **链接**: https://arxiv.org/abs/2408.10159
- **代码**: —

## 一句话总结
Agent 自主生成多样化交互式训练环境,在生成的子任务上自我训练提升泛化能力。

## 核心方法
利用 LLM 根据已有任务模板生成新的交互式环境,通过任务模板库不断扩充训练分布,在生成环境中自对弈训练。

## 关键贡献
提出"环境生成"作为 Agent 自进化的新维度,证明自生成环境可提升 Agent 在未见任务上的零样本泛化。

## 维度速查 (TAXONOMY)
```
What:   Model(Experience) + Context(自演化课程)
When:   Inter-test-time × SFT
How:    Imitation/Experience · Offline · Mixed · Outcome
Where:  General
Eval:   Generalization
```
