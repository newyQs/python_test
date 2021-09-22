import numpy as np

# 创建数组的4种不同方法
# 最基本的方法是将序列传递给NumPy的array()函数; 你可以传递任何序列（类数组），而不仅仅是常见的列表（list）数据类型
a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2 * np.pi, 5)

print(a)  # >>>[0 1 2 3 4]
print(b)  # >>>[0 1 2 3 4]
print(c)  # >>>[0 1 2 3 4]
print(d)  # >>>[ 0.          1.57079633  3.14159265  4.71238898  6.28318531]
print(a[3])  # >>>3
