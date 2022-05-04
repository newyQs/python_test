from io import StringIO

# 1.创建文件对象，写入字符串，使用getvalue获取
f = StringIO()
f.write('hello')
data = f.getvalue()
f.close()

print(data)

# 2.直接在创建StringIO的时候，写入字符串
f = StringIO('hello')
data = f.getvalue()
f.close()

print(data)

# 3.调用write和read方法
# write和read方法会将指针指向在字符串的末尾
f = StringIO("hello")
# f.write("hello")
print(f.read())  # 从字符串末尾开始读，所以没有内容
f.close()

# 4.使用seek定位指针，然后读取内容
# getvalue方法会读取整个字符串
f = StringIO()
f.write("hello")
f.seek(0)  # 指针重新定位到字符串开始
print(f.read())  # 读完后指针又定位到字符串末尾
f.seek(0)  # 指针重新定位到字符串开始
print(f.read())  # 读完后指针又定位到字符串末尾
print(f.getvalue())  # getvalue 函数总是从字符串开始位置开始读
f.close()  # 不要忘记调用文件对象的 close 函数


# 5.自定义一个StringIO类
class MyStringIO(object):
    def __init__(self, data):
        self.data = data

    def read(self):
        return self.data

    def write(self, data):
        self.data = data

    def getvalue(self):
        return self.data

    def close(self):
        del self.data


f = MyStringIO("hello")
print(f.getvalue())
f.close()
