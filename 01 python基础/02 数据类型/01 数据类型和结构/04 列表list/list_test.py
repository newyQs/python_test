lis = ["a", 2, 4.1, True, None, [1, 2, 3]]

ret = lis.pop()

print(ret)
print(lis)

###########################################
lis = ["a", 2, 4.1, True, None, [1, 2, 3]]

ret = lis.pop(1)

print(ret)
print(lis)

###########################################
lis = ["a", 2, 4.1, True, None, [1, 2, 3]]

del lis[2]

print(lis)

###########################################
lis = ["a", 2, 4.1, True, None, [1, 2, 3]]

ret = lis.remove(1)

print(ret)
print(lis)
