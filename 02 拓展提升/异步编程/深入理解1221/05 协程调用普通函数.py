"""
在协程中可以通过一些方法去调用普通的函数。
可以使用的关键字有call_soon,call_later，call_at

loop.call_soon(callback, *args, context=None)
"""
import asyncio
import functools


def callback(args, *, kwargs="default"):
    print(f"普通函数作为回调函数,获取参数:{args},{kwargs}")


async def main(loop):
    print("注册callback")
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwargs="not default")
    loop.call_soon(wrapped, 2)  # 仅支持2个参数
    await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()
