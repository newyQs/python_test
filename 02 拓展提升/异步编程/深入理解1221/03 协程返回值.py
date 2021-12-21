"""

"""
import asyncio


async def foo():
    print("这是一个协程")
    return "返回值"


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("开始运行协程")
        coroutine = foo()
        print("进入事件循环")
        # run_until_complete可以获取协程的返回值，如果没有给定返回值，则像函数一样，默认返回None
        result = loop.run_until_complete(coroutine)
        print(f"run_until_complete可以获取协程的{result}，默认输出None")
    finally:
        print("关闭事件循环")
        loop.close()
