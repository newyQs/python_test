"""

"""
import time
import asyncio
import concurrent.futures


def func1():
    time.sleep(1)
    return "end"


async def main():
    loop = asyncio.get_running_loop()

    # 1. run in the  default loop's executor （默认ThreadPoolExecutor）
    # 第一步：内部会先调用ThreadPoolExecutor的submit方法去线程池中申请一个线程去执行func1函数，并返回一个concurrent.futures.Future对象，
    # 第二步：调用asyncio.wrap_future将concurrent.futures.Future对象包装成asyncio.Future对象，
    # 因为concurrent.futures.Future对象不支持await语法，所以需要包装成asyncio.Future对象才能使用。
    fut = loop.run_in_executor(None, func1)
    result = await fut
    print("default thread pool", result)

    # # 2. run in a custom thread pool:
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print("custom thread pool", result)
    #
    # # 3. run in a custom process pool:
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print("custom process pool", result)


if __name__ == '__main__':
    asyncio.run(main())
