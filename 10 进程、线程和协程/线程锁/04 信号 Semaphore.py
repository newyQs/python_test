import threading
import time

'''
类名：BoundedSemaphore。这种锁允许一定数量的线程同时更改数据，它不是互斥锁。
比如地铁安检，排队人很多，工作人员只允许一定数量的人进入安检区，其它的人继续排队。
'''


def run(n, suo):
    suo.acquire()
    print('run the thread:%s' % n)
    time.sleep(1)
    suo.release()


semaphore = threading.BoundedSemaphore(10)
for i in range(20):
    t = threading.Thread(target=run, args=(i, semaphore))
    t.start()
