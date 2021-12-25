"""
流是用于处理网络连接的高级 async/await-ready 原语。流允许发送和接收数据，而不需要使用回调或低级协议和传输

下面是一个使用 asyncio streams 编写的 TCP echo 客户端示例:
"""
import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()


if __name__ == '__main__':
    asyncio.run(tcp_echo_client('Hello World!'))
