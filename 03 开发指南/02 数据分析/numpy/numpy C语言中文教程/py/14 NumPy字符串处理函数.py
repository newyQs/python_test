"""

"""
import numpy as np

# 1. numpy.char.add()
# numpy.char.add() 将两个数组对应位置的字符串元素进行连接
print(np.char.add(['welcome', 'url'], [' to C net', 'is c.biancheng.net']))

# 2. numpy.char.multiply()
# 该函数将指定的字符串进行多次拷贝，并将拷贝结果返回
print(np.char.multiply('c.biancheng.net', 3))

# 3. numpy.char.center()
# numpy.char.center() 用于居中字符串
print(np.char.center("c.bianchneg.net", 20, '*'))

# 4. numpy.char.capitalize()
# numpy.char.capitalize() 将字符串的第一个字母转换为大写
print(np.char.capitalize('python'))

# 5. numpy.char.title()
# numpy.char.title() 将字符串数组中每个元素的第一个字母转换为大写
print(np.char.title("welcome to china"))

# 6. numpy.char.lower()
# numpy.char.lower() 将字符串数组中每个元素转换为小写
print(np.char.lower("WELCOME TO MYHOME"))

# 7. numpy.char.upper()
# numpy.char.upper() 将数组中的每个元素转换为大写
print(np.char.upper("Welcome To Python"))

# 8. numpy.char.split()
# 该函数通过指定分隔符对字符串进行分割，并返回数组序列。默认情况下，分隔符为空格
print(np.char.split("Welcome To Python"), sep=" ")

# 9. numpy.char.splitlines()
# numpy.char.splitlines() 以换行符作为分隔符来分割字符串，并返回一个数组序列
print("Splitting the String line by line..")
print(np.char.splitlines("Welcome\nTo\nPython"))

# 10. numpy.char.strip()
print("原字符串:", str)
str = "     welcome to Python     "
print(np.char.strip(str))

# 11. numpy.char.join()
# numpy.char.join() 通过指定的分隔符来连接数组中的元素或字符串
print(np.char.join(':', 'Love'))
# 也可指定多个分隔符
print(np.char.join([':', '-'], ['Love', 'Python']))

# 12. numpy.char.replace()
str = "Welcome to China"
print("原字符串:", str)
# 更改后字符串
print(np.char.replace(str, "Welcome to", "Hello"))

# 13. numpy.char.encode()与decode()
# 默认以utf-8的形式进行编码与解码
# cp500国际编码
encode_str = np.char.encode("Welcome to China", 'cp500')
decode_str = np.char.decode(encode_str, 'cp500')
print(encode_str)
print(decode_str)
