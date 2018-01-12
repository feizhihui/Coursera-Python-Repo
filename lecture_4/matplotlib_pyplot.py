# encoding=utf-8

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6), dpi=100)

x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.plot(x, y, 'r--')  # 折线图  红色虚线
# plt.plot(x, y, 'o')  # 散点图

# plt.bar(x, y)  # 柱状图
plt.title('Stock Statistics of Coca-Cola')
plt.xlabel('Month')
plt.ylabel('Average Close Price')
# plt.legend(loc='upper_left')  # 图例位置
# plt.subplot(212)  # 定义子图
# plt.subplots_adjust()  # 定义子图距离


plt.savefig('plt.jpg')
plt.show()
