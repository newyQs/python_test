"""

"""
import numpy as np

# 1. 进行遍历
a = np.arange(0, 60, 5).reshape(3, 4)
# 使用nditer迭代器,并使用for进行遍历
for x in np.nditer(a):
    print(x)

# 2. 遍历顺序
a = np.arange(0, 60, 5).reshape(3, 4)
# a的转置数组
b = a.T
print(b)
for x in np.nditer(b):
    print(x, end=",")

a = np.arange(0, 60, 5).reshape(3, 4)
# copy方法生成数组副本
for x in np.nditer(a.T.copy(order='C')):
    print(x, end=", ")

# 3. 修改数组元素值
a = np.arange(0, 60, 5).reshape(3, 4)
print("原数组是:", a)
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('修改后的数组是：', a)

# 4. 外部循环使用
a = np.arange(0, 60, 5).reshape(3, 4)
print("原数组", a)
# 修改后数组
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x)

# 5. 迭代多个数组
a = np.arange(0, 60, 5).reshape(3, 4)
print(a)
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
# 广播迭代
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=",")
