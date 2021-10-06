from time import time


def timer(funcname):
    def decorate(func):
        def wrapper(*args, **kwargs):
            before = time()
            rst = func(*args, **kwargs)
            after = time()
            print(funcname + "耗时：", after - before)
            return rst
        return wrapper
    return decorate


# 函数 1
@timer("func_one函数")
def func_one(data):
    for i in range(1, data):
        data += i
    return data


# 函数 2
@timer("func_two函数")
def func_two(data):
    for i in range(1, data):
        data -= i
    return data


# 函数 3
@timer("func_three函数")
def func_three(data):
    for i in range(1, data):
        data *= i
    return data


func_one(25000)
func_two(25000)
func_three(25000)
