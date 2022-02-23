"""

"""
import numpy as np

# 1. bitwise_and()
a = 10
b = 12
print("a的二进制数:", bin(a))
print("b的二进制数:", bin(b))
print("将a与b执行按位与操作:", np.bitwise_and(a, b))

# 2. bitwise_or()
a, b = 13, 17
print('13 和 17 的二进制数：')
print(bin(a), bin(b))
print('13 和 17 的位或：')
print(np.bitwise_or(13, 17))

# 3. Invert()
# 数据类型为无符号整型uint8
arr = np.array([20], dtype=np.uint8)
print("二进制表示:", np.binary_repr(20, 8))
print(np.invert(arr))
# 进行取反操作
print("二进制表示: ", np.binary_repr(235, 8))

# 4. left_shift()
# 移动三位后的输出值
print(np.left_shift(20, 3))
# 打印移动后20的二进制数
print(np.binary_repr(20, width=8))
# 函数返回值的二进制数
print(np.binary_repr(160, width=8))

# 5. right_shift()
# 将40右移两位后返回值：
print(np.right_shift(40, 2))
# 移动后40的二进制数：
print(np.binary_repr(40, width=8))
# 移动后返回值的二进制数：
print(np.binary_repr(10, width=8))
