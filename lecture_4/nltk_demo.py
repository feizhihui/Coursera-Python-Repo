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
print(stopwords.words())  # default fileids='english'
