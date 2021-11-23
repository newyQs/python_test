# 1.位置参数：又称必传参数，参数是一一对应的
def myfunc(name, age):
    print(name)
    print(age)


# myfunc("ruhua", 18)  # 实参 "ruhua" 对应形参 name，实参 18 对应形参 age
# myfunc("ruhua", "zhaoritian", 18)  # 错误，实参和形参的个数不匹配

# 2.默认参数：确保位置参数在前，默认参数在后
def girlsschool(name, sex="female"):
    print(name)
    print(sex)


# girlsschool("wanghuahua")
# girlsschool("ruhua", "male")

# 3.可变参数
# 无论传入多少个位置参数，都会组成一个tuple
def func1(*arg):
    print(arg)


# func1()
# func1(1)
# func1(1, 2, 3)


# 如果可变参数在位置参数或默认参数的前面，就变成了命名关键字参数

# 4.关键字参数
# 无论传入多少个默认参数，都会组装成一个dict
# 确保关键字参数在可变参数和默认参数和位置参数前面
def func2(**arg):
    print(arg)


# func2()
# func2(name="ruhua", age=18)


# 5.命名关键字参数
# 和关键字参数不同，命名关键字参数需要一个特殊分隔符 * ，* 后面的参数被视为命名关键字参数
def Human(name, age, *, sex, lover):
    print(name, age, sex, lover)


# Human('ruhua', 18, sex='f', lover='tangbohu')
# Human('ruhua', 18, 23, sex='f', lover='tangbohu') # 错误


# 5.1 如果函数定义中已经有了一个可变参数，后面的命名关键字参数就不再需要一个特殊分隔符 *
def Human1(name, age, *args, sex, lover):
    print(name, age, args, sex, lover)


# Human1('ruhua', 18, sex='female', lover='tangbohu')  # ruhua 18 () female tangbohu
# Human1('ruhua', 18, 22, sex='female', lover='tangbohu')  # ruhua 18 (22,) female tangbohu


# 5.2 命名关键字参数必须传入参数名
def Human2(name, age, *, sex, lover):
    print(name, age, sex, lover)


# Human2('ruhua', 18, 'f', 'tangbohu')  # 必须要指定参数名 sex 和 lover


# 6.各种参数的组合使用
# 位置参数，默认参数，可变参数和关键字参数
def function(pos, default="ok", *args, **kwargs):
    pass
