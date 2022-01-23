"""

"""
import asyncio
import aiomysql


async def execute(host, password):
    print("开始:", host)
    # 网络IO操作，先去连接10.61.67.6，遇到IO则自动切换任务，去连接10.61.67.8
    conn = await aiomysql.connect(host=host, port=3306, user="root", password=password, db="mysql")
    # 网络IO操作，遇到IO自动切换任务
    cur = await conn.cursor()
    # 网络IO操作，遇到IO自动切换任务
    await cur.execute("SELECT Host,User FROM mysql")
    # 网络IO操作，遇到IO自动切换任务
    result = await cur.fechall()
    print(result)
    # 网络IO操作，遇到IO自动切换任务
    await cur.close()
    conn.close()
    print("结束：", host)


if __name__ == '__main__':
    tasks = [
        execute("10.61.67.6", "root"),
        execute("10.61.67.8", "root")
    ]
    asyncio.run(execute(tasks))
