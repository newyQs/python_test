# -*- coding:utf8 -*-
from multiprocessing import Process, Lock


def printer(item, lock):
    # 获取锁
    lock.acquire()
    try:
        print(item)
    except Exception as e:
        print(e)
    else:
        print('no exception.')
    finally:
        # 释放锁
        lock.release()


if __name__ == '__main__':
    # 实例化全局锁
    lock = Lock()
    items = ['PHP', 'Python', 'Java']
    p_list = list()

    for item in items:
        p = Process(target=printer, args=(item, lock))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    print('Done.')
