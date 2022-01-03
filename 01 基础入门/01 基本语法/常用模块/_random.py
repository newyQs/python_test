"""
random.randrange
random.randint
random.choice
random.choices
random.shuffle
random.random
random.uniform
"""
import random

# 1. 簿记功能
# random.seed(a=None, version=2) -> 初始化随机数生成器
ret = random.seed(a=None, version=2)
print(ret)

# 2. 整数用函数
# random.randrange(stop)
# random.randrange(start, stop[, step]) -> 从 range(start, stop, step) 返回一个随机选择的元素
print(random.randrange(10))

# random.randint(a, b) -> 返回随机整数 N 满足 a <= N <= b。相当于 randrange(a, b+1)
print(random.randint(2, 10))

# 3. 序列用函数
# random.choice(seq) -> 从非空序列 seq 返回一个随机元素
print(random.choice("abc"))

# random.choices(population, weights=None, *, cum_weights=None, k=1) -> 从*population*中选择替换，返回大小为 k 的元素列表
print(random.choices("abc"))

# random.shuffle(x[, random]) -> 将序列 x 随机打乱位置
lis = [1, 2, 3]
random.shuffle(lis)
print(lis)

# random.sample(population, k) -> 返回从总体序列或集合中选择的唯一元素的 k 长度列表
print(random.sample("abc", 2))

# 4. 实值分布
# random.random() -> 返回 [0.0, 1.0) 范围内的下一个随机浮点数
print(random.random())

# random.uniform(a, b) -> 返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a
print(random.uniform(2, 10))

# random.triangular(low, high, mode) -> 返回一个随机浮点数 N ，使得 low <= N <= high 并在这些边界之间使用指定的 mode
print(random.triangular(2, 7))
