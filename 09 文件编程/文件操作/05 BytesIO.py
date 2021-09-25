from io import BytesIO
from urllib import request
from PIL import Image

# 1.操作二进制数据的BytesIO
fr = open("./io/cat.jpg", "rb")  # 确保文件存在
data = fr.read()
fr.close()

f = BytesIO(data)  # data 是字节类型
# print(f.getvalue())  # 结果为字节类型
# print(f.getvalue() == data)  # True
f.close()

# 2. 简单示例
rst = request.urlopen("http://birdpython.com/static/img/logo.png")  # 下载图片
print(rst.read()) # 字节码bytes
f = BytesIO(rst.read())  # 把图片二进制文件放入 BytesIO 对象中

fdisk = open("./io/logo.png", "wb")
fdisk.write(f.getvalue())
fdisk.close()

f.close()

# 3.将下载的图片处理成64像素高，64像素宽，然后存储起来
rst = request.urlopen("http://birdpython.com/static/img/logo.png")  # 下载图片
f = BytesIO(rst.read())  # 把图片二进制文件放入 BytesIO 对象中

img = Image.open(f)  # 需要传入一个文件对象
img.thumbnail((64, 64))  # 修改图片像素大小为 64 x 64
img.save("d:/xx.png")  # 存储处理后的图片

f.close()

# 4.文件IO和内存IO的区别？
'''
本质区别在于文件 IO 是程序通过操作系统操作磁盘文件，而内存 IO 是我们直接用程序操作内存;
想要存储的内容持久化，使用文件 IO，而内存 IO 是对内存进行操作，进程结束后，内存就被操作系统回收了；
文件 IO 有读写标识符，内存 IO 没有读写标识符;
'''
