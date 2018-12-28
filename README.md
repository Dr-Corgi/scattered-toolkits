# scattered-toolkits
一些平时写的零零散散的脚本，随用随取。
### Index
#### 1. stc2nlpcc.py
将STC-2的数据转换成NLPCC的数据格式[[post, post_emo], [response, response_emo]]。
#### 2. stc2plain_text.py
将STC-2的数据转换为纯文本格式（使用jieba分词）：

    post_1
    response_1
    post_2
    response_2

#### 3. semeval2bert.py
将SemEval数据转换为可以用BERT进行Fine-tuning的格式。

#### 4. nlpcc2bert.py
将NLPCC数据转换为可以用BERT进行Fine-tuning的格式。

#### 5. bert4nlpcc.py
适用于NLPCC数据的自定义Processor。

#### 6. nlpcc2plain_text.py
将NLPCC数据转换为纯文本格式（按字分词）：

    post_1  post_emo_1
    response_1  res_emo_1
    post_2  post_emo_2
    response_2  res_emo_2

#### 7. ssserver_setup.txt
配置ssserver。

#### 8. tc_bot_autorun.sh
自动运行tc-bot多次并保存运行结果
