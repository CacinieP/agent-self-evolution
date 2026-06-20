# STaR: Bootstrapping Reasoning With Reasoning

- **作者**: Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman (Stanford)
- **发表**: NeurIPS 2022 / arXiv:2203.14465
- **链接**: https://arxiv.org/abs/2203.14465
- **代码**: https://github.com/ezelikman/STaR

## 一句话总结
模型生成推理链(rationalization),只用答对的来微调自己,迭代"用推理教自己推理"。

## 核心方法
循环:用少量示例 prompt 模型对大量问题生成 rationale → 答对的直接用于 SFT;答错的给提示(hint)再生成,若变对则保留 → 微调 → 重复。

## 关键贡献
提出 rationale 自举范式,是 Quiet-STaR、ReST、SPIN 等一众"自生成数据 + 自训练"工作的鼻祖之一。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Inter-test-time × SFT
How:    Imitation(自生成 rationale) · Offline · On-policy · Outcome
Where:  General(推理任务)
Eval:   Generalization, Adaptivity
```

> 个人点评 / 启发 待补充。
