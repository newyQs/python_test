from threading import Timer


def func():
    print("hello everyone this is a 04 first title")


# 表示 3 秒后执行 hello 函数
t = Timer(3, func)
t.start()
t.join()
