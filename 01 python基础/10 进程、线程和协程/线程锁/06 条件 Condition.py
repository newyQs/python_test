import threading
import time

num = 0
con = threading.Condition()


class Mythread(threading.Thread):
    def __init__(self, name, action):
        super(Mythread, self).__init__()
        self.name = name
        self.action = action

    def run(self):
        global num
        con.acquire()
        print("%s开始执行..." % self.name)
        while True:
            if self.action == "add":
                num += 1
            elif self.action == 'reduce':
                num -= 1
            else:
                exit(1)
            print("num当前为：", num)
            time.sleep(1)
            if num == 5 or num == 0:
                print("暂停执行%s！" % self.name)
                con.notify()
                con.wait()
                print("%s开始执行..." % self.name)
        con.release()


if __name__ == '__main__':
    t1 = Mythread("线程 A", 'add')
    t2 = Mythread("线程 B", 'reduce')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
