"""
CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）

"""
import pandas as pd

df = pd.read_csv('nba.csv')
# to_string() 用于返回 DataFrame 类型的数据
print(df.to_string())

print("========== 分隔符1 ==========")

# 如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。
print(df)

print("========== 分隔符2 ==========")

# 三个字段 name, site, age
name = ["Google", "Runoob", "Taobao", "Wiki"]
site = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
age = [90, 40, 80, 98]

# 字典
dic = {'name': name, 'site': site, 'age': age}
df = pd.DataFrame(dic)

# 保存 dataframe
df.to_csv('site.csv')

print("========== 分隔符3 ==========")

# 数据处理
df = pd.read_csv('nba.csv')
# head()
# head(n) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。
print(df.head())
print(df.head(10))

# tail()
# tail(n) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN
print(df.tail())
print(df.tail(10))

# info()
# info() 方法返回表格的一些基本信息：
print(df.info())
