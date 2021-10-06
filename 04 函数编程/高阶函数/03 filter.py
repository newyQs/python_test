# 假值：0 '' [] {} None False 0.0

# 筛选真值
data = [123, 'A', '', [], 0.0, {}, None, 0, False, True]

# 使用推导式
print([item for item in data if item])

# 使用filter
# filter(function or None, iterable) --> filter object
print(list(filter(lambda x: bool(x) is True, data)))
print(list(filter(None, data)))

print(list(map(lambda x: bool(x) is True, data)))
print(any(map(lambda x: bool(x) is True, data)))
