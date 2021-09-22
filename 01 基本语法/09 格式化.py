# 1.传统的%号格式化
'''
%s
%d
%f
%x
'''

# 2.str.format()格式化
"{} {}".format("hello", "world")  # 不设置指定位置，按默认顺序

"{0} {1}".format("hello", "world")  # 设置指定位置

"{1} {0} {1}".format("hello", "world")  # 设置指定位置

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

# 3.f-string
