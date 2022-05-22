# 简单等待的案例
import asyncio


async def foo():
    return 42


task = asyncio.create_task(foo())
# 注意：1、这里传递的要是一个任务组，而不能是单个task，如果只有一个任务，可以这样传递：[task](task,){task}
#       2、直接传递协程对象的方式已弃用 即：done, pending = await asyncio.wait([foo()])
done, pending = await asyncio.wait((task,))

if task in done:
    print(f"The task's result is {task.result()}")
