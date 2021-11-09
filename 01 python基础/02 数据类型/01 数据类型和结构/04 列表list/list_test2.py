lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

ret = lis.append(12)

print(ret)  # None
print(lis)

###########################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

ret = lis.insert(1, "b")

print(ret)  # None
print(lis)

###########################################
lis = ["a", 2, 4.1, True, [1, 2, 3], None, ("b", "c")]

ret = lis.extend([1, 2])

print(ret)  # None
print(lis)
