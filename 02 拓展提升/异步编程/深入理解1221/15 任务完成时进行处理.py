import asyncio
import time


async def foo(n):
    print('Waiting: ', n)
    await asyncio.sleep(n)
    return n


async def main():
    coroutine1 = foo(1)
    coroutine2 = foo(2)
    coroutine3 = foo(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    for task in asyncio.as_completed(tasks):
        result = await task
        print('Task ret: {}'.format(result))


now = lambda: time.time()
start = now()

loop = asyncio.get_event_loop()
done = loop.run_until_complete(main())
print(now() - start)
