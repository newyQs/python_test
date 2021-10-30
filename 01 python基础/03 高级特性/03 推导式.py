
# 一般方法
mylist = []
for item in range(11):
    mylist.append(item * item)
print(mylist)

# 使用列表推导式
print([item * item for item in range(11)])

# 将mylist中是字符串类型的成员变成大写
mylist = ['Hello', "老鸟Python", 2, ('nihao',), True, ["ok"]]
print([item.upper() if isinstance(item, str) else item for item in mylist])

# 思考：如何将成员里的所有成员都进行转换呢？


# 使用推导式打印9X9乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end='\t')
    print()

print('\n'.join(
    ['\t'.join([f'{j}*{i}={i * j}' for j in range(1, i + 1)]) for i in range(1, 10)]))

# 转置矩阵
'''
[[1,2,3],          [[1,4,7], 
 [4,5,6],     =>    [2,5,8],
 [7,8,9]]           [3,6,9]]
'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)
print([[matrix[row][col] for row in range(3)] for col in range(3)])

# 从列表推导式开始，当表达式变得复杂时再转为循环
ages = [23, 56, 12, 34, 51, 8, 34, 21, 18]
print([age for age in ages if age > 10 and age])
