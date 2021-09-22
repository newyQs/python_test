# 文件对象只能处理字符流和字节流
# 如何处理其他类型，如int,float,dict,list...
# 序列化即把变量从内存中变成可存储或传输的过程（也就是变成字符流或字节流的过程）

import pickle
import os

# 1.可序列化的数据
# data = [1, True, "hello"]
# data = {'name': 'jack', 'age': 18}
#
# seqdata = pickle.dumps(data)  # 序列化
# print(type(seqdata))  # Bytes 类型
# print(seqdata)  # 序列化后的字节流
#
# print('----反序列化----')
# data_reseq = pickle.loads(seqdata)  # 反序列化
# print(type(data_reseq))  # 原类型
# print(data_reseq)  # 原数据

# 2.将序列化后的数据存储在磁盘上
# 将原始数据（list类型）序列化成二进制(bytes类型)数据，再保存到磁盘中
# 写入内容，只有字符类型，或者bytes类型
# mydata = ['gbk', 123, True, {'name': 'lee'}, (1, 2, 3)]
# seq = pickle.dumps(mydata)
# with open('./seq_data.txt', 'wb') as f:  # 必须使用wb模式，二进制bytes类型数据
#     f.write(seq)

# 3.读取磁盘中序列化后的数据到内存
# 从磁盘中读取序列化后的数据（二进制），再使用loads反序列化成原始数据（list类型）
# with open('./seq_data.txt', 'rb') as f:  # rb模式读取二进制数据
#     seq_data = f.read()
#
# print(seq_data, type(seq_data))
# data = pickle.loads(seq_data)
# print(data, type(data))

# 4.序列化的作用
# 类似中介的作用，将内存中某个类型的数据根据一定的算法转换成字符流或字节流
# 同样，反序列化就是将序列化后的字符流或字节流转换成原来的样子
# pickle模块序列化只局限在Python语言中

# 5.pickle模块的主要方法
# dumps 和 loads
msg = ['ad', 1, 4, True]
seq_msg = pickle.dumps(msg)

with open('./msg.txt', 'wb') as f:
    f.write(seq_msg)
# 分割线
with open('./msg.txt', 'rb') as f:
    seq_msg = f.read()

msg = pickle.loads(seq_msg)
print(msg, type(msg))

# dump 和 load
info = ['jkl', 23, None]

with open('./info.txt', 'wb') as f:
    pickle.dump(info, f)

with open('./info.txt', 'rb') as f:
    data = pickle.load(f)

print(data, type(data))
