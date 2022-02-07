"""
1.类变量指的是定义在Python类中，方法之外的变量;
2.类变量是由所有该类创建出来的对象共享的变量，每个对象都可以访问修改类变量;
3.我们可以通过实例名.类变量名来访问类变量，也可以通过类名.类变量进行访问;
"""


class Student:
    school = "清华大学"
    postal_code = "100091"

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


if __name__ == '__main__':
    stu1 = Student("张三", 18, "北京市海淀区")
    stu2 = Student("李四", 2, "上海市浦东新区")

    print(id(stu1), stu1.name, stu1.school, stu1.postal_code)

    Student.school = "清华大学"
    stu1.postal_code = "100084"

    print(id(stu1), stu1.name, stu1.school, stu1.postal_code)
    print(id(stu2), stu2.name, stu2.school, stu2.postal_code)
