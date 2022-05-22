# -*- coding:utf8 -*-
import os, time, random
from multiprocessing import Process, Queue


def write(q):
    print('Process to write: %s' % os.getpid())
    for val in range(0, 6):
        print('Put %s to queue...' % val)
        q.put(val)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        try:
            val = q.get(block=True, timeout=5)
            print('Get %s from queue.' % val)
        except Exception as e:
            if q.empty():
                print('队列消费完毕.')
                break


if __name__ == '__main__':
    q = Queue()

    proc1 = Process(target=write, args=(q,))
    proc2 = Process(target=read, args=(q,))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    # 如果proc2不break的话会一直阻塞，不调用join调用terminate方法可以终止进程
    # proc2.terminate()

    print('Done.')
