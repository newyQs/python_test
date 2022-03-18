"""
列表的其他方法：

排序：
sort()

索引：
index()

计数：
count()

翻转：
reverse()
"""
lis = [4, 67, 24, 56, 7, 8]

ret = lis.sort()
print(ret)
print(lis)

##############################################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

ret = lis.index(None)
print(ret)
print(lis)

##############################################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

ret = lis.count(2)
print(ret)
print(lis)

##############################################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

ret = lis.reverse()
print(ret)
print(lis)

##############################################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

ret = lis.copy()

print(ret)
print(lis)

##############################################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

ret = lis.clear()

print(ret)
print(lis)
