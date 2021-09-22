# 与大多数语言一样，Python有许多基本类型，包括整数，浮点数，布尔值和字符串。
# 这些数据类型的行为方式与其他编程语言相似。

x = 3
print(type(x))  # Prints "<class 'int'>"
print(x)  # Prints "3"
print(x + 1)  # Addition; prints "4"
print(x - 1)  # Subtraction; prints "2"
print(x * 2)  # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"

y = 2.5
print(type(y))  # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2)  # Prints "2.5 3.5 5.0 6.25"

# 注意，与许多语言不同，Python没有一元增量(x+)或递减(x-)运算符
