# Recursive Introspection: Teaching Language Model Agents How to Self-Improve (RISE)

- **作者**: Yuxiao Qu et al.
- **发表**: arXiv:2407.18219 (2024, NeurIPS 2024)
- **链接**: https://arxiv.org/abs/2407.18219
- **代码**: —

## 一句话总结
把多轮自我改进建模为在线多轮 RL,训练模型在测试时"递归内省"持续改进自身输出。

## 核心方法
自模仿蒸馏 + 重要性采样处理自生成数据的分布失配,将弱基座模型转化为多轮自我改进的推理器。

## 关键贡献
Llama2/3、Mistral 等模型随轮数增加持续提升数学推理表现,优于自一致性等策略。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy)
When:   Intra-test-time × RL
How:    Reward-based(RL) · Online · On-policy · Process
Where:  General(推理)
Eval:   Adaptivity, Retention
```
