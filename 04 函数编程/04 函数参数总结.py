# 函数参数分为以下5种类型：


# 1.位置参数：一一对应，数量一致
# 不对参数作校检
def func1(name, age):
    print(f'name={name},age={age}')


func1('lee', 18)
func1(18, 'lee')


# 2.默认参数：如果不传，使用默认值，传了使用传了的值
# 注意默认参数在位置参数后面
def func2(name='jack', age=18):
    print(f'name={name},age={age}')


func2()
func2(age=19, name='lucy')

func2(age=22)
func2('lee')


# 3.可变参数
# 接收任意个参数，返回一个tuple
def func3(*args):
    print(args)


func3()
func3(1)
func3(1, [2, 3])

func3((1, 2, 3))
func3(*(1, 2, 3))


# 4.关键字参数
# 接受任意个命名的参数，返回一个dict
def func4(**kwargs):
    print(kwargs)


func4(name='lee', age=18)
func4(**{'name': 'jack', 'age': 18})


# 5.命名关键字参数
# 使用*或者有一个可变参数*arg
def func5(*, name='lee', age=18):
    print(f'name={name},age={age}')


func5()
func5(name='jack')


def func6(*args, name='kelly', age=18):
    print(args)
    print(f'name={name},age={age}')


func6()
func6(name='tom')
func6(name='rouse', age=10)
func6(12, name='kate', age=19)


# 关于*args和**kwargs
def function(*args, **kwargs):
   pass