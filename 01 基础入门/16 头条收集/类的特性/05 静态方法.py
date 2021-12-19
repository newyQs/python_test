"""
1.静态方法是通过@staticmethod装饰器进行修饰的方法，静态方法的参数没有特殊要求，第一个参数即不代表实例，也不代表类，可以为空；
2.静态方法既可以通过类名调用，也可以通过实例名调用；
3.注意，静态方法无法直接访问实例变量和类变量，也无法直接调用实例方法和类方法；
3.建议类方法和静态方法都是通过类名来调用；
"""


class Student:
    school = "清华大学"
    address = "北京市海淀区"

    def __init__(self, name, age, address):
        self.__name = name
        self.age = age
        self.address = address

    @classmethod
    def get(cls):
        print(cls.school)

    @staticmethod
    def print_info():
        print("打印~~~")

    @staticmethod
    def print():
        Student.get()


if __name__ == '__main__':
    stu1 = Student("张三", 18, "深圳市宝安区")

    Student.print_info()
    stu1.print_info()

    Student.print()
