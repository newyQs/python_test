"""

"""
import numpy as np

# 1. numpy.ndarray.byteswap()
# 该函数将数组中每个元素的字节顺序进行大小端调换。
a = np.array([1, 256, 8755], dtype=np.int16)
# 数组a
print(a)
# 以16进制形式表示内存中的数据
print(map(hex, a))
# byteswap()函数通过传递True参数在适当的位置进行转换
# 调用byteswap()函数
print(a.byteswap(True))
# 十六进制形式
print(map(hex, a))
