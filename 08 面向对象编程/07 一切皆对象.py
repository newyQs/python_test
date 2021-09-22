# 1.isinstance函数可以判断一个东西的本质
# 一切皆对象
def func():
    pass


class Test:
    pass


print(isinstance(1, object))
print(isinstance(1.1, object))
print(isinstance("hello", object))
print(isinstance(False, object))
print(isinstance([1], object))
print(isinstance((1,), object))
print(isinstance({1: 1}, object))
print(isinstance(set([1]), object))
print(isinstance(None, object))
print(isinstance(Test(), object))

print(isinstance(int, object))
print(isinstance(float, object))
print(isinstance(str, object))
print(isinstance(bool, object))
print(isinstance(list, object))
print(isinstance(tuple, object))
print(isinstance(dict, object))
print(isinstance(set, object))
print(isinstance(type(None), object))
print(isinstance(Test, object))
print(isinstance(func, object))


# 2.type函数可以判断具体属于什么类型
def func():
    pass


class Test:
    pass


class Myobject(object):
    pass


# 值
print(type(1))
print(type(1.1))
print(type("hello"))
print(type(False))
print(type([1]))
print(type((1,)))
print(type({1: 1}))
print(type(set([1])))
print(type(None))
print(type(Myobject()))

# 类型
print(type(int))
print(type(float))
print(type(str))
print(type(bool))
print(type(list))
print(type(tuple))
print(type(dict))
print(type(set))
print(type(type(None)))
print(type(Myobject))
print(type(func))
