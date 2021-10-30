def callback_func():
    print('callback')


def time_out(interval, callback=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ########## 该部分必须在requests之前导入
            import gevent
            from gevent import monkey
            monkey.patch_all()
            ##########

            try:
                gevent.with_timeout(interval, func, *args, **kwargs)
            except gevent.timeout.Timeout as e:
                callback() if callback else None

        return wrapper

    return decorator


@time_out(3, callback_func)
def func(a, b):
    import time
    time.sleep(2)
    print(a, b)


func(1, 2)
