# 元组是（不可变的）有序值列表。
# 元组在很多方面类似于列表; 其中一个最重要的区别是元组可以用作字典中的键和集合的元素，而列表则不能

d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)  # Create a tuple
print(type(t))  # Prints "<class 'tuple'>"
print(d[t])  # Prints "5"
print(d[(1, 2)])  # Prints "1"
