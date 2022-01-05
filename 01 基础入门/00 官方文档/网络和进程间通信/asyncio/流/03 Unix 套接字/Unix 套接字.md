# Unix 套接字

### coroutine asyncio.open_unix_connection(path=None, *, loop=None, limit=None, ssl=None, sock=None, server_hostname=None, ssl_handshake_timeout=None)
建立一个 Unix 套接字连接并返回 (reader, writer) 这对返回值。

与 open_connection() 相似，但是操作在 Unix 套接字上

请看文档 loop.create_unix_connection().

可用性: Unix。

3.7 新版功能: ssl_handshake_timeout 形参。

在 3.7 版更改: path 现在是一个 path-like object

### coroutine asyncio.start_unix_server(client_connected_cb, path=None, *, loop=None, limit=None, sock=None, backlog=100, ssl=None, ssl_handshake_timeout=None, start_serving=True)
启动一个Unix socket服务。

与 start_server() 相似，但是是在 Unix 套接字上的操作。

请看文档 loop.create_unix_server().

可用性: Unix。

3.7 新版功能: The ssl_handshake_timeout and start_serving parameters.

在 3.7 版更改: path 形参现在可以是 path-like object 对象。