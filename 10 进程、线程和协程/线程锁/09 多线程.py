from threading import Thread
import time


def counter():
    count = 1
    data = 1
    while count < 500000:
        count += 1
        data += data


if __name__ == '__main__':
    bgtime = time.time()
    t1 = Thread(target=counter)
    t2 = Thread(target=counter)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    endtime = time.time()

    print(f'多线程用时：{endtime - bgtime}')
