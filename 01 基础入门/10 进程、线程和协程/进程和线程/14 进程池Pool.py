# -*- coding:utf-8 -*-
from multiprocessing import Process
from multiprocessing import Pool
import time
import os
import random


def smoke(num):
    t_start = time.time()  # 记录开始时间
    print("start %d smoke ！！！！ and pid = %d" % (num, os.getpid()))
    time.sleep(random.random() * 2)  # random.random随机生成0~1之间的浮点数
    t_stop = time.time()
    print("finish %d smoke, time = %0.2f" % (num, (t_start - t_stop)))


def main():
    # 创建进程池Pool
    po = Pool(3)  # 定义一个进程池，最大进程数为3

    # 编写一个循环，加入进程池中
    for i in range(0, 10):
        print("------循环 %d --------" % i)
        # Pool().apply_async(调用的目标函数，（传递的参数元组）)
        # 每次循环会用空闲出来的子进程去调用目标
        po.apply_async(smoke, (i,))

    print("----start-----")
    po.close()  # 关闭进程池
    po.join()  # 等待进程池所有子进程执行完毕，必须在close语句之后
    print("----end-----")


if __name__ == "__main__":
    main()
