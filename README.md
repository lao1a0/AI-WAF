# AI WAF

这是一个基于AI的waf小demo，曾经护网收集到了一批绿盟isop上的输出报告，因此恶意样本是来源于此，模型训练的目标是能够对这一批http流量包进行自动化识别。

# 文件介绍

`file`：存放训练好的模型（太大了，我没上传）

`data`：用于训练的数据源，其中`Flow cleaning.py`是用于清洗流量的

 `model_dataSource.py`：用于生成训练数据

 `model_training.py`：用于模型训练

`model_retraining.py`：用于二次训练

`model_prediction.py`：用于预测

# 日志

2023-10-09：

用的模型`LogisticRegression`，在训练的时候能够到达`acc=1`，但是进行预测的时候最只识别出来了`21/77`。感觉模型的能力已经到达极限了。

# 参考

[exp-db/AI-Driven-WAF: Artificial intelligence-driven Web Firewall (github.com)](https://github.com/exp-db/AI-Driven-WAF)

[jackaduma/AI-WAF: AI driven Web Application Firewall (github.com)](https://github.com/jackaduma/AI-WAF)

# NLP模型概要

[解读NLP深度学习的各类模型 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/58931044)，20个比较流行的NLP模型：

- ==[词嵌入模型，例如 Word2Vec 和 GloVe。这些模型可以将自然语言中的单词映射到实数向量空间，从而表示单词的语义和关系](https://zhuanlan.zhihu.com/p/58931044)[1](https://zhuanlan.zhihu.com/p/58931044)。==
- [递归神经网络（RNN），例如 ELMo 和 BERT。这些模型可以将文本视为一系列单词，旨在捕获文本单词依赖关系和文本结构](https://zhuanlan.zhihu.com/p/58931044)[1](https://zhuanlan.zhihu.com/p/58931044)[2](https://zhuanlan.zhihu.com/p/354221239)。
- [序列标注模型，例如条件随机场（CRF）和隐马尔可夫模型（HMM）。这些模型可以对文本中的每个单词或片段进行分类，如命名实体识别、词性标注等](https://zhuanlan.zhihu.com/p/58931044)[1](https://zhuanlan.zhihu.com/p/58931044)[3](https://bing.com/search?q=NLP方面的流行的模型)。
- [机器翻译模型，例如 Google Translate 和 Microsoft Translator。这些模型可以将一种自然语言翻译成另一种自然语言，如中文翻译成英文](https://zhuanlan.zhihu.com/p/58931044)[4](https://blog.csdn.net/weixin_42611177/article/details/129551735)。
- ==自然语言生成模型，例如 GPT 和 Transformer。这些模型可以根据给定的输入或上下文生成自然语言文本，如写作、对话、摘要等 。==
- 情感分析模型，例如 VADER 和 SentiWordNet。这些模型可以检测文本中的情感倾向和极性，如正面、负面或中性 。
- ==句子相似度模型，例如 Siamese LSTM 和 Deep Averaging Network。这些模型可以计算两个句子之间的语义相似度或相关度，如问答、检索等 。==
- 语言模型，例如 n-gram 和神经网络语言模型（NNLM）。这些模型可以计算一段文本或一个单词出现的概率分布，如预测、生成等 。
- 问答系统模型，例如 BiDAF 和 DrQA。这些模型可以根据给定的问题和文档或知识库返回一个答案或候选答案列表 。
- 自然语言推理（NLI）模型，例如 ESIM 和 InferSent。这些模型可以判断两个句子之间的逻辑关系，如蕴含、矛盾或中立 。
- ==文本分类模型，例如 TextCNN 和 FastText。这些模型可以根据给定的标签或类别对文本进行分类，如新闻分类、主题分类等 。==
- 文本摘要模型，例如 TextRank 和 Pointer-Generator。这些模型可以根据给定的文本生成一个简短的摘要或概要 。
- ==文本匹配模型，例如 MatchPyramid 和 DSSM。这些模型可以计算两个文本之间的匹配程度或相关度，如搜索、排序等 。==
- 文本蕴含模型，例如 Decomposable Attention 和 DIIN。这些模型可以判断一个句子是否能够从另一个句子推理出来，如推理、验证等 。
- 文本纠错模型，例如 Seq2Seq 和 Transformer。这些模型可以检测并纠正文本中的拼写错误、语法错误或语义错误 。
- 文本情感分析（TSA）模型，例如 ATAE-LSTM 和 IAN。这些模型可以检测文本中针对特定目标或方面的情感倾向和极性 。
- 文本复述模型，例如 CopyNet 和 Re3.这些模型可以用不同的方式表达相同的意思，如改写、生成等 。
- 文本风格转换模型，例如 StyleNet 和 UnsupervisedMT。这些模型可以在保持文本内容不变的情况下，改变文本的风格或语气，如正式、幽默等 。
- 文本对齐模型，例如 FastAlign 和 Eflomal。这些模型可以找出两种语言之间的单词或短语的对应关系，如翻译、对照等 。
- 文本生成模型，例如 CTRL 和 T5。这些模型可以根据给定的控制代码或前缀生成特定类型或领域的文本，如新闻、歌词等 。
