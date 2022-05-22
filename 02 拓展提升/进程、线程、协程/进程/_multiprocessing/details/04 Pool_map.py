# -*- coding:utf8 -*-
import os
from multiprocessing import Pool, current_process


def doubler(number):
    result = number * 2
    proc_id = os.getpid()
    proc_name = current_process().name
    print('proc_id:{0} proc_name:{1} result:{2}'.format(proc_id, proc_name, result))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    pool = Pool(processes=3)
    pool.map(doubler, numbers)

    # 关闭pool使其不再接受新的任务
    pool.close()

    # 关闭pool，结束工作进程，不在处理未完成的任务
    # pool.terminate()

    # 主进程阻塞，结束工作进程，不再处理未完成的任务，join方法要在close或terminate之后使用
    pool.join()

    print('Done')
