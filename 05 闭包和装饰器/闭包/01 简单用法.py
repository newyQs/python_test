'''
简单来说，闭包就是一个函数定义中引用了函数外定义的变量，并且该函数可以在其定义环境外被执行
闭包从表现形式上看，如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure)
'''


# 1.示例
def outer(x):
    def inner(y):
        return x + y

    return inner


# 2.闭包无法修改外部函数的局部变量
def outer1():
    x = 200

    def inner():
        x = 250
        print("inner x:", x)

    print("outer x:", x)  # 调用 inner 函数之前
    inner()
    print("outer x:", x)  # 调用 inner 函数之后


# outer1()

# 3.闭包无法直接访问/修改外部函数的局部变量
def outer2():
    x = 250

    def inner():  # 上面一行的 x 相对 inner 函数来说是函数外的局部变量（非全局变量）
        x += x
        return x

    return inner


# outer2()()

# 3.1但是我们可以间接地通过容器类型来解决，因为容器类型是不存放在栈空间的，inner 函数可以访问到
def outer3():
    x = [250]

    def inner():
        x[0] += x[0]
        return x[0]

    print('3.1修改前', x[0])  # 250
    print(inner())  # 500
    print('3.1修改后', x[0])  # 500


# outer3()

# 3.2 我们也可以通过 nonlocal 关键字来解决，该语句显式的指定 x 不是闭包的局部变量
def outer4():
    x = 250

    def inner():
        nonlocal x  # 把 x 声明为非局部变量
        x += x
        return x

    return inner


# print(outer4()())

# 4.循环中不包含域的概念
# 4.1 当循环结束以后，循环体中的临时变量 i 不会销毁，而是继续存在于执行环境中，所以在循环外部 i 的结果为 9
for i in range(10):
    pass

# print(i)  # 9


# 4.2 python 的函数只有在执行时，才会去找函数体里的变量的值
flist = []
for i in range(3):
    def foo(x):
        print(x + i)


    flist.append(foo)

for f in flist:
    f(2)

# loop 在 python 中是没有域的概念的，flist 在像列表中添加 func 的时候，并没有保存 i 的值，
# 而是当执行 f(2)的时候才去取，这时候循环已经结束，i 的值是 2，所以结果都是 4
# 4.3 解决以上问题，改写一下函数的定义就可以
flist = []
for i in range(3):
    def foo(x, y=i):
        print(x + y)


    flist.append(foo)

for f in flist:
    f(2)

# 5.闭包的作用
# 闭包可以保存当前的运行环境，以一个类似棋盘游戏的例子来说明
# 假设棋盘大小为 50*50，左上角为坐标系原点（0,0），我需要一个函数，接收 2 个参数，分别为方向（direction），步长（step），
# 该函数控制棋子的运动。这里需要说明的是，每次运动的起点都是上次运动结束的终点
origin = [0, 0]
legal_x = [0, 50]
legal_y = [0, 50]


def create(pos=origin):
    def player(direction, step):
        '''
        这里应该首先判断参数 direction,step 的合法性
        比如 direction不能斜着走，step不能为负等
        然后还要对新生成的 x，y 坐标的合法性进行判断处理
        这里主要是想介绍闭包，算法就不详细写了。
        '''

        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step
        pos[0] = new_x
        pos[1] = new_y

        # 注意！此处不能写成 pos = [new_x, new_y]，因为参数变量不能被修改，而 pos[] 是容器类的解决方法
        return pos

    return player


player = create()  # 创建棋子 player，起点为原点
print(player([1, 0], 10))  # 向x轴正方向移动10步
print(player([0, 1], 20))  # 向y轴正方向移动20步
print(player([-1, 0], 10))  # 向x轴负方向移动10步


# 6.
def fun():
    temp = [lambda x: x * i for i in range(4)]
    return temp


for every in fun():
    print(every(2))
