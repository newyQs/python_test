'''
列表：长度可变，内部元素可变
1.列表中的每个元素都是可变的，意味着可以对每个元素进行修改和删除；
2.列表是有序的，每个元素的位置都是确定的，可以用索引去访问每个元素；
3.列表中的元素可以是python中的任何对象;
'''
# 支持正向索引和反向索引：同一个元素，正向索引和反向索引的绝对值之和是列表的长度
#       0  1  2  3  4  5  6  7  8
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#       -9 -8 -7 -6 -5 -4 -3 -2 -1


# 列表常用方法汇总：11个
'''
sort(key,reverse)          =>返回None                    ==>修改原列表
remove(object)             =>返回None                    ==>修改原列表
pop(index)                 ==返回删除的元素              ==>修改原列表
extend(iterable)           =>返回None                    ==>修改原列表
insert(index,object)       =>返回None                    ==>修改原列表
append(object)             =>返回None                    ==>修改原列表
clear()                    =>返回None                    ==>修改原列表
reverse()                  =>返回None                    ==>修改原列表

index(object,start,stop)   =>返回元素第一次出现的位置     ==>不修改原列表
count(object)              =>统计元素出现的次数           ==>不修改原列表
copy()                     =>返回拷贝的列表               ==>不修改原列表
'''

# 创建
L1 = [1, 3, 4]

L2 = list((2, 4, 5))
L3 = list(range(10))

print(L1, L2, L3, end=' ')
print()

# 常见操作：

# 增加
# append(obj)/insert(index,obj)/extend(iter)
mylist01 = [1, 2, 3, 4]

mylist01.append('append')
mylist01.insert(1, 'insert')
mylist01.extend(['ext1'])

print(mylist01)

# 删除
# del /pop([index])/remove(obj)
mylist02 = ['data1', 'data12', 'data3', 'data4', 'data5']

del mylist02[1]
print(mylist02)

mylist02.pop()  # 尾部删除
print(mylist02)

mylist02.pop(1)  # 删除不存在索引会报错
print(mylist02)

mylist02.remove('data1')  # 删除不存在的会报错

# 修改
mylist03 = [1, 2, 3, 4, 5]
mylist03[1] = 'modify'
print(mylist03)

# 查询
mylist = ['jack', 'lucy', 'lee']
print(mylist[0])
# print(mylist[12]) IndexError: list index out of range

# 清空
# clear()

# 获取第一次出现的索引。可指定索引范围
# index(obj,start,end)

# 浅复制
# copy()

# 反转
# reverse()

# 排序
# sort(key=func,reverse=bool)


# 方法
print(dir(list))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
