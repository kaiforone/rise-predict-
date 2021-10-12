## 基于历史数据实现香港新股涨跌预测
近两年，港股打新这个概念在资本市场上骄阳似火。2020年，说是捡钱的一年也毫不过分，不少人在这一年里奋勇出击，摘得硕果累累。多少人又在今年的内卷、破发、汇率重重打击下被割的遍体鳞伤。

港股打新已经存在多年，而这些年也沉淀了不少的数据。本项目旨在通过历史数据，利用机器学习相关算法找出数据之中的规律，实现新股的涨跌预测，从而优化投资策略。

## 项目结构
### 1.spider目录
- 目标：历史新股和其上市表现息息相关的重要数据

- 数据来源：利弗莫尔网 、 阿思达克网

其中有3个文件，lm_spider.py、 astocks.py 分别对应以上两个网站的爬虫。爬取到的数据存放在data目录下； user_agent.py为请求头中User-Agent的列表，方便爬虫文件调用。

### 2.data目录

运行spider目录中的两个文件后，爬取到的数据会存放到该目录，分别为livermore.csv 、 astocks.csv

### 3.predict目录

目录下 rise_predict.ipynb 文件实现新股的涨跌预测
