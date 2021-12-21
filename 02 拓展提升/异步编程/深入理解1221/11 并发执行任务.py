"""

"""
import asyncio


async def child():
    print("进入子协程")
    return "the result"


async def main(loop):
    print("将协程child包装成任务")
    task = loop.create_task(child())
    print("通过cancel方法可以取消任务")
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("取消任务抛出CancelledError异常")
    else:
        print("获取任务的结果", task.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()
