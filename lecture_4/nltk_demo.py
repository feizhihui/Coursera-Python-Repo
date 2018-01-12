# encoding: utf-8
"""
NLTK包括获取语料库、字符串处理、搭配发现、词性标注、机器学习、分块解析、语义解释、指标评测、概率与估计等多项语言任务，
在处理时非常方便，例如要载入并去掉停用词可用类似如下几行简单代码就可以完成
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
… if words not in stopwords…
"""
from nltk.corpus import gutenberg, stopwords
from nltk.probability import *

allwords = gutenberg.words('shakespeare-hamlet.txt')
print(len(allwords), type(allwords))
print(allwords.count('Hamlet'))
print(allwords[:20])
A = set(allwords)
longwords = [w for w in A if len(w) > 12]
print(sorted(longwords))

fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()])  # 计算频次
print(fd2.B())  # bins
print(fd2.N())  # total word number
fd2.tabulate(20)
fd2.plot(20)
fd2.plot(20, cumulative=True)

print(len(stopwords.words()), type(stopwords.words()))
print(stopwords.words(fileids='english'))  # default fileids='english'

# 载入本地语料库

from nltk.corpus import PlaintextCorpusReader

corpus_root = r'd:\data'
books = PlaintextCorpusReader(corpus_root, '.*')  # 文件名可用正则表达式
print(books.fileids())
print(books.words())
print(books.raw('2.txt'))

import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist((genre, word)
                               for genre in brown.categories()
                               for word in brown.words(categories=genre))
genres = ['news', 'romance']
modals = ['can', 'could', 'may', 'might', 'must', 'will', 'would']
cfd.tabulate(conditions=genres, samples=modals)
cfd.plot(conditions=genres, samples=modals)
