import numpy as np

# 使用zeros函数创建一个填充零的数组
print(np.zeros((2, 4)))

# 使用ones函数创建一个填充了1的数组
print(np.ones((3, 4)))

# 创建随机数组，初始内容取决于内存的状态
print(np.empty((2, 3)))

# full函数创建一个填充给定值的n * n数组
print(np.full((2, 4), 0))
print(np.full((2, 4), 1))
print(np.full((2, 4), 7))

# eye函数可以创建一个n * n矩阵，对角线为1，其他为0
print(np.eye(5, 5))

# 函数linspace在指定的时间间隔内返回均匀间隔的数字
# 例如，下面的函数返回0到10之间的四个等间距数字
print(np.linspace(0, 10, num=4))