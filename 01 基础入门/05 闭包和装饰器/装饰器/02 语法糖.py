from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        before = time()
        rst = func(*args, **kwargs)
        after = time()
        print("该函数耗时：", after - before)
        return rst

    return wrapper


@timer  # func_one=timer(func_one)
def func_one(data):
    for i in range(1, data):
        data += i
    return data


@timer  # func_two=timer(func_two)
def func_two(data):
    for i in range(1, data):
        data -= i
    return data


@timer  # func_three=timer(func_three)
def func_three(data):
    for i in range(1, data):
        data *= i
    return data


func_one(25000)
func_two(25000)
func_three(25000)

'''
一个函数还可以同时定义多个装饰器，装饰器的执行顺序是从里到外，最先调用最里层的装饰器，
最后调用最外层的装饰器，比如以下函数有三个装饰器，该装饰器函数等同于：f = a(b(c(f)))
@a
@b
@c
def f():
    pass

'''
