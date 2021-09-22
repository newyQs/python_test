import gevent


def func(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)  # 要让 greenlet交替运行，可以通过 gevent.sleep() 交出控制权


if __name__ == '__main__':
    g1 = gevent.spawn(func, 3)
    g2 = gevent.spawn(func, 3)
    g3 = gevent.spawn(func, 3)

    g1.join()
    g2.join()
    g3.join()
