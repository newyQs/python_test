"""

"""
import numpy as np

# 1. numpy.arange()
x = np.arange(8)
print(x)
# 设置 start 、stop 值以及步长
x = np.arange(1, 10, 2)
print(x)

# 2. numpy.linspace()
# 表示在指定的数值区间内，返回均匀间隔的一维等差数组，默认均分 50 份
a = np.linspace(1, 10, 10)
print(a)
# endpoint 为 Fasle 时，此时不包含终止值
arr = np.linspace(10, 20, 5, endpoint=False)
print("数组数值范围 ：", arr)
# retstep参数
x = np.linspace(1, 2, 5, retstep=True)
print(x)

# 3. numpy.logspace
# 该函数同样返回一个 ndarray 数组，它用于创建等比数组
a = np.logspace(1.0, 2.0, num=10)
print(a)
# base = 2 的对数函数
a = np.logspace(1, 10, num=10, base=2)
print(a)
