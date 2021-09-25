# 1.动态语言和静态语言，强类型语言和弱类型语言的区别和联系？？？


# 2.使用type创建类
def func(self, name):  # 在类之前定义要绑定的函数
    print("I'm " + name)


# type(类的名称，继承的父类元组，类的方法名称和函数绑定)
Human = type('Human', (object,), {"talk": func})  # 创建 Human 类，该类继承 object，有一个talk函数
ruhua = Human()
ruhua.talk("ruhua")


# 3.给类绑定属性和方法
def func(self):
    print("我是类绑定的")


def func2():
    print("我是某个对象绑定的")


Human = type('Human', (object,), {})  # 后面动态绑定
Human.func = func
Human.data = "我是类的属性"

ruhua = Human()
ruhua.func2 = func2
ruhua.data2 = "我是某个对象的属性"

ruhua.func()  # 正确
print(ruhua.data)  # 正确
ruhua.func2()  # 正确
print(ruhua.data2)  # 正确

zhaoritian = Human()
zhaoritian.func()  # 正确
print(zhaoritian.data)  # 正确
zhaoritian.func2()  # 错误
print(zhaoritian.data2)  # 错误

# 4.使用 metaclass 创建类
'''
除了使用 type 动态创建类以外，还可以使用 自己定义的元类（metaclass）来创建类，
自己定义一个元类，首先该类要继承 type 类，我们还需要定义一个 __new__ 函数，
__new__ 函数接收到的参数依次是：当前准备创建的类的对象，类的名字，类继承的父类集合，类的函数集合。
我们在使用 metaclass 创建类，按照默认习惯，metaclass 的类名总是以 Metaclass 结尾，以便清楚地表示这是一个 metaclass。
'''


class MyObjectMetaclass(type):
    def __new__(cls, name, bases, funcs):
        def setdata(self, value):
            self.data = value

        funcs['setdata'] = setdata
        return type.__new__(cls, name, bases, funcs)


class MyObject(object, metaclass=MyObjectMetaclass):
    pass


myobject = MyObject()
myobject.setdata("hello")
print(myobject.data)
