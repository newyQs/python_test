"""

"""
import numpy as np

# 1. numpy.empty()
arr = np.empty((3, 2), dtype=int)
print(arr)

# 2. numpy.zeros()
# 默认数据类型为浮点数
a = np.zeros(6)
print(a)
b = np.zeros(6, dtype="complex64")
print(b)
# 使用自定义的数据类型
c = np.zeros((3, 3), dtype=[('x', 'i4'), ('y', 'i4')])
print(c)

# 3. numpy.ones()
arr1 = np.ones((3, 2), dtype=int)
print(arr1)

# 4. numpy.asarray()
# 将列表转化为 numpy 数组：
l = [1, 2, 3, 4, 5, 6, 7]
a = np.asarray(l)
print(type(a))
print(a)
# 使用元组创建 numpy 数组：
l = (1, 2, 3, 4, 5, 6, 7)
a = np.asarray(l)
print(type(a))
print(a)
# 使用嵌套列表创建多维数组：
l = [[1, 2, 3, 4, 5, 6, 7], [8, 9]]
a = np.asarray(l)
print(type(a))
print(a)

# 5. numpy.frombuffer()
# 字节串类型
st = b'hello world'
print(type(l))
a = np.frombuffer(st, dtype="S1")
print(a)
print(type(a))

# 6. numpy.fromiter()
# 使用 range 函数创建列表对象
lis = range(6)
# 生成可迭代对象i
i = iter(lis)
# 使用i迭代器，通过fromiter方法创建ndarray
array = np.fromiter(i, dtype=float)
print(array)
