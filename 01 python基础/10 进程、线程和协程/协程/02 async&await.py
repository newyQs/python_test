import asyncio


async def func(i):
    print('test1', i)
    await asyncio.sleep(1)
    print('test2', i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [func(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
