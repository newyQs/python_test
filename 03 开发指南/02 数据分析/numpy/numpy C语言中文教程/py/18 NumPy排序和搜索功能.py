"""

"""
import numpy as np

# 1. numpy.sort()
# numpy.sort() 对输入数组执行排序，并返回一个数组副本
a = np.array([[3, 7], [9, 1]])
print('a数组是：')
print(a)
# 调用sort()函数
print(np.sort(a))
# 按列排序：
print(np.sort(a, axis=0))
# 设置在sort函数中排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
# 再次打印a数组
print(a)
# 按name字段排序
print(np.sort(a, order='name'))

# 2. numpy.argsort()
# argsort() 沿着指定的轴，对输入数组的元素值进行排序，并返回排序后的元素索引数组
a = np.array([90, 29, 89, 12])
print("原数组", a)
sort_ind = np.argsort(a)
print("打印排序元素索引值", sort_ind)
# 使用索引数组对原数组排序
sort_a = a[sort_ind]
print("打印排序数组")
for i in sort_ind:
    print(a[i], end=" ")

# 3. numpy.lexsort()
# numpy.lexsort() 按键序列对数组进行排序，它返回一个已排序的索引数组，类似于 numpy.argsort()
a = np.array(['a', 'b', 'c', 'd', 'e'])
b = np.array([12, 90, 380, 12, 211])
ind = np.lexsort((a, b))
# 打印排序元素的索引数组
print(ind)
# 使用索引数组对数组进行排序
for i in ind:
    print(a[i], b[i])

# 4. numpy.nonzero()
# 该函数从数组中查找非零元素的索引位置
b = np.array([12, 90, 380, 12, 211])
print("原数组b", b)
print("打印非0元素的索引位置")
print(b.nonzero())

# 5. numpy.where()
# numpy.where() 的返回值是满足了给定条件的元素索引值
b = np.array([12, 90, 380, 12, 211])
print(np.where(b > 12))
c = np.array([[20, 24], [21, 23]])
print(np.where(c > 20))

# 6. numpy.extract()
# 该函数的返回值是满足了给定条件的元素值
x = np.arange(9.).reshape(3, 3)
# 打印数组x:
print(x)
# 设置条件选择偶数元素
condition = np.mod(x, 2) == 0
# 输出布尔值数组
print(condition)
# 按condition提取满足条件的元素值
print(np.extract(condition, x))

# 7. numpy.argmax()
# 该函数返回最大值的的索引，与其相反的函数是 argmin() 求最小值索引
a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
# a数组
print(a)
# argmax() 函数
print(np.argmax(a))
# 将数组以一维展开
print(a.flatten())
# 沿轴 0 的最大值索引：
maxindex = np.argmax(a, axis=0)
print(maxindex)
# 沿轴 1 的最大值索引
maxindex = np.argmax(a, axis=1)
print(maxindex)

# 8. numpy.argmin()
# argmin() 求最小值索引
b = np.array([[3, 4, 7], [8, 2, 1], [5, 9, 6]])
print('数组b：')
print(b)
# 调用 argmin()函数
minindex = np.argmin(b)
print(minindex)
# 展开数组中的最小值：
print(b.flatten()[minindex])
# 沿轴 0 的最小值索引：
minindex = np.argmin(b, axis=0)
print(minindex)
# 沿轴 1 的最小值索引：
minindex = np.argmin(b, axis=1)
print(minindex)
