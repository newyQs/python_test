from functools import reduce

# reduce(function, sequence[, initial]) -> value
# 计算累加：1+2+3+...+100
print(reduce(lambda x, y: x + y, range(1, 101)))

# 计算累乘：1*2*3*4*5 == 5！
print(reduce(lambda x, y: x * y, range(1, 6)))
