from multiprocessing import Process
import time


def counter():
    count = 1
    data = 1
    while count < 500000:
        count += 1
        data += data


if __name__ == '__main__':
    bg_time = time.time()
    p1 = Process(target=counter)
    p2 = Process(target=counter)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time()

    print(f'多进程耗时：{end_time - bg_time}')
