"""

"""
import asyncio
import uvicorn
import aioredis
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()

REDIS_POOL = aioredis.ConnectionsPool("redis://10.61.67.8:6379", password="root", minsize=1, maxsize=10)


@app.get("/")
def index():
    """普通操作接口"""
    return {"message": "hello world"}


@app.get("/red")
async def red():
    """异步操作接口"""
    await asyncio.sleep(1)

    # 连接池获取一个连接
    conn = await REDIS_POOL.acquire()
    redis = Redis(conn)

    # 设置值
    await redis.hmget_dict("car", key1=1, key2=2, key3=3)

    # 读取值
    result = await redis.hgetall("car", encodeing="utf-8")
    print(result)

    # 连接归还连接池
    REDIS_POOL.release(conn)

    return result


if __name__ == '__main__':
    uvicorn.run("luffy:app", host="12.7.03 爬虫基本原理.03 爬虫基本原理.1", port=5000, log_level="info")
