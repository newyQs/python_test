import asyncio
import functools


async def work(x):
    for _ in range(3):
        print('Work {} is running ..'.format(x))
    return "Work {} is finished".format(x)


def call_back_2(num, future):
    print("Callback_2: {}, the num is {}".format(future.result(), num))


coroutine = work(1)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(functools.partial(call_back_2, 100))
loop.run_until_complete(task)
