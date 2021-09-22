# 帅选真值
data = [1, 'A', 0, False, True]

print([item for item in data if item])

print(list(filter(lambda x: bool(x) is True, data)))
print(list(filter(None, data)))