from time import time


# 使用类装饰器主要依靠类的 __call__ 方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法
class Timer(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, arg):
        before = time()
        rst = self._func(arg)
        after = time()
        print("该函数耗时：", after - before)
        return rst


@Timer
def func_one(data):
    for i in range(1, data):
        data += i
    return data


func_one(25000)


# 创建一个装饰器把下面函数输出的字符串首字母大写
def greetings(word="hi jack 马，I'm you brother dongdong"):
    return word.lower()
