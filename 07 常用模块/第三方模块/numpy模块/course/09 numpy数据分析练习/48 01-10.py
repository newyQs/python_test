import numpy as np

# 1 查看numpy版本号
print('1--------')
print(np.__version__)

# 2.创建一维数组
print('2--------')
print(np.array([1, 2, 3]))
print(np.arange(10))
print(np.full((8,), 3))

# 3.创建一个布尔数组
print('3--------')
bo = np.full((3, 4), True)
print(bo)
print(bo.dtype)

print(np.ones((3, 3), dtype=bool))
print(np.zeros((3, 3), dtype=bool))

# 4.如何从一维数组中提取满足指定条件的元素？
print('4--------')
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 取奇数
print(arr[1::2])
print(arr[arr % 2 == 1])

# 5.如何用numpy数组中的另一个值替换满足条件的元素项？
print('5--------')
# 将arr中的所有奇数替换为-1
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# arr[1::2] = -1
arr[arr % 2 == 1] = -1
print(arr)

# 6. 如何在不影响原始数组的情况下替换满足条件的元素项？
print('6--------')
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 == 1, -1, arr)
print(out)
print(arr)

# 7. 如何改变数组的形状？
print('7--------')
arr = np.arange(10)
# 设置为-1自动决定列数，这里相当于5
array = arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols
print(array)

# 8. 如何垂直叠加两个数组？
print('8--------')
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# Method 1:
np.concatenate([a, b], axis=0)

# Method 2:
np.vstack([a, b])

# Method 3:
print(np.r_[a, b])

# 9. 如何水平叠加两个数组？
print('9--------')
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# Method 1:
np.concatenate([a, b], axis=1)

# Method 2:
np.hstack([a, b])

# Method 3:
print(np.c_[a, b])

# 10. 如何在无硬编码的情况下生成numpy中的自定义序列？
print('10--------')
a = np.array([1, 2, 3])
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])


