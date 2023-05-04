# TryMore GPT

TryMore GPT-7B/13B，是由揣摩研习社一个开源的聊天机器人，本项目以LLaMA作为基座模型，使用Vicuna训练框架，在shareGPT，Alpaca中英数据集，COIG中通用价值观，代码编写数据集完成指令微调。在中文表现上相较于原始Vicuna以及一众中文聊天机器人有具有非常有竞争力的表现。

## Release

<p align="center">
<a href=""><img src="img/logo.png" width="40%"></a>

## Contents
- [数据集](#数据集)
- [测试样例](#model-weights)

## 数据集

### Share GPT
使用Share GPT数据集，并对数据集进行简单清洗，然后仅保留数据集中中文和英文两种语言数据。Share GPT主要为真实人类和chatGPT聊天对话场景，该数据集模拟了OpenAI在InstructGPT中针对用户实际使用场景编写指令微调数据集的过程。Vicuna的成功说明了，该数据集使得模型解锁了多轮对话能力和指令遵循能力。

### Alpaca-GPT4
该数据集以Self-instruct的方法在GPT-4模型中蒸馏出5.2W条英文数据，和5.2W条中文数据。相较于Share GPT数据，Alpaca-GPT4数据集覆盖大量问答数据集，该数据集训练模型用一句话更精确详细的回复问题。

### COIG
主要是使用COIG数据集中的人类价值观对齐指令数据集和Leetcode指令数据集。人类价值观对齐指令是中文世界共享人类价值观的样本。作者选择了50个指令作为扩充种子，并使用中文世界通用的价值观对齐样本，生成了3000个结果指令。代码指令的任务可能有助于LLM能力的涌现，作者从CC-BY-SA-4.0许可下的2,589个编程问题中构建Leetcode指令。这些问题包含问题描述、多种编程语言和解释。

## 测试样例

### 计算题
<a href=""><img src="img/example_0.png" width="100%"></a>

### 角色扮演
<a href=""><img src="img/example_2.png" width="100%"></a>

### 人类价值观问答
<a href=""><img src="img/example_3.png" width="100%"></a>

### 其它
<a href=""><img src="img/example_1.png" width="100%"></a>
