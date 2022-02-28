# NumPy数组属性

## ndarray.shape
shape 属性的返回值一个由数组维度构成的元组，比如 2 行 3 列的二维数组可以表示为(2,3)，该属性可以用来调整数组维度的大小。
```python
import numpy as np

a = np.array([[2,4,6],[3,5,7]])
print(a.shape)
```

通过 shape 属性修改数组的形状大小： 
```python
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)
```

## ndarray.reshape()
NumPy 还提供了一个调整数组形状的 reshape() 函数。
```python
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)
```

## ndarray.ndim
该属性返回的是数组的维数，示例如下：
```python
import numpy as np

#随机生成一个一维数组
c = np.arange(24)
print(c)
print(c.ndim)

#对数组进行变维操作
e = c.reshape(2,4,3)
print(e) 
print(e.ndim)
```

## ndarray.itemsize
返回数组中每个元素的大小（以字节为单位），示例如下：
```python
import numpy as np

#数据类型为int8，代表1字节
x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize)
```

## ndarray.flags
返回 ndarray 数组的内存信息，比如 ndarray 数组的存储方式，以及是否是其他数组的副本等。
```python
import numpy as np

x = np.array([1,2,3,4,5])
print (x.flags)
```
