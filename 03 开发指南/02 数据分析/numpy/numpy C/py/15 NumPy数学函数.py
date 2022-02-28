"""

"""
import numpy as np

# 1. 三角函数

arr = np.array([0, 30, 60, 90, 120, 150, 180])
# 计算arr数组中给定角度的三角函数值
# 通过乘以np.pi/180将其转换为弧度
print(np.sin(arr * np.pi / 180))
print(np.cos(arr * np.pi / 180))
print(np.tan(arr * np.pi / 180))

arr = np.array([0, 30, 60, 90])
# 正弦值数组
sinval = np.sin(arr * np.pi / 180)
print(sinval)
# 计算角度反正弦，返回值以弧度为单位
cosec = np.arcsin(sinval)
print(cosec)
# 通过degrees函数转化为角度进行验证
print(np.degrees(cosec))
# 余弦值数组
cosval = np.cos(arr * np.pi / 180)
print(cosval)
# 计算反余弦值，以弧度为单位
sec = np.arccos(cosval)
print(sec)
# 通过degrees函数转化为角度进行验证
print(np.degrees(sec))
# 下面是tan()正切函数
tanval = np.tan(arr * np.pi / 180)
print(tanval)
cot = np.arctan(tanval)
print(cot)
print(np.degrees(cot))

# 2. 舍入函数

# 2.1 numpy.around()
# 该函数返回一个十进制值数，并将数值四舍五入到指定的小数位上
arr = np.array([12.202, 90.23120, 123.020, 23.202])
print(arr)
print("数组值四舍五入到小数点后两位", np.around(arr, 2))
print("数组值四舍五入到小数点后-1位", np.around(arr, -1))

# 2.2 numpy.floor()
a = np.array([-1.8, 1.1, -0.4, 0.9, 18])
# 对数组a向下取整
print(np.floor(a))

# 2.3 numpy.ceil()
a = np.array([-1.8, 1.1, -0.4, 0.9, 18])
# 对数组a向上取整
print(np.ceil(a))
