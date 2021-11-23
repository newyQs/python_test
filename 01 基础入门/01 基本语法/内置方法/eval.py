"""
eval() 函数用来执行一个字符串表达式，并返回表达式的值。

eval(expression[, globals[, locals]])

"""

x = 7
print(eval('3 * x'))
print(eval('pow(2,2)'))
print(eval('2 + 2'))

# 去掉字符串本身的引号
a = "123"
print(type(a))
b = eval(a)
print(type(b))
