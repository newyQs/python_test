'''
https://www.cnblogs.com/ne-zha/p/7482560.html
'''
import time


def total_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)  # 打印统计时间

    return wrapper


# 通过装饰器给hell_word函数装上了统计时间的功能，功能逻辑在装饰器中实现
@total_time
def hello_word():
    time.sleep(0.5)
    print('hello word')


if __name__ == '__main__':
    # hello_word = total_time(hello_word) # 其实经过@total_time装饰后
    hello_word()
