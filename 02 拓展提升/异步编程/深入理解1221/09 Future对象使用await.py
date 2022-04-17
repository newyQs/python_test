import asyncio


def foo(future, result):
    print("设置结果到future", result)
    future.set_result(result)


async def main(loop):
    all_done = asyncio.Future()
    print("调用函数获取future对象")
    loop.call_soon(foo, all_done, "the result")

    result = await all_done
    print("获取future里的结果", result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()
