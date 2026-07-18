# Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking

- **作者**: Eric Zelikman, Georges Harik, Yijia Shao, Varuna Jayasiri, Nick Haber, Noah D. Goodman
- **发表**: arXiv:2403.09629 (2024)
- **链接**: https://arxiv.org/abs/2403.09629
- **代码**: https://github.com/ezelikman/quiet-star

## 一句话总结
LLM 在继续预训练中自主学习在每个 token 前生成内部推理(thought),提升零样本推理能力。

## 核心方法
训练模型在每次预测前自先生成 hidden thought,用 next-token prediction loss 作为奖励驱动 thought 质量改进;通过 REINFORCE 处理 thought 位置的稀疏奖励。

## 关键贡献
首次实现无需任务数据的自教推理(零样本),GSM8K 从 5.9%→10.9%,为 test-time 自进化奠定基础。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT/RL
How:    Reward-based(预测损失) · Offline · On-policy · Hybrid
Where:  General(推理)
Eval:   Generalization
```
