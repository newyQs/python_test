"""
1.实例方法由实例进行调用，要求方法第一个参数是self(自己改个名字也行);
2.第一个参数self代表的是实例本身(实例的地址),这个第一个参数类似于java c++里的this指针;
3.通过这个第一个参数可以访问该实例的其他实例变量和实例方法;
4.调用实例方法的时候通过实例名.实例方法进行调用
"""


class Student:
    def __init__(self, name, age, address):
        self.__name = name
        self.age = age
        self.address = address

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        print(self.__name)

    def print_info(self):
        print(self.__name, self.age, self.address)


if __name__ == '__main__':
    stu1 = Student("李华", 19, "深圳市宝安区")
    stu1.print_info()
    stu1.get_name()
    stu1.set_name("张三")
    stu1.get_name()
    stu1.print_info()
