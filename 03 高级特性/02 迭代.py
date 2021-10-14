from collections.abc import Iterable, Iterator

# 无论是有序集合(str,list,tuple),还是无序集合(dict,set)，我们都可以使用for循环来遍历它，这种遍历叫迭代。
mystr = "hello, how are you"
mylist = [1, 2, 3, 4, 5]
mytuple = (1, 2, 3, 4, 5)

mydict = {'name': 'jack', 'age': 18}
myset = {'name', 'age', 19}

# 有序集合的迭代
for i in mystr:
    print(i, end='\t')
print()
for i in mylist:
    print(i, end='\t')
print()
for i in mytuple:
    print(i, end='\t')
print()
for i in mydict:
    print(i, end='\t')
print()
for i in mytuple:
    print(i, end='\t')
print()

# 字典的迭代
for key in mydict.keys():
    print(key, end='\t')
print()
for value in mydict.values():
    print(value, end='\t')
print()
for items in mydict.items():
    print(items, end='\t')
print()

# python的数据类型
myint = 2
myfloat = 2.2
mybool = True
mynone = None
mystr = "hello"
mylist = [1, 2, 3]
mytuple = (1, 2, 3)
myset = set([1, 2, 3])
mydict = {"a": 1, "b": 2, "c": 3}


def myfunc():
    pass


class Huamn:
    pass


# 判断类型:type()
print(type(myint))
print(type(myfloat))
print(type(mybool))
print(type(mynone))
print(type(mystr))
print(type(mylist))
print(type(mytuple))
print(type(myset))
print(type(mydict))

# 判断是否是可迭代对象:Iterable
print(isinstance(myint, Iterable))  # False
print(isinstance(myfloat, Iterable))  # False
print(isinstance(mybool, Iterable))  # False
print(isinstance(mynone, Iterable))  # False

print(isinstance(mystr, Iterable))  # True
print(isinstance(mylist, Iterable))  # True
print(isinstance(mytuple, Iterable))  # True
print(isinstance(myset, Iterable))  # True
print(isinstance(mydict, Iterable))  # True

# 判断是否是迭代器:Iteration


# 判断是够是生成器:Generation


# 使用enumerate
mylist = [1, 2, 3]
mydict = {"a": 1, "b": 2, "c": 3}

for index, item in enumerate(mylist):
    print(index, item)

for index, item in enumerate(mydict):
    print(index, item)
