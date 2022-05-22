import asyncio


async def work(x):  # 通过async关键字定义一个协程
    for _ in range(3):
        print('Work {} is running ..'.format(x))


coroutine_1 = work(1)  # 协程是一个对象，不能直接运行

# 3.5<version<3.7：
loop = asyncio.get_event_loop()  # 创建一个事件循环
result = loop.run_until_complete(coroutine_1)  # 将协程对象加入到事件循环中，并执行
print(result)  # 协程对象并没有返回结果，打印None
# version≥3.7：
# asyncio.run(coroutine_1)  #创建一个新的事件循环，并以coroutine_1为程序的主入口，执行完毕后关闭事件循环
