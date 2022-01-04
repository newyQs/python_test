import numpy as np

# 11. 如何获取两个numpy数组之间的公共项？
print('11--------')
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(np.intersect1d(a, b))

# 12. 如何从一个数组中删除存在于另一个数组中的项？
print('12--------')
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

# From 'a' remove all of 'b'
print(np.setdiff1d(a, b))

# 13. 如何得到两个数组元素匹配的位置？
print('13--------')
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print(np.where(a == b))

# 14. 如何从numpy数组中提取给定范围内的所有数字？
print('14--------')
# 获取5到10之间的所有项目
a = np.array([2, 6, 1, 9, 10, 3, 27])

# Method 1
index = np.where((a >= 5) & (a <= 10))
print(a[index])

# Method 2:
index = np.where(np.logical_and(a >= 5, a <= 10))
a[index]

# Method 3: (thanks loganzk!)
a[(a >= 5) & (a <= 10)]  # > (array([6, 9, 10]),)


# 15. 如何创建一个python函数来处理scalars并在numpy数组上工作？
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


print('15--------')
pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

print(pair_max(a, b))
# > array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])

# 16. 如何交换二维numpy数组中的两列？
print('16--------')
# Input
arr = np.arange(9).reshape(3, 3)
arr

# Solution
print(arr[:, [1, 0, 2]])
# > array([[1, 0, 2],
# >        [4, 3, 5],
# >        [7, 6, 8]])

# 17. 如何交换二维numpy数组中的两行？
print('17--------')
# Input
arr = np.arange(9).reshape(3, 3)

# Solution
print(arr[[1, 0, 2], :])
# > array([[3, 4, 5],
# >        [0, 1, 2],
# >        [6, 7, 8]])

# 18. 如何反转二维数组的行？
print('18--------')
# Input
arr = np.arange(9).reshape(3, 3)
# Solution
print(arr[::-1])
# array([[6, 7, 8],
#       [3, 4, 5],
#       [0, 1, 2]])

# 19. 如何反转二维数组的列？
print('19--------')
# Input
arr = np.arange(9).reshape(3, 3)

# Solution
arr[:, ::-1]
# > array([[2, 1, 0],
# >        [5, 4, 3],
# >        [8, 7, 6]])

# 20. 如何创建包含5到10之间随机浮动的二维数组？
# Input
arr = np.arange(9).reshape(3, 3)

# Solution Method 1:
rand_arr = np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
# print(rand_arr)

# Solution Method 2:
rand_arr = np.random.uniform(5, 10, size=(5, 3))
print(rand_arr)

