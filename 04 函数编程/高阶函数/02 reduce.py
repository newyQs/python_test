from functools import reduce
import math

# reduce(function, sequence[, initial]) -> value
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 计算累加：1+2+3+...+100 == 5050
print(reduce(lambda x, y: x + y, range(1, 101)))

# 计算累乘：1*2*3*4*5 == 5！
print(reduce(lambda x, y: x * y, range(1, 6)))

# 将列表[1,3,5,7,9]变成整数123579
print(reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9]))


# 筛选素数：
def prime(n):
    """
    只能被1和自身整除的数称为素数，又称为质数
    """
    prime_list = []  # 放素数的容器
    for i in range(2, n + 1):
        for v in range(2, i):
            if i % v == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


prime_list = prime(100)
print(prime_list)
print(len(prime_list))

# 一行解决的
print(list(filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0], range(2, 101))))
print(" ".join("%s" % x for x in range(2, 101) if not [y for y in range(2, x) if x % y == 0]))
