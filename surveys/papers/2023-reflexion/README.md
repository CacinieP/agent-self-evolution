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

> 💡 **点评 / 启发**:把"强化学习"从梯度/标量奖励解放成"自然语言反馈",是 In-Context 进化的奠基之作。关键洞察:语言反馈比 scalar reward 信息密度高得多——一句"你上次漏读了表格第二列"远胜一个 -1。
>
> ⚠️ **局限 / 可质疑**:反思只在"有明确成败信号"的任务(代码/问答)上有效;开放生成任务上自反思常流于空泛,甚至越改越差(后被 SCoRe 等指出"无训练的自纠正不可靠")。
>
> 📚 **来源**:精读原文 + 仓库 reflexion 原型实践。
