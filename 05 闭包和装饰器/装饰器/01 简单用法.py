# 装饰器经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景
# 概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能
from time import time


# 函数 1
def func_one(data):
    for i in range(1, data):
        data += i
    return data


# 函数 2
def func_two(data):
    for i in range(1, data):
        data -= i
    return data


# 函数 3
def func_three(data):
    for i in range(1, data):
        data *= i
    return data


# 改动 1
def timer(func, data):
    before = time()
    func(data)
    after = time()

    return after - before


print('该函数用时：', timer(func_one, 25000))
print('该函数用时：', timer(func_two, 25000))
print('该函数用时：', timer(func_three, 25000))


# 改动 2
def timer(func):
    def wrapper(data):
        before = time()
        rst = func(data)
        after = time()
        print("该函数耗时：", after - before)

        return rst

    return wrapper


func_one = timer(func_one)
func_two = timer(func_two)
func_three = timer(func_three)

func_one(25000)
func_two(25000)
func_three(25000)


# 改动 3 ：函数有参数
def timer(func):
    def wrapper(*args, **kwargs):
        before = time()
        rst = func(*args, **kwargs)
        after = time()
        print("该函数耗时：", after - before)

        return rst

    return wrapper
