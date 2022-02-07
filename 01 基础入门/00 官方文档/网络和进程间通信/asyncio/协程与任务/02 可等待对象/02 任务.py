"""

"""
import asyncio


async def nested():
    return 42


async def main():
    # Schedule nested() to run soon concurrently
    # with "文件及目录操作()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task


asyncio.run(main())
