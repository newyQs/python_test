import asyncio


async def work(x):
    for _ in range(3):
        print('Work {} is running ..'.format(x))
    return "Work {} is finished".format(x)


def call_back(future):
    print("Callback: {}".format(future.result()))


coroutine = work(1)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(call_back)
loop.run_until_complete(task)  # 返回任务的结果
