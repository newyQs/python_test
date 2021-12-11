"""

"""
from multiprocessing import Pool
import time
import os


def action(name='http://c.biancheng.net'):
    print(name, ' --当前进程：', os.getpid())
    time.sleep(3)


if __name__ == '__main__':
    # 创建包含 4 条进程的进程池
    pool = Pool(processes=4)
    # 将action分3次提交给进程池
    pool.apply_async(action)
    pool.apply_async(action, args=('http://c.biancheng.net/python/',))
    pool.apply_async(action, args=('http://c.biancheng.net/java/',))
    pool.apply_async(action, kwds={'name': 'http://c.biancheng.net/shell/'})
    pool.close()
    pool.join()
