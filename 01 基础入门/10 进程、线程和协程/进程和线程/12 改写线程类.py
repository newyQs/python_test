import threading


class MyThreading(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("i'm running......")


if __name__ == '__main__':
    obj = MyThreading()
    obj.start()
    obj.join()
