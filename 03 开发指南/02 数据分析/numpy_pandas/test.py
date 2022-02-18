import time

# 1. 元组本身不可修改，但内部可变元素（如列表）可修改
t = (1, [2, 4, 5], 6)
t[1][0] = 3
print(t)


# 2. 验证列表extend和append方法的效率


def timer(func):
    def wraper(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print("该函数耗时：", after - before)

    return wraper


@timer
def func_one(data):
    mylist = []
    for i in range(1, data):
        mylist.append(i)

    return mylist


@timer
def func_two(data):
    mylist = []
    for i in range(1, data):
        mylist.extend([i])

    return mylist


if __name__ == '__main__':
    func_one(10000000)
    func_two(10000000)
