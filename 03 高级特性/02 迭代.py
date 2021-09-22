from collections.abc import Iterable, Iterator

# 无论是有序集合(str,list,tuple),还是无序集合(dict,set)
# 我们都可以使用for循环来遍历它，这种遍历叫迭代

mystr = "hello nihao"
mylist = [1, 2, 3, 4, 5]
mytuple = (1, 2, 3, 4, 5)

mydict = {'name': 'jack', 'age': 18}
myset = {'name', 'ahe', 19}

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

# Iterable
# 可迭代对象
myint = 2
myfloat = 2.2
mybool = True
mynone = None
mystr = "hello"
mylist = [1, 2, 3]
mytuple = (1, 2, 3)
myset = set([1, 2, 3])
mydict = {"a": 1, "b": 2, "c": 3}

print(isinstance(myint, Iterable))  # False
print(isinstance(myfloat, Iterable))  # False
print(isinstance(mybool, Iterable))  # False
print(isinstance(mynone, Iterable))  # False
print(isinstance(mystr, Iterable))  # True
print(isinstance(mylist, Iterable))  # True
print(isinstance(mytuple, Iterable))  # True
print(isinstance(myset, Iterable))  # True
print(isinstance(mydict, Iterable))  # True

# 使用enumerate
mylist = [1, 2, 3]
mydict = {"a": 1, "b": 2, "c": 3}

for index, item in enumerate(mylist):
    print(index, item)

for index, item in enumerate(mydict):
    print(index, item)
