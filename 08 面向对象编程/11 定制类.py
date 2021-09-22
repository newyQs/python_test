# 1.使用 __len__ 函数
mylist = ["hello", 1, (3, 4), {"a": 1, "b": 2}]

# print(len(mylist))  # 实际调用的是 mylist.__len__() 函数
# print(mylist.__len__())

# 1.1使用__len__函数定制类
# len()函数其实调用的是内部的__len__()方法
# 返回什么有我们自己决定，但必须是int类型。
# class MyObject(object):
#     def __init__(self, *data):
#         self.__data = data
#
#     def __len__(self):
#         # return len(self.__data)
#         return 250  # 必须为int类型，否则报异常
#
#
# myobject = MyObject(4, "hello", [2, 3])
# print(len(myobject))


# 2.使用 __str__ 函数
# print()函数调用的就是类的__str__()方法
# class MyObject(object):
#     def __init__(self, *data):
#         self.__data = data
#
#     def __str__(self):
#         return "I'm MyObject 照片"
#
#
# myobject = MyObject(4, "hello", [2, 3])
# print(myobject)


# 2.1 也可以返回传入的内容
# class MyObject(object):
#     def __init__(self, *data):
#         self.__data = data
#
#     def __str__(self):
#         return str(self.__data)  # 但返回值必须是str或unicode类型
#
#
# myobject = MyObject(4, "hello", [2, 3])
# print(myobject)
# print(type(myobject))  # <class '__main__.MyObject'>
# print(type(MyObject))  # <class 'type'>

# 2.2 Python 还提供一个 __unicode__ 函数，在 Python2 中该函数用于返回中文，而 __str__ 函数用于返回 ASCII。
# 然而，在 Python3 中， __str__ 即可以返回中文也可以返回 ASCII，而 __unicode__ 函数，我们并不需要使用

# 3.使用 __repr__ 函数
# 调试控制台下调用
'''
...class MyObject(object):
...    def __init__(self, *data):
...        self.__data = data
...
...    def __repr__(self):
...        return "I'm MyObject"
...
>>> myobject = MyObject(4, "hello", [2, 3])
>>> myobject
I'm MyObject   # 控制台输出
'''


#  4.使用 __iter__ 函数
# for...in循环遍历可迭代对象（如str,tuple,dict,set）的本质，实际上for...in循环只能遍历迭代器
# 实际上 for...in... 在第一次遍历这些内置容器时，会先调用 Python 内置的 iter 函数，
# 该 iter 函数会自动调用这些内置容器类内部的 __iter__ 函数，
# 这些内置容器类内部的 __iter__ 函数返回一个迭代器（迭代对象），
# 然后 Python 的 for 循环就会不断的调用该迭代器的 __next__ 函数拿到循环的下一个值，
# 直到遇到 StopIteration 异常时退出循环
# 同样我们也可以在自己定义的类中重写 __iter__ 函数，让该函数返回一个迭代器，以便支持 Python 的 for 循环
# class MyObject(object):
#     def __init__(self, *data):
#         self.__data = data
#
#     def __iter__(self):
#         return iter(self.__data)  # 返回一个迭代器（返回的是元组对象转换的迭代器）
#
#
# myobject = MyObject(4, "hello", [2, 3])
#
# for item in myobject:
#     print(item)


# 5.使用 __getitem__ 函数
# 调用__getitem__方法可以像序列一样通过索引取值
# class MyObject(object):
#     def __init__(self, *data):
#         self.__data = data
#
#     def __getitem__(self, index):
#         return self.__data[index]
#
#
# myobject = MyObject(4, "hello", [2, 3])
# print(myobject[1])


# 6.使用 __getattr__ 函数
# 通常情况下，当我们调用类的属性不存在时就会抛出异常，
# 但如果我们重写了 __getattr__ 函数解释器则会调用 __getattr__ 函数来处理不存在的属性
# class Human(object):
#     def __init__(self):
#         self.age = 18
#
#     def __getattr__(self, attr):
#         return attr + "属性不存在"
#
#
# ruhua = Human()
# print(ruhua.age)
# print(ruhua.name)

# 6.1 同样如果我们调用的类的方法不存在时，解释器则会调用 __getattr__ 函数来处理不存在的方法，
# 但要注意该函数要返回一个函数
# def myfunc():
#     print("该函数不存在")
#
#
# class Human(object):
#     def __init__(self):
#         self.age = 18
#
#     def __getattr__(self, attr):
#         return myfunc
#
#
# ruhua = Human()
# ruhua.talk()

# 6.2 __getattr__ 函数的第二个形参接收的是不存在的属性或方法名字，我们可以自己灵活的处理我们想处理的不存在的属性或方法
# def myfunc():
#     print("你瞅啥")
#
#
# class Human(object):
#     def __init__(self):
#         self.age = 18
#
#     def __getattr__(self, attr):
#         if attr == "gender":
#             return 'female'
#         if attr == "talk":
#             return myfunc
#
#
# ruhua = Human()
# print(ruhua.age)
# print(ruhua.gender)
# ruhua.talk()

# 7 使用 __call__ 函数
# 类的对象可以有自己的属性和方法，当我们调用对象的函数时，我们用对象加上点加上函数名来调用，
# 如果我们直接通过在对象的后面加上括号调用，则是调用类的 __call__ 函数，
# 这样一来，对象看起来像个函数，我们称之为仿函数或者函数对象
# class MyObject(object):
#     def __init__(self):
#         pass
#
#     def __call__(self, arg):
#         print(arg)
#
#
# myobject = MyObject()
# myobject("hello")


# 7.1 函数对象和函数之间没有本质区别，函数对象其实就是函数，
# Python 的 callable 函数可以判断一个变量是否是函数，是则返回True反之返回False
# class MyObject(object):
#     def __init__(self):
#         pass
#
#     def __call__(self, arg):
#         pass
#
#
# myobject = MyObject()
# print(callable(myobject)) # True


# 8.实现一个迭代器类
class IterClass(object):
    def __init__(self, *data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            self.index += 1
            return self.data[self.index - 1]


iterClass = IterClass(*[1, 'a', 3, 'b', [1, 3], (1, 4)])
for item in iterClass:
    print(item)
