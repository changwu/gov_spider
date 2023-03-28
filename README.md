# gov_spider

### 帮助

1. 安装python
2. git clone https://github.com/changwu/gov_spider.git
3. cd gov_spider
4. pip install -r requirements.txt
5. python start.py


### 说明

wjbfb.txt 文件按行存储文章解析结果，每行对应一个文章页。

### 其它
1. 将wjbfb.txt文件的数据导成单个文件
```
python export.py
```

2. 制作语料库
```
python make_corpus.py
```

3. glove向量计算
```
# cal.py中列出了计算相似度和距离的例子，可以修改源文件。
python cal.py
```
