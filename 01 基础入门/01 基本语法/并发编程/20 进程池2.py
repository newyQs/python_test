"""
我们可以使用 with 语句来管理进程池，这意味着我们无需手动调用 close() 方法关闭进程池
"""
from multiprocessing import Pool
import time
import os


def action(name='http://c.biancheng.net'):
    time.sleep(3)
    return name + ' --当前进程：%d' % os.getpid()


if __name__ == '__main__':
    # 创建包含 4 条进程的进程池
    with Pool(processes=4) as pool:
        adds = pool.map(action, (
            'http://c.biancheng.net/python/',
            'http://c.biancheng.net/java/',
            'http://c.biancheng.net/Shell/'
        ))
    for arc in adds:
        print(arc)
