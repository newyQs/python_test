from multiprocessing import Process
import os
import time


def func():
    print('子进程id:', os.getpid())  # getpid()
    print('所属父进程id:', os.getppid())  # getppid()
    print('子进程启动的函数！')
    time.sleep(3)
    print('子进程执行完毕！')


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    # p.join()  # 阻塞
    # 这种主进程执行结束，子进程还在执行的进程我们叫做僵尸进程
    # 使用p.join()方法可以强制主进程等待子进程执行完毕再结束主进程

    print('主进程执行的代码！')
    print('主进程id:', os.getpid())
    print('主进程执行完毕！')
