# encoding=utf-8

""" print
500387.698121
0.009962413356928893
500387.698121
0.36264831100468403
"""

import numpy as np
import time

np.random.seed(0)

matrix_size = 1000

t1 = time.clock()
matrix = np.random.random((matrix_size, matrix_size))
print(matrix.sum())
print(time.clock() - t1)

t1 = time.clock()
sum = 0
for i in range(matrix_size):
    for j in range(matrix_size):
        sum += matrix[i][j]
print(sum)
print(time.clock() - t1)
