from multiprocessing import Pool
import time


def func(args):
    time.sleep(1)
    print('正在执行：', args)


if __name__ == '__main__':
    p = Pool(10)
    for num in range(100):
        p.apply_async(func=func, args=(num,))

    p.close()
    p.join()

'''
进程的开销比较大，过多的创建新进程会消耗大量的内存空间和时间（CPU来回切换轮询进程）
通过进程池可以控制内存开销
进程池内部维护了一个进程序列，需要时就去进程池拿取一个进程，
如果进程池中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止

进程池中常用的方法：
apply() 同步执行（串行）
apply_async()异步执行（并行）
terminate()立刻关闭进程池
close()等待所有进程结束，才关闭进程池
join()主进程等待所有子进程执行完毕。必须在close()和terminate()之后。
'''