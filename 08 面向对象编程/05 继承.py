# 继承的概念
# 1.定义一个类，可以从现有类中继承，该类称为子类，而被继承的类称为父类，基类或超类；
# 2.一切皆对象？object。注意在py3中继承不继承object是一样的，但py2不一样，有啥区别？
# 3.如若写出一种py2和py3通用的代码，建议都继承object；

# 4.子类继承父类的所有属性和方法
# class Animal(object):
#     name = "Animal"  # Animal 类的属性
#
#     def talk(self):  # Animal 类的方法
#         print("Animal talking")
#
#
# class Cat(Animal):  # 继承Animal类
#     pass
#
#
# class Bird(Animal):  # 继承Animal类
#     pass
#
#
# onecat = Cat()
# onebird = Bird()
#
#
# print(onecat.name)
# onecat.talk()
#
# print(onebird.name)
# onebird.talk()

# 5.拥有构造函数的父类
class Animal(object):
    def __init__(self):
        self.name = "Animal"

    def talk(self):
        print("Animal talking")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)  # 把子类对象本身传给父类的构造函数


class Bird(Animal):
    def __init__(self):
        # Animal.__init__(self)
        # super(Bird, self).__init__()
        super().__init__()


onecat = Cat()
onebird = Bird()

print(onecat.name)
onecat.talk()

print(onebird.name)
onebird.talk()

# 6.我们只要能把子类的对象传给父类，并且在父类中给该对象定义属性，子类对象都会拥有该属性
# 但是通常我们都是在子类的构造函数中调用父类的构造函数来初始化属性
# class Animal(object):
#     def __init__(self):
#         self.name = "Animal"
#
#     def what(self):
#         self.what = 250
#
#
# class Cat(Animal):
#     def __init__(self):
#         Animal.what(self)  # 把子类对象本身传给父类的 what 函数
#
#     def haha(self):
#         Animal.__init__(self)  # 把子类对象本身传给父类的构造函数
#
#
# onecat = Cat()
#
# print(onecat.name)  # 错误
# print(onecat.what)  # 正确
#
# onecat.haha()
# print(onecat.name)  # 正确

# 7.当子类中没有构造函数时，解释器会自动为子类添加构造函数并继承父类的构造函数
# 但是如果子类有构造函数时就不会默认添加了，需要手动继承父类的构造函数

# 8.继承父类构造函数的两种方法：父类.__init__ 函数或者 super(类名, 对象).__init__ 函数

# 9.几个概念
# 类中所有的成员函数都是属于类的，因为成员函数（不包含里面的变量）是代码，
# 这些代码存放在代码段中，所有对象共用这份代码，所以不存在属于某个对象的成员函数；
# 成员变量有属于对象的（在函数内部定义），也有属于类的（在类内非函数内部定义）
# class Animal(object):
#     name = "Animal"  # 属于类的成员变量
#
#     def __init__(self):  # 成员函数都是属于类的，构造函数也是成员函数
#         self.nameex = "Animalex"  # 属于 self 对象的成员变量
#
#     def talk(self):  # 成员函数都是属于类的
#         self.nameexex = "Animalexex"  # 属于 self 对象的成员变量
#         print("Animal talking")

# 9.1如果我们子类中的属于类的变量或函数和父类中的属于类的变量或函数重名，通过子类的对象访问该重名变量或重名函数都是子类的
# class Animal(object):
#     name = "Animal"
#
#     def talk(self):
#         print("Animal talking")
#
#
# class Bird(Animal):
#     name = "Bird"
#
#     def talk(self):
#         print("Bird talking")
#
#
# onebird = Bird()
# print(onebird.name)  # Bird 类的 talk 成员函数
# onebird.talk()  # Bird 类的 name 成员变量

# 9.2 但是如果是子类属于对象的变量和父类对象中的变量重名，则根据对象本身赋值顺序而定
# class Animal(object):
#     def __init__(self):
#         self.name = "Animal"
#
#
# class Bird(Animal):
#     def __init__(self):
#         Animal.__init__(self)  # 在父类中先给 onebird 对象的 name 赋值为 "Animal"
#         self.name = "Bird"  # 然后改写 onebird 对象的 name 值为 "Bird"
#
#
# onebird = Bird()
# print(onebird.name)  # "Bird"
#
#
# # ---------我是分割线---------
# class Animal(object):
#     def __init__(self):
#         self.name = "Animal"
#
#
# class Bird(Animal):
#     def __init__(self):
#         self.name = "Bird"  # 先给 onebird 对象的 name 赋值为 "Bird"
#         Animal.__init__(self)  # 然后在父类中改写 onebird 对象的 name 值为 "Animal"
#
#
# onebird = Bird()
# print(onebird.name)  # "Animal"
