"""

"""
import numpy as np

# 1. numpy.resize()
# numpy.resize() 返回指定形状的新数组。
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
# a数组的形状
print(a.shape)
b = np.resize(a, (3, 2))
# b数组
print(b)
# b数组的形状
print(b.shape)
# 修改c数组使其形状大于原始数组
c = np.resize(a, (3, 3))
print(c)

# 这里需要区别 resize() 和 reshape() 的使用方法，它们看起来相似，实则不同。
# resize 仅对原数组进行修改，没有返回值，而 reshape 不仅对原数组进行修改，同时返回修改后的结果。

# 2. numpy.append()
a = np.array([[1, 2, 3], [4, 5, 6]])
# 向数组a添加元素
print(np.append(a, [7, 8, 9]))
# 沿轴 0 添加元素
print(np.append(a, [[7, 8, 9]], axis=0))
# 沿轴 1 添加元素
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))

# 3. numpy.insert()
# 表示沿指定的轴，在给定索引值的前一个位置插入相应的值，如果没有提供轴，则输入数组被展开为一维数组
a = np.array([[1, 2], [3, 4], [5, 6]])
# 不提供axis的情况，会将数组展开
print(np.insert(a, 3, [11, 12]))
# 沿轴 0 垂直方向
print(np.insert(a, 1, [11], axis=0))
# 沿轴 1 水平方向
print(np.insert(a, 1, 11, axis=1))

# 4. numpy.delete()
a = np.arange(12).reshape(3, 4)
# a数组
print(a)
# 不提供axis参数情况
print(np.delete(a, 5))
# 删除第二列
print(np.delete(a, 1, axis=1))
# 删除经切片后的数组
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a, np.s_[::2]))

# 5. numpy.argwhere()
x = np.arange(6).reshape(2, 3)
print(x)
# 返回所有大于1的元素索引
y = np.argwhere(x > 1)
print(y)

# 6. numpy.unique()
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print(a)
# 对a数组的去重
uq = np.unique(a)
print(uq)
# 数组去重后的索引数组
u, indices = np.unique(a, return_index=True)
# 打印去重后数组的索引
print(indices)
# 去重数组的下标：
ui, indices = np.unique(a, return_inverse=True)
print(ui)
# 打印下标
print(indices)
# 返回去重元素的重复数量
uc, indices = np.unique(a, return_counts=True)
print(uc)
# 元素出现次数：
print(indices)
