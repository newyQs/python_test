"""

"""
import asyncio


async def main():
    print("主协程")
    print("等待result1协程运行")
    res1 = await result1()
    print("等待result2协程运行")
    res2 = await result2(res1)
    return res1, res2


async def result1():
    print("这是result1协程")
    return "result1"


async def result2(arg):
    print("这是result2协程")
    return f"result2接收了一个参数,{arg}"


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(main())
        print(f"获取返回值:{result}")
    finally:
        print("关闭事件循环")
        loop.close()
