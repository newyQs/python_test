"""
一个异步方法就被称为一个协程（Coroutine）
"""
import asyncio


async def foo():
    print("这是一个协程")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("开始运行协程")
        coroutine = foo()
        print("进入异步循环")
        loop.run_until_complete(coroutine)
    finally:
        print("关闭事件循环")
        loop.close()
