# -*- coding:utf8 -*-
import os, time
from multiprocessing import Process, Pipe, current_process


def proc1(pipe, data):
    for msg in range(1, 6):
        print('{0} 发送 {1}'.format(current_process().name, msg))
        pipe.send(msg)
        time.sleep(1)
    pipe.close()


def proc2(pipe, length):
    count = 0
    while True:
        count += 1
        if count == length:
            pipe.close()
        try:
            # 如果没有接收到数据recv会一直阻塞，如果管道被关闭，recv方法会抛出EOFError
            msg = pipe.recv()
            print('{0} 接收到 {1}'.format(current_process().name, msg))
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    conn1, conn2 = Pipe(True)
    data = range(0, 6)
    length = len(data)
    proc1 = Process(target=proc1, args=(conn1, data))
    proc2 = Process(target=proc2, args=(conn2, length))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    print('Done.')
