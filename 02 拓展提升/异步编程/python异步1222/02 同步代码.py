import time
import asyncio


# 定义异步函数
async def hello():
    await asyncio.sleep(1)
    print('Hello World:%s' % time.time())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [hello() for i in range(100)]
    loop.run_until_complete(asyncio.wait(tasks))
