"""
global 和 nonlocal的作用：
https://www.cnblogs.com/yuzhanhong/p/9183161.html

"""
# 1 global
# 1.1 global关键字用来在**函数或其他局部作用域**中使用全局变量。但是如果不修改全局变量也可以不使用global关键字。
gcount = 0


def global_test1():
    gcount += 1  # 在函数内部修改了全局变量
    print(gcount)


"""
以上代码会报错：第一行定义了全局变量，在内部函数中又对外部函数进行了引用并修改，
那么python会认为它是一个局部变量，又因为内部函数没有对其gcount进行定义和赋值，所以报错。
"""

# 1.2 如果局部要对全局变量修改，则在局部声明该全局变量
gcount = 0


def global_test2():
    global gcount  # 声明为全局变量，这样就可以修改了
    gcount += 1
    print(gcount)


# 1.3 如果局部不声明全局变量，并且不修改全局变量，则可以正常使用
gcount = 0


def global_test():
    print(gcount)  # 函数内部可以正常使用全局变量，但是不能修改，修改需要使用global关键字声明为全局变量


global_test()


# 2 nonlocal
# 2.1  nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
def make_counter():
    count = 0

    def outer():
        def counter():
            nonlocal count
            count += 1
            return count

        return counter

    return outer


# 3 混合使用
def scope_test():
    def do_local():
        # 此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。
        # 此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam  # 使用外层的spam变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

if __name__ == '__main__':
    ret = make_counter()
    print(ret()())
