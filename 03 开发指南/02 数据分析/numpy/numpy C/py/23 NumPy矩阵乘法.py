"""

"""
import numpy as np

# 1. 逐元素矩阵乘法
# multiple() 函数用于两个矩阵的逐元素乘法
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ndmin=3)
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]], ndmin=3)
result = np.multiply(array1, array2)
print(result)

# 2. 矩阵乘积运算
# matmul() 用于计算两个数组的矩阵乘积
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ndmin=3)
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]], ndmin=3)
result = np.matmul(array1, array2)
print(result)

# 3. 矩阵点积
# dot() 函数用于计算两个矩阵的点积
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ndmin=3)
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]], ndmin=3)
result = np.dot(array1, array2)
print(result)
