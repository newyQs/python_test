# 1.使用types 模块的 MethodType 函数
# 1.1 给类的对象绑定函数
from types import MethodType


class Human(object):
    pass


def sex(self):
    print("女")


ruhua = Human()
zhaoritian = Human()
ruhua.printsex = MethodType(sex, ruhua)
ruhua.printsex()  # 调用绑定的 printsex 函数
zhaoritian.printsex()  # 错误


# 1.2给类绑定函数
class Human(object):
    pass


def sex(self):
    print("女")


ruhua = Human()
zhaoritian = Human()
Human.printsex = MethodType(sex, Human)
ruhua.printsex()  # 调用绑定的 printsex 函数
zhaoritian.printsex()  # 调用绑定的 printsex 函数

# 2.为什么使用MethodType 函数对对象进行动态绑定函数时，被绑定的函数需要 self 参数，
# 而我们前面讲的直接给对象进行动态绑定函数不需要这个参数
from types import MethodType


class Human(object):
    pass


def sex(self):  # 需要 self 参数
    print("女")


def printage():  # 不需要 self 参数
    print(18)


ruhua = Human()
zhaoritian = Human()

# 使用MethodType
ruhua.printsex = MethodType(sex, ruhua)
ruhua.printsex()

# 不使用
ruhua.printage = printage
ruhua.printage()
