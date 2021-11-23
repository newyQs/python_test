# 1.读取内容的三个方法
# read([k])
# readline([l])
# readlines([l])

f = open('./io/poem.txt', 'r', encoding='utf-8')
data = f.read()
data_k=f.read(18)
data_rl=f.readline()
data_rf_l = f.readline(24)
data_rls = f.readlines()
data_rls_h = f.readlines(2)
f.close()
print(data_rls)
print(type(data_rls)) # list

with open("./io/poem.txt", "r", encoding='utf-8') as f:
    while True:
        data = f.read(5)
        if data == "":  # 没有数据了退出循环
            break
        print(data)

with open("./io/poem.txt", "r", encoding='utf-8') as f:
    while True:
        dataline = f.readline()
        if dataline == "":  # 没有数据了退出循环
            break
        print(dataline)

with open("./io/poem.txt", "r", encoding='utf-8') as f:
    datalines = f.readlines()

print(datalines)

# 2.正确将文件对象关闭
try:
    f = open("./io/poem.txt", "r", encoding='utf-8')
    data = f.read()
    print(data)
    print(data.fuck)  # 报异常，退出 try 语句，进入 except 语句
    f.close()  # 解释器不会执行这条语句
except:
    f.close()
    raise ("文件操作出现错误")

# 3.使用with语句
with open("./io/poem.txt", "r", encoding='utf-8') as f:
    data = f.read()
    print(data)
    print(data.fuck)  # 虽然报异常，但在 with 块内，解释器会自动调用 close 函数，关闭文件对象

# 4.读取二进制文件（视频，图片，音频）
with open('./io/cat.jpg', 'rb') as f:
    data = f.read()

# print(data)
print(type(data))  # bytes
