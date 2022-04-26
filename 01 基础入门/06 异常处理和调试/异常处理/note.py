#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This is notebook foe exception

try:
    pass  # 需要判断是否会抛出异常的代码，如果没有异常处理，python会直接停止执行程序
except:  # 这里会捕捉到上面代码中的异常，并根据异常抛出异常处理信息
    # except ExceptionName，args：
    pass  # 这里执行异常处理的相关代码，打印输出等
else:  # 如果没有异常则执行else
    pass  # try部分被正常执行后的执行代码
finally:
    pass  # 退出try语句块总会执行的程序
