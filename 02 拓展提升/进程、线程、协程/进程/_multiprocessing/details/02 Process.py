# -*- coding:utf8 -*-
import os
from multiprocessing import Process, current_process


class MyProcess(Process):
    def __init__(self, number):
        # 必须调用父类的init方法
        super(MyProcess, self).__init__()
        self.number = number

    def run(self):
        result = self.number * 2
        # 获取子进程ID
        # self.pid
        proc_id = os.getpid()
        # 获取子进程名称
        # self.name
        proc_name = current_process().name
        print('proc_id:{0} proc_name:{1} result:{2}'.format(proc_id, proc_name, result))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    p_list = []
    # 父进程的ID和名称
    print('parent_proc_id:{0} parent_proc_name:{1}'.format(os.getpid(), current_process().name))

    for num in numbers:
        # 创建子进程
        p = MyProcess(num)
        p_list.append(p)
        # 启动子进程，启动一个新进程实际就是执行本进程对应的run方法
        p.start()

    # join方法会让父进程等待子进程结束后再执行
    for p in p_list:
        p.join()

    print("Done.")
