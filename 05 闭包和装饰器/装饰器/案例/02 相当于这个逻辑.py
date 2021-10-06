import time


# 装饰器函数
def total_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


def hello_word():
    time.sleep(0.5)
    print('hello word')


if __name__ == '__main__':
    # 把函数当做参数传入装饰器函数，然后装饰器函数返回包裹函数wrapper地址，执行装饰器函数本质上执行包裹函数wrapper中逻辑
    total_time = total_time(hello_word)
    total_time()

    # 相当于
    # total_time(hello_word)()
