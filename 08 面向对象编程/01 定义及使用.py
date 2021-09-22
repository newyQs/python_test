# 定义一个类
class Human:
    pass


# print(type(Human))  # <class 'type'>

# 实例化2个对象。注意每个对象都是独立的
pep = Human()
# print(type(pep))  # <class '__main__.Human'>
pep_ = Human()


# 给类添加属性和方法
class Human:
    name = 'jack'

    def get_name(self):
        print(id(self))
        print(self.name)


pep_a = Human()
pep_b = Human()
pep_a.get_name()
pep_b.get_name()
