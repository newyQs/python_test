import numpy as np

'''
Numpy库的核心是数组对象或ndarray对象（n维数组）。

'''
array = np.arange(20)
print(array)
print(array.shape)

print(array[3])
# print(array[-2])

array[3] = 100
print(array)

# array[3] = 'Numpy'
# print(array)  # ValueError: invalid literal for int() with base 10: 'Numpy'

array[3] = '12'
print(array)

# 使用arange函数，你可以创建一个在定义的起始值和结束值之间具有特定序列的数组
# 类似于python内置的range()函数
print(np.arange(10, 35, 3))
