# Task 对象
## class asyncio.Task(coro, *, loop=None)
一个与 Future 类似 的对象，可运行 Python 协程。非线程安全。

Task 对象被用来在事件循环中运行协程。如果一个协程在等待一个 Future 对象，Task 对象会挂起该协程的执行并等待该 Future 对象完成。当该 Future 对象 完成，被打包的协程将恢复执行。

事件循环使用协同日程调度: 一个事件循环每次运行一个 Task 对象。而一个 Task 对象会等待一个 Future 对象完成，该事件循环会运行其他 Task、回调或执行 IO 操作。

使用高层级的 asyncio.create_task() 函数来创建 Task 对象，也可用低层级的 loop.create_task() 或 ensure_future() 函数。不建议手动实例化 Task 对象。

要取消一个正在运行的 Task 对象可使用 cancel() 方法。调用此方法将使该 Task 对象抛出一个 CancelledError 异常给打包的协程。如果取消期间一个协程正在等待一个 Future 对象，该 Future 对象也将被取消。

cancelled() 可被用来检测 Task 对象是否被取消。如果打包的协程没有抑制 CancelledError 异常并且确实被取消，该方法将返回 True。

asyncio.Task 从 Future 继承了其除 Future.set_result() 和 Future.set_exception() 以外的所有 API。

Task 对象支持 contextvars 模块。当一个 Task 对象被创建，它将复制当前上下文，然后在复制的上下文中运行其协程。

在 3.7 版更改: 加入对 contextvars 模块的支持。

### cancel()
请求取消 Task 对象。

这将安排在下一轮事件循环中抛出一个 CancelledError 异常给被封包的协程。

协程在之后有机会进行清理甚至使用 try ... ... except CancelledError ... finally 代码块抑制异常来拒绝请求。不同于 Future.cancel()，Task.cancel() 不保证 Task 会被取消，虽然抑制完全取消并不常见，也很不鼓励这样做。

以下示例演示了协程是如何侦听取消请求的:
```
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): before sleep
#     cancel_me(): cancel sleep
#     cancel_me(): after sleep
#     main(): cancel_me is cancelled now
```
### cancelled()
如果 Task 对象 被取消 则返回 True。

当使用 cancel() 发出取消请求时 Task 会被 取消，其封包的协程将传播被抛入的 CancelledError 异常。

### done()
如果 Task 对象 已完成 则返回 True。

当 Task 所封包的协程返回一个值、引发一个异常或 Task 本身被取消时，则会被认为 已完成。

### result()
返回 Task 的结果。

如果 Task 对象 已完成，其封包的协程的结果会被返回 (或者当协程引发异常时，该异常会被重新引发。)

如果 Task 对象 被取消，此方法会引发一个 CancelledError 异常。

如果 Task 对象的结果还不可用，此方法会引发一个 InvalidStateError 异常。

### exception()
返回 Task 对象的异常。

如果所封包的协程引发了一个异常，该异常将被返回。如果所封包的协程正常返回则该方法将返回 None。

如果 Task 对象 被取消，此方法会引发一个 CancelledError 异常。

如果 Task 对象尚未 完成，此方法将引发一个 InvalidStateError 异常。

### add_done_callback(callback, *, context=None)
添加一个回调，将在 Task 对象 完成 时被运行。

此方法应该仅在低层级的基于回调的代码中使用。

要了解更多细节请查看 Future.add_done_callback() 的文档。

### remove_done_callback(callback)
从回调列表中移除 callback 。

此方法应该仅在低层级的基于回调的代码中使用。

要了解更多细节请查看 Future.remove_done_callback() 的文档。

### get_stack(*, limit=None)
返回此 Task 对象的栈框架列表。

如果所封包的协程未完成，这将返回其挂起所在的栈。如果协程已成功完成或被取消，这将返回一个空列表。如果协程被一个异常终止，这将返回回溯框架列表。

框架总是从按从旧到新排序。

每个被挂起的协程只返回一个栈框架。

可选的 limit 参数指定返回框架的数量上限；默认返回所有框架。返回列表的顺序要看是返回一个栈还是一个回溯：栈返回最新的框架，回溯返回最旧的框架。(这与 traceback 模块的行为保持一致。)

### print_stack(*, limit=None, file=None)
打印此 Task 对象的栈或回溯。

此方法产生的输出类似于 traceback 模块通过 get_stack() 所获取的框架。

limit 参数会直接传递给 get_stack()。

file 参数是输出所写入的 I/O 流；默认情况下输出会写入 sys.stderr。

### classmethod all_tasks(loop=None)
返回一个事件循环中所有任务的集合。

默认情况下将返回当前事件循环中所有任务。如果 loop 为 None，则会使用 get_event_loop() 函数来获取当前事件循环。

此方法 已弃用 并将在 Python 3.9 中移除。请改用 asyncio.all_tasks() 函数。

### classmethod current_task(loop=None)
返回当前运行任务或 None。

如果 loop 为 None，则会使用 get_event_loop() 函数来获取当前事件循环。

此方法 已弃用 并将在 Python 3.9 中移除。请改用 asyncio.current_task() 函数。