"""

"""
import numpy as np

# 1. numpy.dot()
# 按照矩阵的乘法规则，计算两个矩阵的点积运算结果。
# 当输入一维数组时返回一个结果值，若输入的多维数组则同样返回一个多维数组结果。

# 输入一维数组
A = [1, 2, 3]
B = [4, 5, 6]
print(np.dot(A, B))

# 输入二维数组
a = np.array(
    [[100, 200],
     [23, 12]]
)
b = np.array(
    [[10, 20],
     [12, 21]]
)
dot = np.dot(a, b)
print(dot)

# 2. numpy.vdot()
# 该函数用于计算两个向量的点积结果，与 dot() 函数不同
a = np.array([[100, 200], [23, 12]])
b = np.array([[10, 20], [12, 21]])
vdot = np.vdot(a, b)
print(vdot)

# 3. numpy.inner()
# inner() 方法用于计算数组之间的内积。当计算的数组是一维数组时，它与 dot() 函数相同，若输入的是多维数组则两者存在不同
A = [[1, 10],
     [100, 1000]]
B = [[1, 2],
     [3, 4]]
# inner函数
print(np.inner(A, B))
# dot函数
print(np.dot(A, B))

# 4. numpy.matmul()
# 该函数返回两个矩阵的乘积，假如两个矩阵的维度不一致，就会产生错误。
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[23, 23, 12], [2, 1, 2], [7, 8, 9]])
mul = np.matmul(a, b)
print(mul)

# 5. numpy.linalg.det()
# 该函数使用对角线元素来计算矩阵的行列式
a = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a))

# 6. numpy.linalg.solve()
# 该函数用于求解线性矩阵方程组，并以矩阵的形式表示线性方程的解
m = np.array([[3, 2, 1], [1, 1, 1], [1, 2, -1]])
print('数组 m：')
print(m)
print('矩阵 n：')
n = np.array([[10], [6], [2]])
print(n)
print('计算：m^(-1)n：')
x = np.linalg.solve(m, n)
print(x)

# 7. numpy.linalg.inv()
# 该函数用于计算矩阵的逆矩阵，逆矩阵与原矩阵相乘得到单位矩阵
a = np.array([[1, 2], [3, 4]])
print("原数组:", a)
b = np.linalg.inv(a)
print("求逆:", b)
