'''
需求：
　　计算出斐波那契数列中第n个数的值？
　　求一个共有10个台阶的楼梯，从下走到上面，一次只能迈出1~3个台阶，并且不能后退，有多少中方法？
'''


def jian_zhi(func):
    # 中间字典，判断已经是否求解过
    median = {}

    def wrapper(*args):
        # 假如不在中间字典中，说明没有求解过，添加到字典中去，在的话，直接返回, 将不在递归下去，保证每次递归的唯一性
        if args not in median:
            median[args] = func(*args)
        return median[args]

    return wrapper


@jian_zhi
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@jian_zhi
def climb(n, steps):
    count = 0
    # 当最后台阶为0的时候，说明最后只是走了一次
    if n == 0:
        count = 1
    # 当最后台阶不为0的时候，说明还需要走至少一次
    elif n > 0:
        # 对三种情况进行分别处理momo
        for step in steps:
            count += climb(n - step, steps)

    # 返回每次递归的计数
    return count


if __name__ == '__main__':
    print(climb(10, (1, 2, 3)))
    print(fibonacci(20))
