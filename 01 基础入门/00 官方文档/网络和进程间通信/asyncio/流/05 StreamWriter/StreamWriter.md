# StreamWriter
### class asyncio.StreamWriter
这个类表示一个写入器对象，该对象提供api以便于写数据至IO流中。

不建议直接实例化 StreamWriter；而应改用 open_connection() 和 start_server()。

### can_write_eof()
如果下层的传输支持 write_eof() 方法则返回``True``，否则返回 False。

### write_eof()
在已缓冲的写入数据被刷新后关闭流的写入端。

### transport
返回下层的 asyncio 传输。

### get_extra_info(name, default=None)
访问可选的传输信息；详情参见 BaseTransport.get_extra_info()。

### write(data)
Write data to the stream.

This method is not subject to flow control. Calls to write() should be followed by drain().

### writelines(data)
Write a list (or any iterable) of bytes to the stream.

This method is not subject to flow control. Calls to writelines() should be followed by drain().

### coroutine drain()
等待直到可以适当地恢复写入到流。 示例:

### writer.write(data)
await writer.drain()
这是一个与下层的 IO 写缓冲区进行交互的流程控制方法。 当缓冲区大小达到最高水位（最大上限）时，drain() 会阻塞直到缓冲区大小减少至最低水位以便恢复写入。 当没有要等待的数据时，drain() 会立即返回。

### close()
Close the stream.

### is_closing()
如果流已被关闭或正在被关闭则返回 True。

3.7 新版功能.

### coroutine wait_closed()
等待直到流被关闭。

应当在 close() 之后被调用以便等待直到下层的连接被关闭。

3.7 新版功能.