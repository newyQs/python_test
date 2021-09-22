# __slots__的作用：让一个类的对象只能有几个有效。这个值通常由一个元组表示
# 注意：__slots__只对类的对象的属性有所限制，对类的属性无限制
# 1.1定义一个只有sex属性的类
# class Human(object):
#     __slots__ = ("sex",)  # 固定有效的属性
#
#     def __init__(self):
#         self.sex = "女"
#         # self.age = 18  # 错误，不允许除 sex 以外的属性存在
#
#
# ruhua = Human()

# 1.2给类的对象绑定属性时也会出错
# ruhua.age = 18
# print(ruhua.age)

# 1.3给类绑定呢？有效
# 要注意 __slots__ 无法限制类的属性
# 定义类或动态绑定类的属性都是有效的
# Human.age = 22
# print(ruhua.age)

# 1.4在有继承关系的类中，如果只有基类有__slots__，子类没有__slots__，有且仅对当前类起作用
# class Human(object):
#     __slots__ = ("sex",)
#
#     def __init__(self):
#         self.sex = "女"
#         # self.name = "human"  # 错误，受 __slots__ 限制
#
#
# class Woman(Human):
#     def __init__(self):
#         Human.__init__(self)
#         self.age = 18  # 正确，不受基类的 __slots__ 限制
#
#
# hm = Human()  # hm 是基类对象
# ruhua = Woman()  # ruhua 是子类对象
# print(ruhua.age)

# 1.5如果想让子类的对象属性受限制，则也需要在子类中定义__slots__
# 这样子类对象限制的属性总和为子类限制的对象属性+父类限制对象的属性
# class Human(object):
#     __slots__ = ("sex",)
#
#     def __init__(self):
#         self.sex = "女"  # 正确，只受 Human 类中的 __slots__ 限制
#         # self.name = "如花"  # 错误，只受 Human 类中的 __slots__ 限制
#
#
# class Woman(Human):
#     __slots__ = ("name",)
#
#     def __init__(self):
#         self.sex = "女"  # 正确，符合基类中的 __slots__ 限制
#         self.name = "如花"  # 正确，符合子类中的 __slots__ 限制
#         # self.age = 18  # 错误，不符合基类和子类中的 __slots__ 限制
#
#
# ruhua = Woman()

# 1.6 如果只有子类中有 __slots__，而基类中没有定义 __slots__，
# 则子类中的 __slots__ 对子类的对象或基类中的对象都不起任何作用
class Human(object):
    def __init__(self):
        self.sex = "女"  # 正确，子类中的 __slots__ 不起任何作用
        self.name = "如花"  # 正确，子类中的 __slots__ 不起任何作用


class Woman(Human):
    __slots__ = ("name",)

    def __init__(self):
        self.sex = "女"  # 正确，子类中的 __slots__ 不起任何作用
        self.name = "如花"  # 正确，子类中的 __slots__ 不起任何作用
        self.age = 18  # 正确，子类中的 __slots__ 不起任何作用


ruhua = Woman()

# 2.总结：
'''
1.如果想要限制对象定义的属性，请使用__slots__。而__slots__在类中定义，一般以一个元组表示；
2.给类定义__slots__之后，在类的内部或外部绑定任何其他属性都不起作用；
3.__slots__只对对象的属性有所限制，而不限制类的属性；
4.__slots__只对当前定义的类有效，如果想要继承的子类有效，则需要在子类中也定义__slots__，这样子类中
 __slots__限制在子类+父类的__slots__总和
5.如果子类中定义了__slots__，而父类没有__slots__，则该__slots__对子类和父类都不起作用；

子类定义，父类未定义：子类和父类都不起作用
子类未定义，父类定义：子类不起作用
子类和父类都定义：子类限制在子类+父类定义
'''
