"""

"""
import numpy as np

# 1. 数组变维操作

# 1.1 numpy.ndarray.flat
# numpy.ndarray.flat 返回一个数组迭代器
a = np.arange(9).reshape(3, 3)
for row in a:
    print(row)
# 使用flat属性：
for ele in a.flat:
    print(ele, end="，")

# 1.2 numpy.ndarray.flatten()
# numpy.ndarray.flatten 返回一份数组副本，对副本修改不会影响原始数组
a = np.arange(8).reshape(2, 4)
print(a)
# 默认按行C风格展开的数组
print(a.flatten())
# 以F风格顺序展开的数组
print(a.flatten(order='F'))

# 1.3 numpy.ravel()
# numpy.ravel() 将多维数组中的元素以一维数组的形式展开，该方法返回数组的视图（view），如果修改，则会影响原始数组
a = np.arange(8).reshape(2, 4)
print('原数组：')
print(a)
print('调用 ravel 函数后：')
print(a.ravel())
print('F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))

# 2. 数组转置操作

# 2.1 numpy.transpose()
a = np.arange(12).reshape(3, 4)
print(a)
print(np.transpose(a))

# 2.2 numpy.rollaxis()
# 创建了三维的 ndarray
a = np.arange(27).reshape(3, 3, 3)
print(a)
# 对换0轴与2轴
print(np.swapaxes(a, 2, 0))

# 3. 修改数组维度操作

# 3.1 numpy.broadcast()
a = np.array([[1], [2], [3]])
b = np.array([4, 5, 6])
# 对b广播a
d = np.broadcast(a, b)
# d它拥有 iterator 属性
r, c = d.iters
print(next(r), next(c))
print(next(r), next(c))
# 使用broadcast将a与b相加
e = np.broadcast(a, b)
f = np.empty(e.shape)
f.flat = [x + y for (x, y) in e]
print(f)
print(a + b)

# 3.2 numpy.broadcast_to()
a = np.arange(4).reshape(1, 4)
print("原数组", a)
print('调用 broadcast_to 函数之后：')
print(np.broadcast_to(a, (4, 4)))

# 3.3 numpy.expand_dims()
x = np.array(([1, 2], [3, 4]))
print('数组 x：')
print(x)
# 在 0 轴处插入新的轴
y = np.expand_dims(x, axis=0)
print('数组 y：')
print(y)
print('\n')
print('数组 x 和 y 的形状：')
print(x.shape, y.shape)

#  3.4 numpy.squeeze()
x = np.array([[[0], [1], [2]]])
print(x.shape)
print(np.squeeze(x).shape)
print(np.squeeze(x, axis=(2,)).shape)

a = np.arange(9).reshape(1, 3, 3)
print(a)
b = np.squeeze(a)
print(b)
print('数组 a 和 b 的形状：')
print(x.shape, y.shape)

# 4 连接与分割数组操作

# 4.1 连接数组操作
# 创建数组a
a = np.array([[10, 20], [30, 40]])
print(a)
# 创建数组b
b = np.array([[50, 60], [70, 80]])
print(b)
# 沿轴 0 连接两个数组
print(np.concatenate((a, b)))
# 沿轴 1 连接两个数组
print(np.concatenate((a, b), axis=1))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# 垂直堆叠
c = np.vstack((a, b))
print(c)

# 4.2 分割数组操作
a = np.arange(6)
# 原数组
print(a)
# 将数组分为二个形状大小相等的子数组
b = np.split(a, 2)
print(b)
# 将数组在一维数组中标明要位置分割
b = np.split(a, [3, 4])
print(b)

# arr1数组
arr1 = np.floor(10 * np.random.random((2, 6)))
print(arr1)
# 拆分后数组
print(np.hsplit(arr1, 3))
