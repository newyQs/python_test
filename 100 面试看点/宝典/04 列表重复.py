"""

"""
# 01 给定两个列表，如何找出相同元素和不同元素？
list1 = [2, 3, 4, 11, 13, 24, 12]
list2 = [3, 4, 12, 2, 14, 6, 9]

set1 = set(list1)
set2 = set(list2)
print(set1 & set2)  # 找相同
print(set1 ^ set2)  # 找不同

# 02 删除列表中重复的元素
# 使用内置的set去重
e1 = [1, 2, 3, 4, 5, 2, 4, 3, 2]
es1 = list(set(e1))
print(es1)

# 如果想要维持原来的排序，使用sort方法
L1 = [12, 3, 4, 2, 3, 4, 5]
L2 = list(set(L1))
L2.sort(key=L1.index)
print(L2)

# 也可以这样写
mylist1 = [2, 3, 3, 1, 4, 2]
mylist2 = sorted(set(mylist1), key=mylist1.index)
print(mylist2)

# 也可以用遍历
lis1 = [11, 12, 2, 3, 3]
lis2 = []
for item in lis1:
    if item not in lis2:
        lis2.append(item)

print(lis2)

# 03 公差11的列表生成式
print([d * 11 for d in range(10)])
