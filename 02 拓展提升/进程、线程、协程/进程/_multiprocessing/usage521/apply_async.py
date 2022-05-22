"""
apply_async提交一个任务异步执行
"""
from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool() as p:
        futures = [p.apply_async(f, (i,)) for i in range(1, 1001)]
        res = [future.get() for future in futures]
        print("结果：", sum(res))
