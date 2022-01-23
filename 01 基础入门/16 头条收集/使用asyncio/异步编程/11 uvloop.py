"""
是asyncio循环的替代方案，事件循环>默认的asyncio的事件循环

效率提升至少一倍,django3和fastapi内部就是使用的uvloop 所以快 支持 异步

只需要添加如下两行，其他相同。注意：该模块不支持windows
import uvloop
asyncio.set_event_loop_policy(uvloop.E)
"""
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.E)

# 编写asyncio代码，和之前一样

# 内部的时间循环自动化会变为uvloop
