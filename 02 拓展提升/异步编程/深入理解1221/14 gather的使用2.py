"""

"""
import asyncio
import time


async def step1(n, start):
    await asyncio.sleep(n)
    print("第一阶段完成")
    print("此时用时", time.time() - start)
    return n


async def step2(n, start):
    await asyncio.sleep(n)
    print("第二阶段完成")
    print("此时用时", time.time() - start)
    return n


async def main():
    now = time.time()
    result = await asyncio.gather(step1(5, now), step2(2, now))
    for i in result:
        print(i)
    print("总用时", time.time() - now)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
