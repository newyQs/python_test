# -*- coding:utf8 -*-
import os
from multiprocessing import Process, current_process


def doubler(number):
    result = number * 2
    # 获取子进程ID
    proc_id = os.getpid()
    # 获取子进程名称
    proc_name = current_process().name
    print('proc_id:{0} proc_name:{1} result:{2}'.format(proc_id, proc_name, result))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    p_list = list()
    # 父进程ID和名称
    print('parent_proc_id:{0} parent_proc_name:{1}'.format(os.getpid(), current_process().name))

    for num in numbers:
        # 创建子进程
        p = Process(target=doubler, args=(num,))
        p_list.append(p)
        # 启动子进程
        p.start()

    # join方法会让父进程等待子进程结束后再执行
    for p in p_list:
        p.join()

    print("Done.")
