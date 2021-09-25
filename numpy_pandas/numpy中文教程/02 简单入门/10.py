import numpy as np

# Where
'''
where()函数是另外一个根据条件返回数组中的值的有效方法。
只需要把条件传递给它，它就会返回一个使得条件为真的元素的列表。
'''
a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(b)  # >>>(array([0, 1, 2, 3, 4]),)
print(c)  # >>>[5 6 7 8 9]
