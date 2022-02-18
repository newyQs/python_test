"""
DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。

DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。

DataFrame 构造方法如下：
    pandas.DataFrame( data, index, columns, dtype, copy)

参数说明：
    data：一组数据(ndarray、series, map, lists, dict 等类型)。
    index：索引值，或者可以称为行标签。
    columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
    dtype：数据类型。
    copy：拷贝数据，默认为 False。


"""
import pandas as pd

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=float)
print(df)

print("========== 分隔符1 ==========")

data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}

df = pd.DataFrame(data)
print(df)

print("========== 分隔符2 ==========")

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

df = pd.DataFrame(data)

print(df)

print("========== 分隔符3 ==========")

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])

print("========== 分隔符4 ==========")

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行和第二行
print(df.loc[[0, 1]])

print("========== 分隔符5 ==========")

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)

print("========== 分隔符6 ==========")

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# 指定索引
print(df.loc["day2"])
