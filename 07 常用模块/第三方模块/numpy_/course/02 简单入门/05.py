import numpy as np

# Basic Operators
a = np.arange(25)
print(a)
a = a.reshape((5, 5))
print(a)
print('------------')
b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
print(b)
b = b.reshape((5, 5))
print(b)
print('------------')

# 逐个位置元素进行计算
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b)
print(a > b)

# 矩阵运算
print(a.dot(b))
