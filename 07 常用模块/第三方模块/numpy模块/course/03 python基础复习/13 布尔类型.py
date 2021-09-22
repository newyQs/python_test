# Python实现了所有常用的布尔逻辑运算符，但它使用的是英文单词而不是符号 (&&, ||, etc.)：
t = True
f = False
print(type(t))  # Prints "<class 'bool'>"
print(t and f)  # Logical AND; prints "False"
print(t or f)  # Logical OR; prints "True"
print(not t)  # Logical NOT; prints "False"
print(t != f)  # Logical XOR; prints "True"
