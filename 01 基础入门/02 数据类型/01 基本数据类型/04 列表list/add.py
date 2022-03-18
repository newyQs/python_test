"""
列表的增加方法：
append(value) -> None

insert(index, value) -> None

extend(iter) -> None
"""
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

# TODO append接收增加的元素，返回None，改变原列表
ret = lis.append(12)
print(ret)  # None
print(lis)

###########################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

# TODO index()指定位置插入元素，返回None，改变原列表
ret = lis.insert(1, "b")
print(ret)  # None
print(lis)

###########################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

# TODO extend 扩展列表，返回None，改变原列表
ret = lis.extend([1, 2])
print(ret)  # None
print(lis)
