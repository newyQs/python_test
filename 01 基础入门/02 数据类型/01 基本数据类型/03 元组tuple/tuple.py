"""
元组：固定长度、不可变的python对象序列
1.一种固定的列表，一旦初始化，其中的元素都不可修改；
2.元组内部元素的可变性，注意可变对象和不可变对象；
3.空元组记为()，只有一个元素的元组记为(ele,)，不可为(ele)，()是数学中小括号；
"""

# 元组常用方法汇总：2个
'''
index(object,start,stop) =>返回元素第一次出现的位置
count(object)            =>统计元素出现的次数
'''

# 1.创建元祖
t1 = (1, 2, 3)
t2 = ('abc',)

t3 = tuple(['lee', 2])
t4 = tuple([2])

print(t1, t2, t3, t4, end=' ')
print()

# 2.获取元组元素：有序集合通过索引获取
print(t1[1])

e = ('a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'f', 'd')
# 3.统计元组中指定元素出现的次数
print(e.count('f'))

# 4.获取元组中指定元素第一次出现的位置（索引）
print(e.index('d'))  # 元素不存在则报错

# 5.有序序列支持切片操作
ts = e[2:8]
print(ts)
print(ts[:])

# 6.获取元组长度:实际len()调用的是对象类内部的__len__()方法
print(len(e))
print(e.__len__())

# tuple对象类所有方法
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
'''
# print('----')
# print(tt.__add__((12, 3)))
# print(tt.__class__)
# print(tt.__contains__(12))
# print(tt.__getitem__(1))
