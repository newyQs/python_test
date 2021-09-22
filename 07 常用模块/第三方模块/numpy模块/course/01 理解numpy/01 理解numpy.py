import numpy as np

# 定义一维NumPy数组
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)  # [1 2 3 4 5]
print([1, 2, 3, 4, 5])  # [1, 2, 3, 4, 5]

# 打印创建的数组的形状：（m,n） m行n列
print(my_array.shape)  # (5,)

# 通过索引打印指定元素
print(my_array[0])
print(my_array[1])

# 通过for循环来遍历数组
for i in my_array:
    print(i)

# 修改数组中的元素
my_array[1] = -2
print(my_array)

# 创建一个长度为5的NumPy数组，但所有元素都为0
my_new_array = np.zeros((5))
print(my_new_array)

# 创建一个长度为5的NumPy数组，但所有元素都为1
my_new_array1 = np.ones((5))
print(my_new_array1)

# 创建一个长度为5的随机NumPy数组
my_random_array = np.random.random((5))
print(my_random_array)

# 创建二维数组0
my_2d_array = np.zeros((2, 3))
print(my_2d_array)

# 创建二维数组1
my_2d_array_new = np.ones((2, 4))
print(my_2d_array_new)

# 二维数组获取元素中的值
my_array = np.array([[4, 5], [6, 1]])
print(my_array[0][1])
print(my_array[0, 1])
print(my_array.shape)  # (2, 2)

# 提取第2列（索引1）的所有元素
print(my_array[:, 1])

# 提取第1行（索引0）的所有元素
print(my_array[0, :])
