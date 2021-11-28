'''
https://blog.csdn.net/qq_40678222/article/details/83065192

集合：无序且元素唯一的容器。类似于字典，但只有键（key），没有值（value）。
1.集合中每个元素都是无序的，不重复的任意对象；
2.可以通过集合去判断数据的从属关系，可以做集合运算，可添加，删除元素；
3.通过add增加元素，通过remove删除元素；
4.集合运算：& | ;
'''

# set集合常用方法汇总：17个
'''
remove(element)
copy()
pop()
add(element)
update(s)
clear(s)

difference(s)
difference_update(s)
discard(element)

intersection(s)
intersection_update(s)
isdisjoint(s)
issubset(s)
issuperset(s)

symmetric_difference(s)
symmetric_difference_update(s)
union(s)

'''

# 创建：
s1 = {1, 3, 4}
s2 = set([1, 2, 3])

# set对象类的全部方法
'''
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', 
'__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', 
'__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
'__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 
'symmetric_difference_update', 'union', 'update']
'''
