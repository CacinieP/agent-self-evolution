# Self-Instruct: Aligning Language Models with Self-Generated Instructions

- **作者**: Yizhong Wang, Yufei Wang, et al. (AllenAI)
- **发表**: ACL 2023 / arXiv:2212.10560
- **链接**: https://arxiv.org/abs/2212.10560
- **代码**: https://github.com/yizhongw/self-instruct

## 一句话总结
让 LLM 用少量种子指令自我生成大规模指令数据并微调自身,降低指令数据对人工标注的依赖。

## 核心方法
种子指令 → 模型生成新指令与实例 → 过滤(去重 / 去低质 / 去 ROUGE 冲突)→ 微调;可迭代。

## 关键贡献
开创"自生成训练数据"范式,是后续 SPIN / Self-Rewarding / Self-Evolving 的方法论源头之一。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(数据)
When:   Inter-test-time × SFT
How:    Imitation(自生成示教) · Offline · On-policy · Outcome
Where:  General
Eval:   Generalization(SuperNaturalInstructions)
```

> 个人点评 / 启发 待补充。
