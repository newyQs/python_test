"""

"""


class People:
    def __init__(self, name, age, ):
        self.name = name
        self.age = age
        self.__privater_var = 10

    def intro(self):
        print(f'My name is {self.name},I\'m {self.age}')

    def get_var(self):
        print(self.__privater_var)

    def set_var(self, var):
        self.__privater_var = var


someone = People(name='jack', age=20)

someone.intro()

print(someone.age)

someone.get_var()  # 通过get_var方法访问私有属性__privater_var，值为10
someone.set_var(30)  # 通过set_var方法修改私有属性__privater_var，值为30
someone.get_var()  # 再次通过get_var方法访问私有属性__privater_var，值为30

'''
接下下来看看为什么我们使用someone.__privater_var会报错呢？
AttributeError: 'People' object has no attribute '__privater_var'

这里我们先使用 dir() 函数：
print(dir(someone)) #  获得当前someone的属性列表

结果：
['_People__privater_var', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'get_var', 'intro', 'name', 'set_var']
从打印出的结果中，我们并没有找到'_peivater_var'但是我们看到一个'_People__privater_var'.有没有想到什么？原来是被重命名了。好，我们来试试：

print(someone._People__privater_var)
someone._People__privater_var = 40
print(someone._People__privater_var)

结果：
30
40
所以说，私有变量的属性是可以修改的。既然Python阻止访问，一般情况下就不要访问
'''

