mylist = []

for item in range(11):
    mylist.append(item * item)

print(mylist)

print([item * item for item in range(11)])

# 将mylist中是字符串类型的成员的变成大写字母
mylist = ['Hello', "老鸟Python", 2, ["Ok"]]
print([item.upper() if isinstance(item, str) else item for item in mylist])

# 使用字典推导式打印9X9乘法口诀表

# 转置矩阵
'''
[[1,2,3],
 [4,5,6],     =>
 [7,8,9]]

[[1,4,7],
 [2,5,8],     
 [3,6,9]]
'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)
print([[matrix[row][col] for row in range(3)] for col in range(3)])

# 从列表推导式开始，当表达式变得复杂时再转为循环
ages = [23, 56, 12, 34, 51, 8, 34, 21, 18]
print([age for age in ages if age > 10 and age])
