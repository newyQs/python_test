# Stream 函数
下面的高级 asyncio 函数可以用来创建和处理流:

### coroutine asyncio.open_connection(host=None, port=None, *, loop=None, limit=None, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None)
建立网络连接并返回一对 (reader, writer) 对象。

返回的 reader 和 writer 对象是 StreamReader 和 StreamWriter 类的实例。

loop 参数是可选的，当从协程中等待该函数时，总是可以自动确定。

limit 确定返回的 StreamReader 实例使用的缓冲区大小限制。默认情况下，limit 设置为 64 KiB 。

其余的参数直接传递到 loop.create_connection() 。

3.7 新版功能: ssl_handshake_timeout 形参。

### coroutine asyncio.start_server(client_connected_cb, host=None, port=None, *, loop=None, limit=None, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, start_serving=True)
启动套接字服务。

当一个新的客户端连接被建立时，回调函数 client_connected_cb 会被调用。该函数会接收到一对参数 (reader, writer) ，reader是类 StreamReader 的实例，而writer是类 StreamWriter 的实例。

client_connected_cb 即可以是普通的可调用对象也可以是一个 协程函数; 如果它是一个协程函数，它将自动作为 Task 被调度。

loop 参数是可选的。当在一个协程中await该方法时，该参数始终可以自动确定。

limit 确定返回的 StreamReader 实例使用的缓冲区大小限制。默认情况下，limit 设置为 64 KiB 。

余下的参数将会直接传递给 loop.create_server().

3.7 新版功能: The ssl_handshake_timeout and start_serving parameters.
