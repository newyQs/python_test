"""
同步是指完成事务的逻辑，先执行第一个事务，如果阻塞了，会一直等待，直到这个事务完成，再执行第二个事务，顺序执行；

异步是和同步相对的；

异步是指在处理调用这个事务之后，不会等待这个事务的处理结果，直接处理其他事务去了，通过状态、通知、回调来通知调用者处理结果；
"""
import time


def hello():
    time.sleep(1)


def run():
    for i in range(5):
        hello()
        print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！


if __name__ == '__main__':
    run()
