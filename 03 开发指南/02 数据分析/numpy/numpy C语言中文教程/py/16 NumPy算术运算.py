"""

"""
import numpy as np

# NumPy 数组的“加减乘除”算术运算，分别对应 add()、subtract()、multiple() 以及 divide() 函数。
# 注意：做算术运算时，输入数组必须具有相同的形状，或者符合数组的广播规则，才可以执行运算。

# 数组a
a = np.arange(9, dtype=np.float_).reshape(3, 3)
print(a)
# 数组b
b = np.array([10, 10, 10])
print(b)
# 数组加法运算
print(np.add(a, b))
# 数组减法运算
print(np.subtract(a, b))
# 数组乘法运算
print(np.multiply(a, b))
# 数组除法运算
print(np.divide(a, b))

# numpy.reciprocal()
# 该函数对数组中的每个元素取倒数，并以数组的形式将它们返回。
# 当数组元素的数据类型为整型（int）时，对于绝对值小于 1 的元素，返回值为 0，而当数组中包含 0 元素时，返回值将出现 overflow（inf） 溢出提示

# 注意此处有0
a = np.array([0.25, 1.33, 1, 0, 100])
# 数组a默认为浮点类型数据
print(a)
# 对数组a使用求倒数操作
print(np.reciprocal(a))
# b数组的数据类型为整形int
b = np.array([100], dtype=int)
print(b)
# 对数组b使用求倒数操作
print(np.reciprocal(b))

# numpy.power()
a = np.array([10, 100, 1000])
# a数组
print('我们的数组是；')
# 调用 power 函数
print(np.power(a, 2))
# b数组
b = np.array([1, 2, 3])
print(b)
# 调用 power 函数
print(np.power(a, b))

# numpy.mod()
# 返回两个数组相对应位置上元素相除后的余数，它与 numpy.remainder() 的作用相同
a = np.array([11, 22, 33])
b = np.array([3, 5, 7])
# a与b相应位置的元素做除法
print(np.mod(a, b))
# remainder方法一样
print(np.remainder(a, b))

# 复数数组处理函数
a = np.array([-5.6j, 0.2j, 11., 1 + 1j])
print(a)
# real()
print(np.real(a))
# imag()
print(np.imag(a))
# conj()
print(np.conj(a))
# angle()
print(np.angle(a))
# angle() 带参数deg
print(np.angle(a, deg=True))
