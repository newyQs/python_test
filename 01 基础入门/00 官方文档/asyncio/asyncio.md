python3.6 中文版本
https://docs.python.org/zh-cn/3.6/library/asyncio.html

python3.7中文版本
https://docs.python.org/zh-cn/3.7/library/asyncio.html

# asyncio --- 异步 I/O
asyncio 是用来编写 并发 代码的库，使用 async/await 语法。

asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。

asyncio 往往是构建 IO 密集型和高层级 结构化 网络代码的最佳选择。

asyncio 提供一组 高层级 API 用于:
+ 并发地 运行 Python 协程 并对其执行过程实现完全控制;
+ 执行 网络 IO 和 IPC;
+ 控制 子进程;
+ 通过 队列 实现分布式任务;
+ 同步 并发代码;

此外，还有一些 低层级 API 以支持 库和框架的开发者 实现:
+ 创建和管理 事件循环，以提供异步 API 用于 网络化, 运行 子进程，处理 OS 信号 等等;
+ 使用 transports 实现高效率协议;
+ 通过 async/await 语法 桥接 基于回调的库和代码。