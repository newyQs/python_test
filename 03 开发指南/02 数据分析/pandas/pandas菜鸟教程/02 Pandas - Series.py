"""
Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。

Series 由索引（index）和列组成，函数如下：
    pandas.Series( data, index, dtype, name, copy)

参数说明：
    data：一组数据(ndarray 类型)。
    index：数据索引标签，如果不指定，默认从 0 开始。
    dtype：数据类型，默认会自己判断。
    name：设置名称。
    copy：拷贝数据，默认为 False。
"""
import pandas as pd

# 1. 通过列表创建
a = [1, 2, 3]
# 未指定索引
myvar = pd.Series(a)
print(myvar)
print(myvar[1])

print("========== 分隔符1 ==========")

a = ["Google", "Runoob", "Wiki"]
# 指定索引
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])

print("========== 分隔符2 ==========")

# 2. 通过字典创建
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites)
print(myvar)

print("========== 分隔符3 ==========")

# 指定索引数据
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index=[1, 2])
print(myvar)

print("========== 分隔符4 ==========")

# 3. 设置 Series 名称参数
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index=[1, 2], name="RUNOOB-Series-TEST")

print(myvar)
