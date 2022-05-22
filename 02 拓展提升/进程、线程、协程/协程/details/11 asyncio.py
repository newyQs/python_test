import asyncio
import time


async def work(delay, msg):
    print(f"Task receives the message :'{msg}' ")
    await asyncio.sleep(delay)
    print(msg)


async def main():
    print(f"Started at {time.strftime('%X')}")
    await work(1, "hello")  # 启动一个协程，但是这是同步执行的
    await work(2, "world")
    print(f"Finished at time {time.strftime('%X')}")


asyncio.run(main())
# 运行结果：
# 先打印print(f"Task receives the message :'{msg}' ")然后等待1秒后打印“hello”，
# 然后再次打印print(f"Task receives the message :'{msg}' ")等待2秒后打印“world”
