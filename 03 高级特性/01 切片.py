# sequence[start,end,step]

# 正向切片：step>=1 default=1 integer
# 从左至右，含头不含尾
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist[1:9])
print(mylist[1:])
print(mylist[:9])

print(mylist[1:-1])

print(mylist[1:100])

print(mylist[6:3])  # []

print(mylist[1:10:2])

# 逆向切片：step <= -1 integer
# 从右至左，含头不含尾
print(mylist[1:9:-1])

print(mylist[9:1:-1])

# 关于切片的一些问题
# 1.如果切片截取的范围不存在，则返回一个空集，如[]
# 2.如果切片的索引越界，则截取到越界前的最后一个成员
# 3.切片并不改变集合本身的值
# 4.切片步长为正时，从左往右截取，默认为1；切片为负时，从右往左截取

# 问题
strone = "Hello"
strthree = "Hell"
strtwo = strone[:4]  # "Hell"
strfour = strone[:]  # "Hello"

print(strtwo)
print(strthree)
print(id(strtwo))
print(id(strthree))

print(strone)
print(strfour)
print(id(strone))
print(id(strfour))

print(id(strone[1]))
print(id(strtwo[1]))
print(id(strthree[1]))
print(id(strfour[1]))
