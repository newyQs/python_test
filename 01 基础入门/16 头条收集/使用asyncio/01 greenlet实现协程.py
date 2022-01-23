"""
https://blog.csdn.net/zhouxuan612/article/details/120736002
"""
from greenlet import greenlet


def fun1():
    print(111)
    gr2.switch()
    print(222)
    gr2.switch()


def fun2():
    print(333)
    gr1.switch()
    print(444)


if __name__ == '__main__':
    gr1 = greenlet(fun1)
    gr2 = greenlet(fun2)

    gr1.switch()
