# python中函数的默认参数是局部变量，在第一次使用的时候，其内存就已经确定了，不会在每次调用时重新分配内存
# 下面两次调用，其id是一样的
def func(L=[]):
    print(id(L))
    L.append(1)
    print(L)


func()
func()


# 函数内定义
# 两次调用 L 指向的内存确实不是一个（第一次结果为 [2]， 第二次结果为 [2]），但是打印出的内存地址确是一样的
def func1():
    L = []
    print(id(L))
    L.append(2)
    print(L)


func1()
func1()


# 内存分配机制是一样的
def func3():
    L = []
    print(id(L))
    L.append(3)
    print(L)


func3()
mylist = []
print(id(mylist))
func3()


# 通过将默认参数设定为不变对象
def func4(L=None):
    if not isinstance(L, list):
        L = []
    L.append(2)
    print(L)

# func4()
# func4()
