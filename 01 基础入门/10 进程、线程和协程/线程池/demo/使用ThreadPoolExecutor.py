#! /usr/bin/env python
# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import time


def sayhello(a):
    print("hello: " + a)
    time.sleep(1)


def main():
    seed = ["a", "b", "c", "d", "e", "f", "g"]

    # 不使用线程
    start1 = time.time()
    for each in seed:
        sayhello(each)
    end1 = time.time()
    print("time1: " + str(end1 - start1))

    # ThreadPoolExecutor使用submit
    start2 = time.time()
    with ThreadPoolExecutor(3) as executor:
        for each in seed:
            executor.submit(sayhello, each)
    end2 = time.time()
    print("time2: " + str(end2 - start2))

    # ThreadPoolExecutor使用map
    start3 = time.time()
    with ThreadPoolExecutor(3) as executor1:
        executor1.map(sayhello, seed)
    end3 = time.time()
    print("time3: " + str(end3 - start3))


if __name__ == '__main__':
    main()

"""
concurrent.futures.ThreadPoolExecutor，在提交任务的时候，有两种方式，一种是submit（）函数，另一种是map（）函数，两者的主要区别在于：

2.1、map可以保证输出的顺序, submit输出的顺序是乱的

2.2、如果你要提交的任务的函数是一样的，就可以简化成map。但是假如提交的任务函数是不一样的，或者执行的过程之可能出现异常（使用map执行过程中发现问题会直接抛出错误）就要用到submit（）

2.3、submit和map的参数是不同的，submit每次都需要提交一个目标函数和对应的参数，map只需要提交一次目标函数，目标函数的参数放在一个迭代器（列表，字典）里就可以。
"""
