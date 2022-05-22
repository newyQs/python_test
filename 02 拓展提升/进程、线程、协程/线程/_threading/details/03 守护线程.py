import threading
import time


def run(n):
    print("task", n)
    time.sleep(1)  # 此时子线程停1s
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')


if __name__ == '__main__':
    t = threading.Thread(target=run, args=("t1",))
    t.setDaemon(True)  # 把子进程设置为守护线程，必须在start()之前设置
    t.start()
    print("end")
