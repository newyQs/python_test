"""
1.具有__iter__()方法的对象称为【可迭代对象】，该方法可获取其迭代器对象；
2.具有__iter__()和__next__()方法的对象称为【迭代器对象】，该方法能够自动返回下一个结果，当达到序列结尾，引发Stopiteration异常

+ 可迭代对象本身不一定是迭代器，但可以通过其 __iter__() 方法得到对应的迭代器对象；
+ 定义可迭代对象，必须实现 __iter__() 方法，定义迭代器，必须实现 __iter__() 和 __next__() 方法；
+ 对于可迭代对象，可以使用 iter( ) 函数得到其对应的迭代器对象，使用 next( ) 函数获取该迭代器对象当前返回的元素；
+ 可以将迭代器简单理解为“内置了 for 循环的可迭代对象”，每使用 next( ) 函数访问一次迭代器对象，
  其在返回当前元素的同时，内部指针将指向下一个元素;
+ iter( ) 函数与 __iter__() 方法联系非常紧密，iter()是直接调用该对象的 __iter__() 方法，
  并将其返回结果作为自己的返回值，next( ) 函数则是调用该对象的 __next__() 方法获取当前元素;

"""
# 生成器定义
mygen = (item for item in range(10))

print(mygen)
# 如何输出每一个元素
# 调用__next__函数或next函数（实际该函数简介调用生成器的__next__函数）
print(mygen.__next__())
print(next(mygen))
print(mygen.__next__())


# 生成器保存的是算法，每次调用 __next__ 函数 就计算出下一个元素的值，
# 直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的错误。
# 通常情况下使用for循环遍历

# 让函数变成生成器
def ge_even():
    data = 1
    while True:
        if data % 2 == 0:
            yield data
        data += 1


even = ge_even()
print(type(even))  # even 是个生成器


# 调用
def ge_func():
    yield 1
    yield 2
    yield 3


myge = ge_func()
print(myge.__next__())
print(myge.__next__())
print(myge.__next__())

myge = ge_func()
for item in myge:
    print(item)


# 为什么第一种调用和后两种调用的结果不一致
def ge_func():
    yield 1
    yield 2
    yield 3


# 第一种调用
print(ge_func().__next__())
print(ge_func().__next__())
print(ge_func().__next__())

# 第二种调用
myge = ge_func()
for item in myge:
    print(item)

# 第三种调用
for item in ge_func():
    print(item)

# 可迭代对象，迭代器，生成器的层级关系:
# Iterable < Iteration < Generation (包含关系)

