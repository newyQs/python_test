import numpy as np

#  如果只使用arange函数，它将输出一维数组。
#  要使其成为二维数组，请使用reshape函数链接其输出。
array = np.arange(20).reshape(4, 5)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]

print(array)
print(array.shape)

print(array[3][4])
print(array[3, 4])
