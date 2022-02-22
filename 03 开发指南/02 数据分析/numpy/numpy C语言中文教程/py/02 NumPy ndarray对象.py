"""
array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,like=None)
"""
import numpy as np

# 1.创建一维数组
a = np.array([1, 2, 3])
print(a)
print(type(a))

# 2. 创建多维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# 3. 通过设置dtype参数改变数组的数据类型
c = np.array([2, 4, 6, 8], dtype="complex")
print(c)

# 4.通过 ndim 可以查看数组的维度：
arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])
print(arr.ndim)

# 5. 使用 ndmin 参数创建不同维度的数组
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)

# 6. reshape函数接受一个元组作为参数，用于指定了新数组的行数和列数：
e = np.array([[1, 2], [3, 4], [5, 6]])
print("原数组", e)
print(e.ndim)
e = e.reshape(2, 3)
print("新数组", e)
print(e.ndim)
