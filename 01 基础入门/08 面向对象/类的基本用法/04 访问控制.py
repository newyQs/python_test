# 1.最好不要直接通过对象来访问（读或写）属性， 而是通过类提供的函数进行读写属性操作
class Human:
    def __init__(self, my_name):
        self.name = my_name

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name


luren_a = Human("ruhua")
print(luren_a.get_name())  # 访问属性
luren_a.set_name("wanghuahua")  # 修改属性
print(luren_a.get_name())


# 2.为了让内部属性不被外部访问， 我们可以在属性的名称前加上两个下划线 __
# 实例的变量名如果以 __ 开头，就变成了一个私有变量：只有在类的内部可以访问（读写），在类的外部不能访问
class Human:
    def __init__(self, my_name):
        self.__name = my_name

    def get_name(self):
        return self.__name  # 类的内部可以访问

    def set_name(self, new_name):
        self.__name = new_name  # 类的内部可以访问


luren_a = Human("ruhua")
print(luren_a.get_name())

luren_a.set_name("wanghuahua")
print(luren_a.get_name())

print(luren_a.__name)  # 报异常，因为类的外部无法访问
luren_a.__name = "wanghuahua"  # 报异常，因为类的外部无法访问


# 2.1  Python 在类内部把所有以 __ 开头的变量进行了更名，如果我们知道更改后的属性名，就可以在外部进行访问该属性
class Human:
    def __init__(self, my_name):
        self.__name = my_name


luren_a = Human("lucy")
print(luren_a._Human__name)  # Python 3.7 版本把名字改成了 _Human__name

Human.__name = "jack"
print(luren_a.__name)  # Python 只对类内部 __开头的变量做改名，所以可以访问

# 我们可以通过 id 函数知道它们并不是一个变量
print(id(luren_a.__name))
print(id(luren_a._Human__name))

# 3.单下划线的变量，可以在外部访问，但不建议这么做
