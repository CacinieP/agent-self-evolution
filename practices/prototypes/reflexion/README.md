# Prototype: Reflexion(最小可运行原型 — 环境反馈版)

> 对应论文:[Reflexion: Language Agents with Verbal Reinforcement Learning](../../../surveys/papers/2023-reflexion)(NeurIPS 2023)
> TAXONOMY 定位:`What: Context/Memory · When: Intra-test-time × ICL · How: Reward-based(环境反馈)`

## 🎯 这个原型做什么

复现 Reflexion 的核心机制,并突出它与 [Self-Refine](../self_refine) 的关键区别:

| | Self-Refine | **Reflexion(本原型)** |
|---|---|---|
| 反馈来源 | 模型**自评** | **环境真实执行**(运行 Python 代码跑测试) |
| 记忆 | 单轮内 | **跨试验持久化**,历史反思不断累积复用 |

场景:给 Agent 一个编程题,它要写出能通过测试的代码。
```
试验 i: act(带历史反思写代码) → 环境执行跑测试 → 失败则 reflect(生成反思存入 memory) → 试验 i+1
```

## 📁 文件

| 文件 | 说明 |
|---|---|
| [`reflexion.py`](./reflexion.py) | 主程序,单文件 |
| `requirements.txt` | 真实模型模式需要 `openai` |

## 🚀 快速开始

```bash
# 离线 mock(无需 API,可观察"失败→反思入记忆→下次成功"的飞轮)
python reflexion.py --mock --task "写函数 is_prime(n): 判断 n 是否为素数" --trials 3

# 真实模型
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
python reflexion.py --task "写函数 is_prime(n): 判断 n 是否为素数" --trials 3 --allow-unsafe-exec
```

> 当前 CLI 的内置评测固定调用 `is_prime(n)`；若要换题,请同步替换代码中的 `DEFAULT_TESTS`。真实模型模式必须显式添加 `--allow-unsafe-exec`。

## 🧠 实现要点

- **真实环境反馈**:`run_tests()` 在带超时的独立 Python 子进程中执行代码并跑测试,失败诊断作为反馈信号。
- **记忆跨试验**:`memory: list[str]` 在所有试验间持久,每次 `act` 都把历史反思注入提示。
- **代码提取**:用正则从模型回复中抽取 ```` ```python ``` ```` 代码块,容错裸代码。
- **早停**:一旦某试验通过即终止,避免浪费。

## 🔧 可玩的扩展方向

1. **换场景**:把 `run_tests` 换成网页/数据库任务的环境执行器,变成 GUI/SQL 版 Reflexion。
2. **记忆管理**:给反思加相关度检索或容量上限(避免无限增长),即向 Voyager 技能库靠拢。
3. **对比评测**:对比 `--trials 1`(单次尝试,尚无历史反思)与 `--trials 3`(可复用失败反思)的通过率。
4. **与 Self-Refine 串联**:先自评微调,再环境反馈,体会两种反馈的差异。

## ⚠️ 安全提示

`run_tests()` 仍会使用 `exec/eval` 执行模型生成的代码。独立子进程与超时只能隔离崩溃和死循环,**不构成安全沙箱**。真实模型模式因此要求显式传入 `--allow-unsafe-exec`;仍请只在容器或受限解释器中运行不受信任代码。

## 📐 维度速查(TAXONOMY)

```
What:   Context / Memory (反思记忆)
When:   Intra-test-time × ICL
How:    Reward-based(环境执行反馈) · Online · On-policy · Outcome
Where:  General(编程)
Eval:   Adaptivity(测试通过率)
```
