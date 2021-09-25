# 把属性设置私有的，让用户通过 get 和 set 来访问属性
class Human(object):
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        try:
            age = int(age)
            if age < 0:
                print('年龄不能为负数')
            else:
                self._age = age
        except TypeError:
            print('年龄调整失败，请输入数字')


jack = Human(19)
print(jack.get_age())

jack.set_age(20)
print(jack.get_age())


# 将函数变成属性，
class Human(object):
    def __init__(self, age=0):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        try:
            age = int(age)
            if age < 0:
                print("年龄不能为负数，年龄调整失败")
            else:
                ruhua.__age = age
        except TypeError:
            print("请输入整数，年龄调整失败")


ruhua = Human()
ruhua.age = 18
print(ruhua.age)
