from .tasks import send
import time


def register():
    start = time.time()
    send.delay('666')
    print('耗时:', time.time() - start)


if __name__ == '__main__':
    register()
