# encoding=utf-8

"""
f=sqrt(x)
"""


def sqrt(a, lr):
    """"""
    x = 0
    y, y_new = 1, 0
    while abs(y - y_new) > 1e-12:
        y = y_new
        dx = x ** 2 - a
        x = x - lr * dx
        y_new = 1 / 3 * x ** 3 - a * x
    return x


for x in [10, 100, 1000, 10000, 100000]:
    print(sqrt(x, 0.001))
