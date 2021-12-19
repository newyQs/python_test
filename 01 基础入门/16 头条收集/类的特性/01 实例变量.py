"""
实例变量：
1.实例变量指的是可以被实例直接使用的变量；
2.啥叫实例呢？实例就是对象，就是由类创建出来的对象；
3.尽管我们用的是同一个类创建的，但是不同的实例在计算机中存储的的内存地址确实不一样的，每份实例都有一套自己的数据；
4.实例变量就是该实例所拥有的变量，在__init__构造方法里，通过self.变量名定义的变量都是实例变量；
5.我们可以在类内部通过self.变量名来引用实例变量。我们可以在类外通过对象名.变量名来调用该实例的变量；
"""


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


if __name__ == '__main__':
    stu1 = Student("张三", 18, "北京市海淀区")
    stu2 = Student("李四", 2, "上海市浦东新区")
    stu3 = Student("王五", 29, "广州市天河区")

    print(id(stu1), stu1.name)
    print(id(stu2), stu2.name)
    print(id(stu3), stu3.name)
