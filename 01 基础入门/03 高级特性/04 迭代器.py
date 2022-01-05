"""
+ 迭代是指通过 for 循环遍历集合中每一个成员的过程，Python 的 for 语句可以遍历任何可迭代的对象，
+ 在 Python 中，list，tuple，str，set，dict等类型的对象都是可以迭代的,
+ 迭代器是一种可以被遍历的对象，并且能作用于 Python 内置的 next 函数，迭代器对象从集合的第一个元素开始访问，
+ 直到所有的元素被访问完结束，迭代器只能往后遍历不能回溯，迭代器必须实现两个基本的函数:__iter__()和 __next__()

1. python的int，float，bool，NoneType类型都是不可迭代对象，更不是迭代器；
2. python的str，list，dict，set都是可迭代对象，但不是迭代器,可通过iter()函数将其转为迭代器；
3. 迭代器的充分必要条件是：含有 __iter__()方法和__next__()方法；
4. 生成器一定是迭代器，但迭代器未必是生成器，即迭代器包含生成器；
"""
from collections.abc import Iterator

mystr = "hello"
mylist = [1, 2, 3]
mytuple = (1, 2, 3)
myset = set([1, 2, 3])
mydict = {"a": 1, "b": 2, "c": 3}

print(isinstance(mystr, Iterator))  # False
print(isinstance(mylist, Iterator))  # False
print(isinstance(mytuple, Iterator))  # False
print(isinstance(myset, Iterator))  # False
print(isinstance(mydict, Iterator))  # False

# 可以用 iter 函数把一个可迭代对象作为参数，创建一个迭代器
it_mystr = iter("hello")
it_mylist = iter([1, 2, 3])
it_mytuple = iter((1, 2, 3))
it_myset = iter(set([1, 2, 3]))
it_mydict = iter({"a": 1, "b": 2, "c": 3})

print(isinstance(it_mystr, Iterator))  # True
print(isinstance(it_mylist, Iterator))  # True
print(isinstance(it_mytuple, Iterator))  # True
print(isinstance(it_myset, Iterator))  # True
print(isinstance(it_mydict, Iterator))  # True

# Python 的 for 循环本质上就是在遍历对象时，会先调用 iter 函数把这些对象转为迭代器，
# 然后遍历，遍历就是通过不断调用迭代器的 __next__ 函数实现的
mylist = [1, 2, 3]
for item in mylist:  # 解释器第一次看到 for...in 语句时，会先调用 iter 函数用 mylist 生成一个迭代器
    print(item)

# Python 解释器把上面 for ... in 语句转为下面代码
it_mylist = iter(mylist)  # 第一次 for...in 时先利用可迭代对象 mylist 生成一个迭代器
item = it_mylist.__next__()  # 第一次 for...in 时
print(item)

item = it_mylist.__next__()  # 第二次 for...in 时
print(item)

item = it_mylist.__next__()  # 第三次 for...in 时
print(item)

# for 循环遍历对象时，会首先调用 iter 函数把对象变为迭代器，如果遍历的对象是不可迭代的，则在 iter 函数转换时抛出异常
data = 5
for item in data:
    print(item)

# Python 解释器首先把上面 for ... in 语句转为下面代码，因为 data 是不可迭代对象，所以在转化成迭代器时报异常
data = iter(data)  # TypeError: 'int' object is not iterable
