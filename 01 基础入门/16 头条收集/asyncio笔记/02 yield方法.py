"""

"""


# 创建生成器函数
def fun1():
    yield 1
    yield from fun2()
    yield 2


def fun2():
    yield 3
    yield 4


f = fun1()
for item in f:
    print(item)
