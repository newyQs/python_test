"""

"""
import asyncio
import functools


def callback(future, n):
    print('{}: future done: {}'.format(n, future.result()))


async def register_callbacks(all_done):
    print('注册callback到future对象')
    all_done.add_done_callback(functools.partial(callback, n=1))
    all_done.add_done_callback(functools.partial(callback, n=2))


async def main(all_done):
    await register_callbacks(all_done)
    print('设置future的结果')
    all_done.set_result('the result')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        loop.run_until_complete(main(all_done))
    finally:
        loop.close()
