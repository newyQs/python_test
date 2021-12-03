import gevent
from gevent import monkey

monkey.patch_all()


def func(name):
    a = 0
    print(name)
    print("我下面做计算导致的阻塞，你协程库也没啥卵用啊。。。")
    while True:  # CPU（计算）密集型
        a += 1


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(func, "任务1"),
        gevent.spawn(func, "任务2"),
        gevent.spawn(func, "任务3")
    ])
