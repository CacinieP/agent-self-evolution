# Large Language Models Are Human-Level Prompt Engineers (APE)

- **作者**: Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan, Jimmy Ba (UofT)
- **发表**: ICLR 2023 / arXiv:2211.01910
- **链接**: https://arxiv.org/abs/2211.01910
- **代码**: https://github.com/keirp/open_fewshot

## 一句话总结
把指令生成当成"自然语言程序合成":用 LLM 从输入-输出示例生成候选指令,再按表现筛选出最佳 prompt。

## 核心方法
从少量样例反向生成候选指令 → 在保留集上用打分函数(对数似然/准确率)评估 → 选最优指令;可用迭代式蒙特卡洛搜索进一步优化。

## 关键贡献
开创"自动 prompt 工程"范式,证明 LLM 生成的指令可达到甚至超过人工水平,是 Prompt 优化方向的奠基工作。

## 维度速查 (TAXONOMY)
```
What:   Context(Prompt Optimization)
When:   Inter-test-time
How:    Reward-based(打分函数) · Offline · On-policy · Outcome
Where:  General
Eval:   Adaptivity, Generalization
```

> 个人点评 / 启发 待补充。
