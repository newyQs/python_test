import numpy as np
import sys

# 21. 如何在numpy数组中只打印小数点后三位？
print('21--------')
# Input
rand_arr = np.random.random((5, 3))
# Limit to 3 decimal places
np.set_printoptions(precision=3)
print(rand_arr)

# 22. 如何通过e式科学记数法（如1e10）来打印一个numpy数组？
print('22--------')
# Reset printoptions to default
np.set_printoptions(suppress=False)

# Create the random array
np.random.seed(100)
rand_arr = np.random.random([3, 3]) / 1e3
print(rand_arr)

np.set_printoptions(suppress=True, precision=6)  # precision is optional
print(rand_arr)

# 23. 如何限制numpy数组输出中打印的项目数？
print('23--------')
np.set_printoptions(threshold=6)
a = np.arange(15)
print(a)

# 24. 如何打印完整的numpy数组而不截断
print('24--------')
# Input
np.set_printoptions(threshold=6)
a = np.arange(15)

# Solution
np.set_printoptions(threshold=sys.maxsize)
print(a)

# 25. 如何导入数字和文本的数据集保持文本在numpy数组中完好无损？
print('25--------')
# Solution
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# Print the first 3 rows
print(iris[:3])

# 26. 如何从1维元组数组中提取特定列？
print('26--------')
# # **给定：**
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
# print(iris_1d.shape)
#
# # Solution:
# species = np.array([row[4] for row in iris_1d])
# print(species[:5])

# 27. 如何将1维元组数组转换为2维numpy数组？
print('27--------')
# # **给定：**
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
#
# # Solution:
# # Method 1: Convert each row to a list and get the first 4 items
# iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
# print(iris_2d[:4])
#
# # Alt Method 2: Import only the first 4 columns from source url
# # iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
# # iris_2d[:4]

# 28. 如何计算numpy数组的均值，中位数，标准差
print('28--------')
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

# Solution
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(mu, med, sd)

# 29. 如何规范化数组，使数组的值正好介于0和1之间？
print('29--------')
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

# Solution
Smax, Smin = sepallength.max(), sepallength.min()
# S = (sepallength - Smin) / (Smax - Smin)
# or
S = (sepallength - Smin) / sepallength.ptp()  # Thanks, David Ojeda!
# print(S)

# 30. 如何计算Softmax得分？
print('30--------')
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.array([float(row[0]) for row in iris])


# Solution
def softmax(x):
    """Compute softmax values for each sets of scores in x.
    https://stackoverflow.com/questions/34968722/how-to-implement-the-softmax-function-in-python"""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)


print(softmax(sepallength))
