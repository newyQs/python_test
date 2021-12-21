"""
future表示还没有完成的工作结果。事件循环可以通过监视一个future对象的状态来指示它已经完成。future对象有几个状态：
Pending
Running
Done
Cancelled

创建future的时候，task为pending，事件循环调用执行的时候当然就是running，调用完毕自然就是done，如果需要停止事件循环，就需要先把task取消，状态为cancel。
"""
import asyncio


def foo(future, result):
    print(f"此时future的状态:{future}")
    print(f"设置future的结果:{result}")
    future.set_result(result)
    print(f"此时future的状态:{future}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        loop.call_soon(foo, all_done, "Future is done!")
        print("进入事件循环")
        result = loop.run_until_complete(all_done)
        print("返回结果", result)
    finally:
        print("关闭事件循环")
        loop.close()
    print("获取future的结果", all_done.result())
