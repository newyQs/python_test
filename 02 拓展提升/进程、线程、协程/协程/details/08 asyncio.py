import asyncio


async def work(x):  # 通过async关键字定义一个协程
    for _ in range(3):
        print('Work {} is running ..'.format(x))


coroutine_1 = work(1)  # 协程是一个对象，不能直接运行

loop = asyncio.get_event_loop()
task = loop.create_task(coroutine_1)
# task = asyncio.ensure_future(coroutine_1)  # 这样也能创建一个task
print(task)
loop.run_until_complete(task)  # run_until_complete接受的参数是一个future对象，当传人一个协程时，其内部自动封装成task
print(task)
