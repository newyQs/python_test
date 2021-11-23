class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性外部无法直接访问
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s say : i am %d." % (self.name, self.age))


p = People('Python', 10, 20)
p.speak()
# __weight无法直接访问
print(p.name, '--', p.age)  # ,'--',p.__weight)


# 单继承:
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


class Speak:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    # 普通方法，对象调用
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))

    # 私有方法，self调用
    def __song(self):
        print('唱一首歌自己听', self)

    # 静态方法，对象和类调用，不能和其他方法重名，不然会相互覆盖，后面定义的会覆盖前面的
    @staticmethod
    def song():
        print('唱一首歌给类听:静态方法')

    # 普通方法，对象调用
    def song(self):
        print('唱一首歌给你们听', self)

    # 类方法，对象和类调用，不能和其他方法重名，不然会相互覆盖，后面定义的会覆盖前面的
    @classmethod
    def song(self):
        print('唱一首歌给类听:类方法', self)


# 多继承：
class Sample(Speak, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speak.__init__(self, n, t)


test = Sample('Song', 24, 56, 7, 'Python')
test.speak()
test.song()
Sample.song()
Sample.song()
test.song()

# testAPI.__song() 无法访问私有方法
