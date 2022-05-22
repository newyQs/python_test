"""
map提交一批任务同步执行
"""
from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool() as p:
        res = p.map(f, range(1, 10))
        print("结果：", sum(res))
