# 筛选真值
data = [1, 'A', 0, False, True]

# 使用推导式
print([item for item in data if item])

# 使用filter
# filter(function or None, iterable) --> filter object
print(list(filter(lambda x: bool(x) is True, data)))
print(list(filter(None, data)))
