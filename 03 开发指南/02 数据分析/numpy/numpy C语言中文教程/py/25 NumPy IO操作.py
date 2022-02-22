"""

"""
import numpy as np

# 1. numpy.save()
# numpy.save() 方法将输入数组存储在.npy文件中
a = np.array([1, 2, 3, 4, 5])
np.save('first', a)

# 使用 load() 从 first.npy 文件中加载数据
b = np.load('first.npy')
print(b)

# 2. savetxt()
# savetxt() 和 loadtxt() 分别表示以文本格式存储数据或加载数据
a = np.array([1, 2, 3, 4, 5])
np.savetxt('second.txt', a)
# 使用loadtxt重载数据
b = np.loadtxt('second.txt')
print(b)
