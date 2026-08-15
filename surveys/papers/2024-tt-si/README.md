# Self-Improving LLM Agents at Test-Time

- **作者**: Emre Can Acikgoz et al.
- **发表**: arXiv:2510.07841 (2025)
- **链接**: https://arxiv.org/abs/2510.07841
- **代码**: —

## 一句话总结
Agent 在测试阶段自我积累经验并改进,无需构建大规模训练集。

## 核心方法
推理过程中对自身输出进行评价与修正,通过迭代改进提升单次任务表现,无需参数更新。

## 关键贡献
摆脱"大数据微调"范式的测试时自我改进,在多 benchmark 上稳定提升。

## 维度速查 (TAXONOMY)
```
What:   Model(Policy) + Context(Memory)
When:   Intra-test-time × ICL
How:    Reward-based(自评) · Online · On-policy · Process
Where:  General
Eval:   Adaptivity, Efficiency
```
