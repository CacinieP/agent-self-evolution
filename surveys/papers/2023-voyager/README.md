# Voyager: An Open-Ended Embodied Agent with Large Language Models

- **作者**: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Shi, Anima Anandkumar (NVIDIA / Caltech)
- **发表**: arXiv:2305.16291
- **链接**: https://arxiv.org/abs/2305.16291
- **代码**: https://github.com/MineDojo/Voyager

## 一句话总结
Minecraft 中的 LLM 终身学习 Agent:自动生成课程、写代码技能、把成功技能存进可复用的技能库。

## 核心方法
三大组件:自动课程(生成探索目标)+ 技能库(代码化技能 + 语义检索)+ 迭代提示(执行失败后用环境反馈修正代码)。

## 关键贡献
首个 LLM 驱动的开放式终身学习 Agent,展示"技能积累 → 解锁更难任务"的正反馈飞轮。

## 维度速查 (TAXONOMY)
```
What:   Tool(Create/Master) + Context(Memory / 技能库)
When:   Inter-test-time × ICL
How:    Reward-based(环境执行反馈) · Online · On-policy · Outcome
Where:  General(Embodied / Minecraft)
Eval:   Adaptivity, Retention(新物品/科技树解锁数)
```

> 个人点评 / 启发 待补充。
