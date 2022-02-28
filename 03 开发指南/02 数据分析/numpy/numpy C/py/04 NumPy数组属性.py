"""

"""
import numpy as np

# 1. shape 属性的返回值一个由数组维度构成的元组
a = np.array([[2, 4, 6], [3, 5, 7]])
print(a.shape)

# 2. 通过 shape 属性修改数组的形状大小
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)

# 3. 通过reshape()函数调整数组形状
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(a)
print(b)

# 4. 返回数组维度
# 随机生成一个一维数组
c = np.arange(24)
print(c)
print(c.ndim)
# 对数组进行变维操作
e = c.reshape(2, 4, 3)
print(e)
print(e.ndim)

# 5. 返回数组中每个元素的大小（以字节为单位）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)
x = np.array([1, 2, 3, 4, 5], dtype=np.int64)
print(x.itemsize)

# 6. 返回 ndarray 数组的内存信息，比如 ndarray 数组的存储方式，以及是否是其他数组的副本等
x = np.array([1, 2, 3, 4, 5])
print(x.flags)
