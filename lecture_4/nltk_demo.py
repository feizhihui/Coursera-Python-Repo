# encoding: utf-8

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
