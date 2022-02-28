"""

"""
import numpy as np

# 1. 赋值操作
# 赋值操作是数组引用的一种方法。
# 比如，将 a 数组赋值给变量 b，被赋值后的变量 b 与 a 组具有相同的内存 id。
# 因此，无论操作 a、b 中哪个数组，另一个数组也会受到影响。
a = np.array([[1, 2, 3, 4], [9, 0, 2, 3], [1, 2, 3, 19]])
print("原数组", a)
print("a数组的ID:", id(a))
b = a
print("数组b的id:", id(b))
b.shape = 4, 3
print("b数组形状的更改也会反映到a数组上:")
print(a)

# 2. ndarray.view()
# ndarray.view() 返回一个新生成的数组副本，因此对该数组的操作，不会影响到原数组。
a = np.array([[1, 2, 3, 4], [9, 0, 2, 3], [1, 2, 3, 19]])
print("原数组", a)
print("数组a的ID:", id(a))
b = a.view()
print("数组b的ID:", id(b))
# 打印b数组
print(b)
# 改变b数组形状
b.shape = 4, 3
print("原数组a", a)
print("新数组b", b)

# 3. 切片创建视图
# 使用切片可以创建视图数组，若要修改视图的就会影响到原数组
arr = np.arange(10)
print('数组arr：')
print(arr)
# 创建切片修改原数组arr
a = arr[3:]
b = arr[3:]
a[1] = 123
b[2] = 234
print(arr)

# 4. ndarray.copy()
# 该方法返回原数组的副本，对副本的修改不会影响到原数组。
a = np.array([[1, 2, 3, 4], [9, 0, 2, 3], [1, 2, 3, 19]])
print("原数组", a)
print("a数组ID:", id(a))
b = a.copy()
print("b数组ID:", id(b))
print("打印经过copy方法的b数组：")
print(b)
b.shape = 4, 3
print("原数组", a)
print("经过copy方法的b数组", b)
