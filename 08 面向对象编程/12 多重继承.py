# 1.多重继承的写法
# class Human(object):
#     def __init__(self):
#         pass
#
#
# class Bird(object):
#     def __init__(self):
#         pass
#
#
# class BirdHuman(Human, Bird):
#     def __init__(self):
#         pass

# 2.多重继承的基本特性
# 2.1多重继承具有所有父类的属性和方法
# class Human(object):
#     human_name = "human"
#
#     def hh(self):
#         print(self.human_name)
#
#
# class Bird(object):
#     bird_name = "bird"
#
#     def bb(self):
#         print(self.bird_name)
#
#
# class BirdHuman(Human, Bird):
#     # pass # 如果不写(pass)，解释器自动调用下面语法
#     def __init__(self): # 在子类的构造函数中调用父类的构造函数
#         Human.__init__(self)
#         Bird.__init__(self)
#
#
# birdman = BirdHuman()
# birdman.hh()
# birdman.bb()
# print(birdman.human_name)
# print(birdman.bird_name)

# 2.2 多重继承的子类的多个父类中拥有重名的方法，则调用的是第一个继承的父类的方法
# 这里就不是就近原则了
# class Human(object):
#     def __init__(self):
#         self.humanname = "I'm a man"
#
#     def func(self):
#         print(self.humanname)
#
#
# class Bird(object):
#     def __init__(self):
#         self.birdname = "I'm a bird"
#
#     def func(self):
#         print(self.birdname)
#
#
# class BirdHuman(Human, Bird):  # 第一个继承的父类是 Human 类
#     def __init__(self):
#         Human.__init__(self)
#         Bird.__init__(self)
#
#
# birdman = BirdHuman()
# birdman.func()  # 调用的是 Human 类的 func 函数

# 2.3多重继承的子类的多个父类中有重名的属性，调用的是到目前为止给该属性赋值的类中的属性。
# 就近原则，从上至下
# class Human(object):
#     def __init__(self):
#         self.name = "human"
#
#
# class Bird(object):
#     def __init__(self):
#         self.name = "bird"
#
#
# class BirdHuman(Human, Bird):
#     def __init__(self):
#         Human.__init__(self)
#         Bird.__init__(self)
#
#
# birdman = BirdHuman()
# print(birdman.name)  # 最后一次调用的是 Bird 的构造函数，所以目前为止 name 为 bird
#
#
# class BirdHumanTwo(Human, Bird):
#     def __init__(self):
#         Bird.__init__(self)
#         Human.__init__(self)
#
#
# birdmantwo = BirdHumanTwo()
# print(birdmantwo.name)  # 最后一次调用的是 Human 的构造函数，所以目前为止 name 为 human

# 3.如果在我们 BirdHuman 类中，我们认为该类中含有的 Human 的功能比较多， 而 Bird 类中仅仅只是一个辅助类，
# 里面只有很少的属性和方法， 在 Python 中这种多重继承关系，我们把 Bird 这种辅助类叫作 MixIn，
# 我们写代码的时候要习惯于给辅助父类命名的时候加上 MixIn，当然你也可以不加上这个关键字
class Human(object):
    def __init__(self):
        pass


class BirdMixIn(object):
    def __init__(self):
        pass


class BirdHuman(Human, BirdMixIn):
    def __init__(self):
        pass


# 总结：
'''
1.python2 和 python3的多重继承规则？？？
2.多重继承中重名属性调用的是最近的赋值，而重名方法则是调用第一个继承的父类
3.对于继承功能较少的父类，可以使用MixIn
'''