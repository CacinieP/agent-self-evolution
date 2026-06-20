# Reflexion: Language Agents with Verbal Reinforcement Learning

- **作者**: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **发表**: NeurIPS 2023 / arXiv:2303.11366
- **链接**: https://arxiv.org/abs/2303.11366
- **代码**: https://github.com/noahshinn/reflexion

## 一句话总结
Agent 不更新权重,而是把每次尝试后的"口头自我反思"写入记忆,后续试验中据此避免重复犯错。

## 核心方法
失败后由自身生成自然语言反思,作为额外记忆条目注入下一轮上下文,实现"语言化强化学习"。

## 关键贡献
证明 in-context 的语言反馈即可显著提升 Agent 在 AlfWorld / HotPotQA / HumanEval 等任务的表现,开启 self-reflection 范式。

## 维度速查 (TAXONOMY)
```
What:   Context / Memory (反思记忆)
When:   Intra-test-time × ICL
How:    Reward-based(语言反馈) · Online · On-policy · Outcome
Where:  General
Eval:   Adaptivity(AlfWorld, HotPotQA, HumanEval)
```

> 个人点评 / 启发 待补充。
