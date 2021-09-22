from multiprocessing import Process
import os


class MyProcess(Process):
    def __init__(self, person):
        super().__init__()
        self.person = person

    def run(self):
        print(os.getpid())
        print(self.pid)
        print(f'我是谁：{self.person}')


if __name__ == '__main__':
    p1 = MyProcess('lucy')
    p2 = MyProcess('jack')

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('主进程已结束！')
