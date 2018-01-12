# encoding=utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
# plt.plot(x, y)  # 折线图
plt.plot(x, y, 'o')  # 散点图
plt.savefig('plt.jpg')
plt.show()
