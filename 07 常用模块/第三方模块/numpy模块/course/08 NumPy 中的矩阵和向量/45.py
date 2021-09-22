import numpy as np

A = np.array([[1, -1, 2], [3, 2, 0]])
print(A)

v = np.array([[2], [1], [3]])
print(v)

print(np.transpose(np.array([1, 2, 3])))
print(np.transpose(np.array([[1, 2, 3]])))

# 打印矩阵A中的右下方条目
print(A[1, 2])

# 切出A矩阵中的第二列
print(A[:, 1:2])

# 矩阵乘法或矩阵向量乘法
print(np.dot(A, v))
