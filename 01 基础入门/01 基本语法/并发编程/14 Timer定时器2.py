"""
需要说明的是，Timer 只能控制函数在指定时间内执行一次，如果要使用 Timer 控制函数多次重复执行，则需要再执行下一次调度。

如果程序想取消 Timer 的调度，则可调用 Timer 对象的 cancel() 函数。例如，如下程序每 1s 输出一次当前时间：
"""
from threading import Timer
import time

# 定义总共输出几次的计数器
count = 0


def print_time():
    print("当前时间：%s" % time.ctime())
    global t, count
    count += 1
    # 如果count小于10，开始下一次调度
    if count < 10:
        t = Timer(1, print_time)
        t.start()


if __name__ == '__main__':
    # 指定1秒后执行print_time函数
    t = Timer(1, print_time)
    t.start()
