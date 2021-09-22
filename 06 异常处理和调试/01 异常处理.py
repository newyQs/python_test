# 1.错误处理的两种方式
# 返回值和抛出异常

mystr = "hello"
index = mystr.find("nihao")  # 返回 -1
data = divmod(250, 0)  # 抛出异常


# 2.try...except...finally
#
def division(ldata, rdata):
    if not isinstance(ldata, (int, float)) or not isinstance(rdata, (int, float)):
        raise TypeError("类型错误")

    if rdata == 0:
        raise ValueError("除数不能为 0")
    else:
        return ldata / rdata


try:
    data = division("hello", 4)  # 尝试不同测试用例
except ValueError:
    print("除数不能为 0")
except TypeError:
    print("请输入数字类型数据")
finally:
    print('over')
