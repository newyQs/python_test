# 1.位置参数：又称必传参数，一一对应，数量一直
def myfunc(name, age):
    print(name)
    print(age)


# myfunc("ruhua", 18)  # 实参 "ruhua" 对应形参 name，实参 18 对应形参 age
# myfunc("ruhua", "zhaoritian", 18)  # 错误，实参和形参的参数个数不匹配

# 2.默认参数：确保位置参数在前，默认参数在后
def girlsschool(name, sex="f"):
    print(name)
    print(sex)


# girlsschool("wanghuahua")
# girlsschool("ruhua", "m")


# 2.1
# python中函数的默认参数是局部变量，在第一次使用的时候，其内存就已经确定了，不会在每次调用时重新分配内存
# 下面两次调用，其id是一样的
def func(L=[]):
    print(id(L))
    L.append(2)
    print(L)


# func()
# func()

# 2.2
# 函数内定义
# 两次调用 L 指向的内存确实不是一个（第一次结果为 [2]， 第二次结果为 [2]），但是打印出的内存地址确是一样的
def func1():
    L = []
    print(id(L))
    L.append(2)
    print(L)


# func1()
# func1()


# 2.3
# 内存分配机制是一样的
def func3():
    L = []
    print(id(L))
    L.append(2)
    print(L)


# func3()
# mylist = []
# print(id(mylist))
# func3()


# 2.4
# 通过将默认参数设定为不变对象
def func4(L=None):
    if not isinstance(L, list):
        L = []
    L.append(2)
    print(L)


# func4()
# func4()

# 3.可变参数
# 无论传入多少个位置参数，都会组成一个tuple
def func5(*arg):
    print(arg)


# func5()
# func5(1)
# func5(1, 2, 3)


# 如果可变参数在位置参数或默认参数的前面，就变成了命名关键字参数

# 4.关键字参数
# 无论传入多少个默认参数，都会组装成一个dict
# 确保关键字参数在可变参数和默认参数和位置参数前面
def func6(**arg):
    print(arg)


# func6()
# func6(name="ruhua", age=18)


# 5.命名关键字参数
# 和关键字参数不同，命名关键字参数需要一个特殊分隔符 * ，* 后面的参数被视为命名关键字参数
def Human(name, age, *, sex, lover):
    print(name, age, sex, lover)


# Human('ruhua', 18, sex='f', lover='tangbohu')

# 5.1如果函数定义中已经有了一个可变参数，后面的命名关键字参数就不再需要一个特殊分隔符 *
def Human1(name, age, *args, sex, lover):
    print(name, age, args, sex, lover)


# Human1('ruhua', 18, sex='f', lover='tangbohu')

# 5.2 命名关键字参数必须传入参数名
def Human2(name, age, *, sex, lover):
    print(name, age, sex, lover)


Human2('ruhua', 18, 'f', 'tangbohu')  # 必须要指定参数名 sex 和 lover


# 6.各种参数的组合使用
# 必选参数，默认参数，可变参数和关键字参数
def func0(a, b="ok", *c, **d):
    pass
