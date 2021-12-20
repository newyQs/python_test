"""
在使用代码操作redis时，链接、操作、断开都是网络IO
"""
import asyncio
import aioredis


async def execute(address, password):
    print("开始执行：", address)
    # 网络IO操作，先去连接10.61.67.6，遇到IO则自动切换任务，去连接10.61.67.8
    redis = await aioredis.create_redis_pool(address, password=password)
    # 网络IO操作，遇到IO自动切换任务
    await redis.hmset_dict("car", key1=1, key2=2, key3=3)
    # 网络IO操作，遇到IO自动切换任务
    result = await redis.hgetall("car", encoding="utf-8")
    print(result)

    redis.close()
    # 网络IO操作，遇到IO自动切换任务
    await redis.wait_closed()
    print("结束：", address)


if __name__ == '__main__':
    tasks = [
        execute("redis://10.61.67.6", "root"),
        execute("redis://10.61.67.8", "root")
    ]
    asyncio.run(asyncio.wait(tasks))
