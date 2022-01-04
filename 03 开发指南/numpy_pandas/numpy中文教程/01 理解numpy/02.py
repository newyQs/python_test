import numpy as np

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
print(a)
print(b)

sum = a + b
difference = a - b
product = a * b
quotient = a / b

print("Sum = \n", sum)
print("Difference = \n", difference)
print("Product = \n", product)
print("Quotient = \n", quotient)

# 乘法运算符执行逐元素乘法而不是矩阵乘法。要执行矩阵乘法,需如下操作
matrix_product = a.dot(b)
print(matrix_product)

