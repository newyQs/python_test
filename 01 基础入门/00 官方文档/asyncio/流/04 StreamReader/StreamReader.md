# StreamReader
### class asyncio.StreamReader
这个类表示一个提供api来从IO流中读取数据的读取器对象。

不推荐直接实例化 StreamReader 对象，建议使用 open_connection() 和 start_server() 来获取 StreamReader 实例。

coroutine read(n=-1)
读取 n 个byte. 如果没有设置 n , 则自动置为 -1 ，读至 EOF 并返回所有读取的byte。

如果读到EOF，且内部缓冲区为空，则返回一个空的 bytes 对象。

coroutine readline()
读取一行，其中“行”指的是以 \n 结尾的字节序列。

如果读到EOF而没有找到 \n ，该方法返回部分读取的数据。

如果读到EOF，且内部缓冲区为空，则返回一个空的 bytes 对象。

coroutine readexactly(n)
精准读取 n 个 bytes，不能超过也不能少于。

如果在读取完 n 个byte之前读取到EOF，则会抛出 IncompleteReadError 异常。使用 IncompleteReadError.partial 属性来获取到达流结束之前读取的 bytes 字符串。

### coroutine readuntil(separator=b'\n')
从流中读取数据直至遇到 分隔符

成功后，数据和指定的separator将从内部缓冲区中删除(或者说被消费掉)。返回的数据将包括在末尾的指定separator。

如果读取的数据量超过了配置的流限制，将引发 LimitOverrunError 异常，数据将留在内部缓冲区中并可以再次读取。

如果在找到完整的separator之前到达EOF，则会引发 IncompleteReadError 异常，并重置内部缓冲区。 IncompleteReadError.partial 属性可能包含指定separator的一部分。

3.5.2 新版功能.

### at_eof()
如果缓冲区为空并且 feed_eof() 被调用，则返回 True 。