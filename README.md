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

