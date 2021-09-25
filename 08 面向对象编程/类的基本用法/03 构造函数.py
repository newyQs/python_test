# 1.构造函数，使得每个实例都能具有相同的属性，但不同的属性值
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("大家好，我是%s；我的年龄是%s" % (self.name, self.age))


luren_a = Human("ruhua", 18)  # Python 解释器会自动调用构造函数，并把 luren_a 作为第一个实参传给构造函数
print(luren_a.name)
luren_a.speak()

luren_b = Human("xingxing", 17)  # Python 解释器会自动调用构造函数，并把 luren_b 作为第一个实参传给构造函数
print(luren_b.name)
luren_b.speak()


# 2.将通用的属性定义在构造函数外面
class Circle:
    PI = 3.1415926

    def __init__(self, radius):
        self.radius = radius

    def show_area(self):
        print(self.radius * self.PI)


red_circle = Circle(3)
red_circle.show_area()  # 用的是类的属性 PI

blue_circle = Circle(5)  # 用的是类的属性 PI
blue_circle.show_area()

Circle.PI = 1  # 可以通过类改变属性 PI
print(red_circle.PI)  # 用的是类的属性 PI
print(blue_circle.PI)  # 用的是类的属性 PI


# 通过对象修改类的属性时，只是改变了当前对象的指向
class Circle:
    PI = 3.1415926

    def __init__(self, radius):
        self.radius = radius


red_circle = Circle(3)
blue_circle = Circle(5)
red_circle.PI = 1  # 只是改变了 red_circle 对象的属性 PI 指向

print(red_circle.PI)  # 1
print(blue_circle.PI)  # blue_circle 对象的属性 PI 还在指向 Cirle 类的属性 PI
print(Circle.PI)  # Circle 类的属性 PI 只能通过 Cirle 类来改变
