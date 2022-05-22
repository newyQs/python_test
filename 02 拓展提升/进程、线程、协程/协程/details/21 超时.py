# 超时的案例
import asyncio


async def eternity():
    # Sleep for one hour
    # await asyncio.sleep(0.5)
    await asyncio.sleep(3600)
    print('yay!')


async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)  # 等待 可等待对象 完成，超过timeout秒后，抛出asyncio.TimeoutError异常
    except asyncio.TimeoutError:
        print('timeout!')


asyncio.run(main())
