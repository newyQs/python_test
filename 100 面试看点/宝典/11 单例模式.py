"""
单例模式应用的场景一般发现在以下条件下：
（1）资源共享的情况下，避免由于资源操作时导致的性能或损耗等。如日志文件，应用配置。
（2）控制资源的情况下，方便资源之间的互相通信。如线程池等。 1.网站的计数器 2.应用配置 3.多线程池 4.
数据库配置，数据库连接池 5.应用程序的日志应用....
"""


class A(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance
        else:
            return cls._instance


a1 = A()
a2 = A()

print(id(a1), id(a2))
