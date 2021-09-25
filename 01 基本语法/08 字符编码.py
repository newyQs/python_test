'''
计算机最早由美国人发明的，最开始只有127个字符被编码到计算机里面，如大小写字母，数字，和一些符号，这些被称为ASCII编码。
如我们所知，一个字节（1 bytes）可以表示的范围是0~255（0~2**8-1），因此一个字节就可以表示出所有的ASCII编码。

但是，使用1个字节处理中文是远远不够的，至少得2个字节，2个字节可表示的范围为0~65535（0~2**16-1），这些被称为unicode编码。
通常在字符的前面加上u表示计算机使用unicode储存字符串。

考虑一个问题，如果一段字符串只有极少数中文，而大多数都是英文，那使用unicode编码将会增大存储空间，在储存和传输上显得十分不划算，
因此就出现了utf-8编码，它可以智能的将字母（a-zA-Z），数字（0~9）等使用1个字节表示，中文使用2~4个字节表示。

在 Python3 中，字符串前面什么都不要加，默认就是采用 UTF-8 编码；如果加上 u 就是 UNICODE 编码。

gbk 编码是微软出的对含有中文的字符串进行编码的一种格式，gbk 对 ascii 使用 1 个字节，对中文使用 2 个字节。
'''
print('hello'.encode())
print(b'hello'.decode())

print(len('hello'))
