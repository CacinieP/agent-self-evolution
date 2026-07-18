# AgentGen: Enhancing Planning Abilities for LLM-based Agent via Environment and Task Generation

- **作者**: Mengkang Hu, Pu Zhao, Can Xu, Qingfeng Sun, Jianguang Lou, Qingwei Lin, Ping Luo, Saravan Rajmohan
- **发表**: KDD 2025 / arXiv:2408.00764
- **链接**: https://arxiv.org/abs/2408.00764
- **代码**: —

## 一句话总结
用 LLM 自动生成多样化的环境和规划任务,通过指令微调提升 Agent 规划能力。

## 核心方法
用灵感库保证环境多样性 + 双向演化方法(Bi-Evol)自适应任务难度,构建 Agent 训练数据。

## 关键贡献
自生成训练数据使 Llama-3.1-8B 超越 GPT-3.5,70B 达 SOTA,验证"环境生成"作为 Agent 自进化新维度。

## 维度速查 (TAXONOMY)
```
What:   Model(Experience) + Context(自演化课程)
When:   Inter-test-time × SFT
How:    Imitation/Experience · Offline · Mixed · Outcome
Where:  General
Eval:   Generalization
```
