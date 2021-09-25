class Human:
    name = "ruhua"


luren_a = Human()
# 1.给实例对象绑定一个属性，该属性只会作用于当前对象
luren_a.age = 18
print(luren_a.age)


def speak():
    print("大家好，我是 ruhua")


# 2.给实例对象绑定一个方法，该方法只会作用于当前对象
luren_a.speak = speak
luren_a.speak()


# 3.给类绑定属性和方法，可以作用于所有的实例对象
class Human:
    name = "ruhua"


# 3.1 给类绑定方法时，需要添加一个self参数，接收实例对象本身
def speak(self):
    print("大家好，我是" + self.name)


luren_a = Human()
luren_b = Human()

# 3.2 给类绑定属性和方法
Human.age = 18
Human.speak = speak

print(luren_a.age)
luren_a.speak()

print(luren_b.age)
luren_b.speak()
