# encoding=utf-8
from math import sqrt, log2


def isPrime(n):
    assert type(n) == int
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(2, 1000000):
    if not isPrime(i): continue

    p = log2(i + 1)

    if not p == int(p): continue

    if isPrime(int(p)):
        print(i)
