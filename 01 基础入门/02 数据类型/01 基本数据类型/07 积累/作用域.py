"""
对于变量作用域，变量的访问以 L（Local） –> E（Enclosing） –> G（Global） –>B（Built-in） 的规则查找，
即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
"""

# 1.内部函数，不修改全局变量可以访问全局变量
a = 10


def func():
    b = a + 2  # 仅仅访问全局变量 a
    print(b)


func()

# 2.内部函数，修改同名全局变量，则python会认为它是一个局部变量
b = 10


def func():
    b = b + 1  # 修改同名的全局变量，则认为是一个局部变量
    print(b)


func()

# 3. global 和 nonlocal？
# nonlocal 只能修改外层函数的变量而不能修改外层函数所引用的全局变量
x = 0


def outer():
    global x
    x = 1

    def inner():
        nonlocal x
        x = 2
        print(x)

    inner()


outer()
print(x)


# global 关键字会跳过中间层直接将嵌套作用域内的局部变量变为全局变量:
def outer():
    num = 10

    def inner():
        global num
        print(num)
        num = 100
        print(num)

    inner()
    print(num)


outer()
print(num)
