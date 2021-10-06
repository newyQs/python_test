'''
基于官方文档3.9.7
'''


# ========= all ==========
# print(all([]))  # True
# all(iterable)。参数是一个可迭代对象，如果iterable中所有元素均为真值（或iterable为空），结果返回True，否则返回False。
# 相当于:iterable中只要又一个为假，就返回False。
def all(iterable):
    for item in iterable:
        if not item:
            return False
    return True


# ========= any ==========
# print(any([]))  # False
# any(iterable)。参数是一个可迭代对象，如果iterable中只要有一个元素为真值，记过返回True，否则返回False（iterable为空）。
# 相当于：
def any(iterable):
    for item in iterable:
        if item:
            return True
    return False


# ========= int ==========
# 返回一个基于数字或字符串x构造的整数对象，或者在未给出参数时，返回0。
print(int())

# ========= float ==========
# 返回从数字或字符串x生产的浮点数，或者在未给出参数时，返回0.0。
print(float())

# ========= bool ==========
# 返回一个布尔值True和False。
print(bool())

# ========= complex ==========
# 返回值为real+imag*1j的复数，或者将字符串或者数字转换为复数。
print(complex())

# ========= bin ==========
# 将一个整数转变为前缀为"0b"的二进制字符串。
print(bin(10))

# ========= oct ==========
# 将一个整数转变为前缀为"0o"的八进制字符串。
print(oct(10))

# ========= hex ==========
# 将一个整数转变为前缀为"0x"的小写十六进制字符串。
print(hex(10))

# ========= abs ==========
# 返回一个数的绝对值，参数可以是整数/浮点数/或实现了__abs__()的对象。如果参数是复数，则返回模。
print(abs(-3))
print(abs(-2.5))
print(abs(1 + 5j))

# ========= divmode ==========
# 将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数。


# ========= round ==========


# ========= pow ==========


# ========= sum ==========


# ========= min ==========


# ========= max ==========
