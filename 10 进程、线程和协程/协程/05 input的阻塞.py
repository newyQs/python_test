import gevent
from gevent import monkey

monkey.patch_all()


def func(name):
    print(name)
    input("我阻塞，你协程库能奈我何...")


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(func, "任务1"),
        gevent.spawn(func, "任务2"),
        gevent.spawn(func, "任务3")
    ])
