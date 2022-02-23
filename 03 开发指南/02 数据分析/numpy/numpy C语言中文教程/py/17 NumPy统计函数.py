"""

"""
import numpy as np

# numpy.amin() 和 numpy.amax()
# 这两个函数用于计算数组沿指定轴的最小值与最大值，并以数组形式返回
# 对于二维数组来说，axis=1 表示沿着水平方向，axis=0 表示沿着垂直方向。
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('数组a是：')
print(a)
# amin()函数
print(np.amin(a))
# 调用 amin() 函数，axis=1
print(np.amin(a, 1))
# 调用amax()函数
print(np.amax(a))
# 再次调用amax()函数
print(np.amax(a, axis=0))

# numpy.ptp()
# numpy.ptp() 用于计算数组元素中最值之差值，也就是（最大值 - 最小值）。
a = np.array([[2, 10, 20], [80, 43, 31], [22, 43, 10]])
print("原数组", a)
print("沿着axis 1:", np.ptp(a, 1))
print("沿着axis 0:", np.ptp(a, 0))

# numpy.percentile()
# 百分位数，是统计学中使用的一种度量单位。该函数表示沿指定轴，计算数组中任意百分比分位数
a = np.array([[2, 10, 20], [80, 43, 31], [22, 43, 10]])
print("数组a:", a)
print("沿着axis=0计算百分位数", np.percentile(a, 10, 0))
print("沿着axis=1计算百分位数", np.percentile(a, 10, 1))

# numpy.median()
# numpy.median() 用于计算 a 数组元素的中位数（中值）
a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
# 数组a:
print(a)
# median()
print(np.median(a))
# axis 0
print(np.median(a, axis=0))
# axis 1:
print(np.median(a, axis=1))

# numpy.mean()
# 该函数表示沿指定的轴，计算数组中元素的算术平均值（即元素之总和除以元素数量）
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('我们的数组是：')
print(a)
print('调用 mean() 函数：')
print(np.mean(a))
print('沿轴 0 调用 mean() 函数：')
print(np.mean(a, axis=0))
print('沿轴 1 调用 mean() 函数：')
print(np.mean(a, axis=1))

# numpy.average()
# 加权平均值是将数组中各数值乘以相应的权数，然后再对权重值求总和，最后以权重的总和除以总的单位数（即因子个数）。
# numpy.average() 根据在数组中给出的权重，计算数组元素的加权平均值。该函数可以接受一个轴参数 axis，如果未指定，则数组被展开为一维数组。
a = np.array([1, 2, 3, 4])
print('a数组是：')
print(a)
# average()函数：
print(np.average(a))
# 若不指定权重相当于对数组求均值
we = np.array([4, 3, 2, 1])
# 调用 average() 函数：')
print(np.average(a, weights=we))
# returned 为Ture，则返回权重的和
print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True))

# 在多维数组中，您也可以指定 axis 轴参数
a = np.arange(6).reshape(3, 2)
# 多维数组a
print(a)
# 修改后数组
wt = np.array([3, 5])
print(np.average(a, axis=1, weights=wt))
# 修改后数组
print(np.average(a, axis=1, weights=wt, returned=True))

# 方差np.var()
print(np.var([1, 2, 3, 4]))

# 标准差np.std()
print(np.std([1, 2, 3, 4]))
