

# 1.定义
# 使用def关键字定义
def func_name(*args, **kwargs):
    pass


# 2.函数参数
# 分为：位置参数；默认参数；可变参数；关键字参数；命名关键字参数；

# 3.返回值
# 默认return None
def myfunc():
    return "ruhua", "xingxing", "zhaoritian"


rst = myfunc()
print(rst)  # 可以看到是一个 tuple
print(type(rst))  # tuple 类型
