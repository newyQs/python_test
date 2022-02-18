"""

"""
import numpy as np

"""
array(
    object: object, 
    dtype: DTypeLike, 
    copy: bool, 
    order: _OrderKACF, 
    subok: bool, 
    ndmin: int, 
    like: ArrayLike
)-> ndarray

numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

参数说明：
    object	数组或嵌套的数列
    dtype	数组元素的数据类型，可选
    copy	对象是否需要复制，可选
    order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
    subok	默认返回一个与基类类型一致的数组
    ndmin	指定生成数组的最小维度
"""
a = np.array([1, 2, 3])
# print(a, type(a))

b = np.array((1, 2, 3))
# print(b, type(b))

c = np.array("dss")
# print(c, type(c))

d = np.array([[1, 2, 3], [4, 5, 6]])
# print(d)

e = np.array([1, 2, 3], ndmin=2)
# print(e)

f = np.array([1, 2, 3], dtype=complex)
print(f)
