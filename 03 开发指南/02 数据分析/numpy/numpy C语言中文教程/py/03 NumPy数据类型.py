"""

"""
import numpy as np

# 1. 创建一个dtype对象
a = np.dtype(np.int64)
print(a)

# 2. 使用数据类型标识码
dt = np.dtype([('score', 'i1')])
print(dt)

# 3. 将上述标识码应用到ndarray中
dt = np.dtype([('score', 'i1')])
a = np.array([(55,), (75,), (85,)], dtype=dt)
print(a)
print(a.dtype)
print(a['score'])

# 4. 定义结构化数据
teacher = np.dtype([('name', 'S20'), ('age', 'i1'), ('salary', 'f4')])
print(teacher)
# 将其应用于ndarray对象
b = np.array([('ycs', 32, 6357.50), ('jxe', 28, 6856.80)], dtype=teacher)
print(b)
