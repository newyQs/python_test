"""
1.类方法顾名思义，就是属于类的方法。可以被类调用，也可以被实例调用；
2.类方法定义的时候必须借助@classmethod装饰器来才能定义；
3.类方法的第一个参数不是self(代表实例本身),而是cls(代表类本身),然后通过这个cls来访问类的其他类变量和类方法
"""


class Student:
    school = "清华大学"
    address = "北京市海淀区"

    def __init__(self, name, age, address):
        self.__name = name
        self.age = age
        self.address = address

    @classmethod
    def print_info(cls):
        print(cls.school, cls.address)


if __name__ == '__main__':
    stu1 = Student("张三", 18, "深圳市宝安区")

    Student.print_info()
    stu1.print_info()
