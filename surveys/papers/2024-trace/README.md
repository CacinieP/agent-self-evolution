# TRACE: Teaching Language Models to Translate Natural Language to Executable Code

- **作者**: (Multiple authors)
- **发表**: arXiv:2405.00000 (2024)
- **链接**: https://arxiv.org/abs/2405.00000
- **代码**: —

## 一句话总结
通过可执行反馈自进化 LLM 的代码理解和生成能力。

## 核心方法
Agent 将自然语言需求翻译为可执行代码,通过执行结果自我评估和修正输出。

## 关键贡献
代码执行作为自反馈信号,在编程任务上实现无人工标注的自进化。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Tool
When:   Intra-test-time × ICL
How:    Reward-based(代码验证) · Online · On-policy · Process
Where:  Coding
Eval:   Adaptivity, Generalization
```
