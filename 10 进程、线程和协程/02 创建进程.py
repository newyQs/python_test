from multiprocessing import Process
import os
import time


def func():
    print('子进程id:', os.getpid())
    print('所属父进程id:', os.getppid())
    print('子进程启动的函数！')
    time.sleep(3)
    print('子进程执行完毕！')


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    # p.join()  # 阻塞
    # 这种主进程结束，子进程还在执行的进程我们叫做僵尸进程
    print('主进程执行的代码！')
    print('主进程id:', os.getpid())
    print('主进程执行完毕！')
