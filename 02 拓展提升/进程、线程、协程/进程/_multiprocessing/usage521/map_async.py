"""
map_async提交一批任务异步执行
"""
from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool() as p:
        futures = p.map_async(f, range(1, 11))
        print(futures.get())

