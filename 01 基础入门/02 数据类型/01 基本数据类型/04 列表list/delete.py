"""
列表的删除方法：
pop() -> value
pop(index) -> value

del list[index] -> index

remove(value) -> None
"""
lis = ["a", 2, 4.1, True, None, [1, 2, 3]]

# TODO pop不传参数，表示删除列表最后一个元素，返回删除的元素
ret = lis.pop()
print(ret)  # [1, 2, 3]
print(lis)  # ['a', 2, 4.1, True, None]

###########################################
lis = ["a", 2, 4.1, True, None, [1, 2, 3]]

# TODO pop接收参数则删除指定位置的列表元素，返回删除的元素，改变原列表
ret = lis.pop(1)
print(ret)  # 2
print(lis)  # ['a', 4.1, True, None, [1, 2, 3]]

###########################################
lis = ["a", 3, 4.1, True, None, [1, 2, 3]]

# TODO del 操作符 删除指定位置的列表元素
del lis[2]
print(lis)  # ['a', 3, True, None, [1, 2, 3]]

###########################################
lis = ["a", 2, 4.1, True, None, [1, 2, 3]]
# TODO 列表的remove方法，接收删除指定的列表元素，返回None，改变原列表
ret = lis.remove(4.1)
print(ret)  # None
print(lis)  # ['a', 2, True, None, [1, 2, 3]]
