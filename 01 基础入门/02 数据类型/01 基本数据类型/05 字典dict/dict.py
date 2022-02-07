"""
字典{key:value}：哈希表，关联数组。由多个键值对组合。
1.字典中的数据必须以键值对形式出现；
2.键不可重复，值可重复，若键重复则只记住最后一个值；
3.键（key）必须是可hash的，即不可变对象，不能进行修改，而值可以修改，也可以是任意对象；
"""

# 字典常用方法汇总：11个
'''
copy()
clear()

fromkeys(seq)

get(key) 

pop(key)
popitem()

update(__m,kwargs)

keys()          迭代的是key
values()        迭代的是value
items()         迭代（key,value）

setdefault(key,default)
'''

# 创建
d1 = {'name': 'lee', 'age': 18, 'city': 'chaohu'}
d2 = dict(((1, 2), (3, 4)))

dd = {'name': 'lee', 'age': 18, 'city': 'chaohu'}
# 查询
print(dd['name'])
# print(dd['sex']) # KeyError: 'sex'
print(dd.get('sex'))  # key不存在返回None

# 增加
dd['sex'] = 'male'
print(dd)

dd.update({'sex': 'female'})  # 覆盖
print(dd)
dd.update({'gender': 'male'})
print(dd)

# 修改
dd['sex'] = 'male'
print(dd)

# 删除
dd.pop('sex')  # 指定键删除
print(dd)

dd.popitem()  # 删除最后一个
print(dd)

# 循环迭代：dict.keys()  dict.values()  dict.items()
for i in dd:
    print(i)

for i in dd.keys():
    print(i)

for i in dd.values():
    print(i)

for i in dd.items():
    print(i)

# 复制
d_co = dd.copy()

# 清空
dd.clear()

# setdefault()
dd.setdefault('ss', 'this is a 04 first')
print(dd['ss'])
print(dd.get('ss'))

# fromkeys()
key = ['a', 'b', 'c']
value = [1, 2, 3]
d = dict.fromkeys(key, value)
print(d)

# 列举dict全部方法
'''
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 
'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''
