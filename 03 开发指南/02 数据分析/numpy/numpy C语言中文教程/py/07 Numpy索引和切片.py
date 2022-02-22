"""

"""
import numpy as np

# 1. 基本切片
a = np.arange(10)
# 生成切片对象
s = slice(2, 9, 3)  # 从索引2开始到索引9停止，间隔时间为2
print(a[s])
# 通过冒号来分割切片参数
a = np.arange(10)
b = a[2:9:2]
print(b)
# 关于冒号的用法
a = np.arange(10)
print(a[3])
print(a[2:])
print(a[2:5])

# 2. 多维数组切片
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
# 从[1:]索引处开始切割
print(a[1:])

# 省略号的使用
# 创建a数组
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
# 返回数组的第二列
print(a[..., 1])
# 返回数组的第二行
print(a[1, ...])
# 返回第二列后的所有项
print(a[..., 1:])
