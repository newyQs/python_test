'''
元组：固定长度、不可变的python对象序列
1.一种固定的列表，一旦初始化，其中的元素都不可修改；
2.元组内部元素的可变性，注意可变对象和不可变对象；
3.空元组记为()，只有一个元素的元组记为(ele,)，不可为(ele)，()是数学中小括号；
'''

# 元组常用方法汇总：2个
'''
index(object,start,stop) =>返回元素第一次出现的位置
count(object)            =>统计元素出现的次数
'''

# 创建
t1 = (1, 2, 3)
t2 = ('abc',)

t3 = tuple(['lee', 2])
t4 = tuple([2])

print(t1, t2, t3, t4, end=' ')
print()

# 获取元组元素
print(t1[1])

# 常见操作：

tt = (1, 3, 2, 5, 5, 6, 2, 5, 6, 7, 2, 2, 4, 8)
# 1.统计元组中指定元素出现的次数
print(tt.count(2))

# 2.获取元组中指定元素第一次出现的位置（索引）
print(tt.index(2))
# print(tt.index(12)) 元素不存在则会报错

# 切片操作
ts = tt[2:8]
print(ts)

print(ts[:])

# 获取元组长度
print(len(tt))
print(tt.__len__())

# tuple对象所有方法
print(dir(tuple))
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
