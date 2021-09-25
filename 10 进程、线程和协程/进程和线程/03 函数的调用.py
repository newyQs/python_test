from multiprocessing import Process
import os


def func(name):
    print(f'调用我的进程名字：{name}；子进程id是{os.getpid()}；父进程id是{os.getppid()}')


if __name__ == '__main__':
    p1 = Process(target=func, args=('子进程1',))  # args是传入到调用函数里的参数，是一个元组
    p2 = Process(target=func, args=('子进程2',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    func('主进程')

'''
开启的进程依赖于一个函数执行，而不能说子进程就是函数。
'''
