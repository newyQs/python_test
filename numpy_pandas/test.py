# 1.元组本身不可修改，但内部可变元素（如列表）可修改
t = (1, [2, 4, 5], 6)
t[1][0] = 3
print(t)

# 检测列表extend和append方法的效率
from time import time


def timer(func):
    def wraper(*args, **kwargs):
        before = time()
        func(*args, **kwargs)
        after = time()
        print("该函数耗时：", after - before)

    return wraper


@timer
def func_one(data):
    l = []
    for i in range(1, data):
        l.append(i)
    return l


@timer
def func_two(data):
    l = []
    for i in range(1, data):
        l.extend([i])
    return l

func_one(10000000)
func_two(10000000)