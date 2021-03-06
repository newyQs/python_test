"""
使用asyncio.run()调用一个协程
"""
import asyncio


async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")


# 文件及目录操作() # 简单的调用不会起作用

# 要真正运行一个协程，asyncio 提供了三种主要机制:
# 1.asyncio.run() 函数用来运行最高层级的入口点 "文件及目录操作()" 函数
asyncio.run(main())

# 2.等待一个协程


# 3.asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程

