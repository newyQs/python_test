"""

"""
import numpy.matlib
import numpy as np

# 1. matlib.empty()
# matlib.empty() 返回一个空矩阵，所以它的创建速度非常快
# 矩阵中会填充无意义的随机值
print(np.matlib.empty((2, 2)))

# 2. numpy.matlib.zeros()
# numpy.matlib.zeros() 创建一个以 0 填充的矩阵
print(np.matlib.zeros((2, 2)))

# 3. numpy.matlib.ones()
# numpy.matlib.ones() 创建一个以 1 填充的矩阵
print(np.matlib.ones((2, 2)))

# 4. numpy.matlib.eye()
# numpy.matlib.eye() 返回一个对角线元素为 1，而其他元素为 0 的矩阵
print(np.matlib.eye(n=3, M=4, k=0, dtype=float))

# 5. numpy.matlib.identity()
# 该函数返回一个给定大小的单位矩阵，矩阵的对角线元素为 1，而其他元素均为 0
print(np.matlib.identity(5, dtype=float))

# 6. numpy.matlib.rand()
# numpy.matlib.rand() 创建一个以随机数填充，并给定维度的矩阵
print(np.matlib.rand(3, 3))

# 这里需要注意，因为 matrix 只能表示二维数据，而 ndarray 也可以是二维数组，所以两者可以互相转换
i = np.matrix('1,2;3,4')
print(i)

# 实现 matrix 与 ndarray 之间的转换
j = np.asarray(i)
print(j)
k = np.asmatrix(j)
print(k)
