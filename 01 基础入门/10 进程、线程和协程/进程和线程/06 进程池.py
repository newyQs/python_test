from multiprocessing import Pool
import time


def func(args):
    time.sleep(1)
    print('正在执行：', args)


if __name__ == '__main__':
    p = Pool(10)
    for num in range(100):
        # 每次循环会用空闲出来的子进程去调用目标
        p.apply_async(func=func, args=(num,))  # p.apply_async(调用的目标函数，（传递的参数元组）)

    p.close()
    p.join()

'''
进程的开销比较大，创建过多的新进程会消耗大量的内存空间和时间（CPU来回切换轮询进程）；
这里，通过进程池可以控制内存开销；
进程池内部维护了一个进程序列，需要时就去进程池拿一个进程，
如果进程池中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止；

进程池中常用的方法：
apply()         同步执行（串行） （不建议使用，并且3.x以后不再出现）
apply_async()   异步执行（并行）
map()
map_async()
terminate()     立刻关闭进程池，不再处理未处理的任务
close()         关闭进程池（pool），使其不再接受新的任务
join()          主进程阻塞等待所有子进程执行完毕，必须在close()或terminate()之后使用
'''
