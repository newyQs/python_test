"""

"""
import numpy as np
from matplotlib import pyplot as plt

# 1. 绘制线性函数图像
x = np.arange(1, 11)
y = 2 * x + 5
# 绘制坐标标题
plt.title("Matplotlib demo")
# 绘制x、y轴备注
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
plt.show()

# 如果想要以圆点的样式，来代替图 1 中的线条样式，那么可以使用“ ob”作为 plot() 的格式化字符
x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo1")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y, "ob")
plt.show()

# 2. 绘制正弦波图
# 计算正弦曲线上的x和y坐标
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave image")
# 使用matplotlib制图
plt.plot(x, y)
plt.show()

# 3. subplot()
# subplot() 允许您在同一画布中的不同位置绘制多个图像，可以理解为对画布按行、列分割
# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 绘制subplot 网格为2行1列
# 激活第一个 subplot
plt.subplot(2, 1, 1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
# 展示图像
plt.show()

# 4. bar()柱状图
# 第一组数据
x1 = [5, 8, 10]
y1 = [12, 16, 6]
# 第二组数据
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.bar(x1, y1, align='center')
plt.bar(x2, y2, color='g', align='center')
plt.title('Bar graph')
# 设置x轴与y轴刻度
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

# 5. numpy.histogram()
a = np.arange(8)
hist, bin_edges = np.histogram(a, density=True)

# numpy.histogram() 将输入数组 a 和 bins 作为两个参数，其中 bins 数组的连续元素作为 bin 区间的边界值。
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
print(hist)
print(bins)

# 6. plt()
# pyplot 子模块的 plt() 函数将一个输入数组和 bins 数组作为参数，并将其输出为直方图
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")
plt.show()
