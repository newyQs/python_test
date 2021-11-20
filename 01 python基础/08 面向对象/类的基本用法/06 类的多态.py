# 当子类和父类存在同名的成员函数时，通过某个子类的对象调用该函数，总是会调用相应子类的函数，该行为称为多态
class Animal(object):
    def talk(self):
        print("Animal talking")


class Cat(Animal):
    def talk(self):
        print("Cat talking")


class Bird(Animal):
    def talk(self):
        print("Bird talking")


def func(animal):
    animal.talk()


onecat = Cat()
onebird = Bird()

func(onecat)  # "Cat talking"
func(onebird)  # "Bird talking"


# name的调用顺序
class Animal(object):
    name = "Animal one"

    def __init__(self):
        self.name = "Animal two"


class Bird(Animal):
    name = "Bird one"

    def __init__(self):
        self.name = "Bird two"
        Animal.__init__(self)


birdone = Bird()
print(birdone.name)
