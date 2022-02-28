# NumPy ndarray对象
NumPy 定义了一个 **n 维数组对象**，简称 **ndarray 对象**，该对象具有以下特点：
1. ndarray对象是一个一系列相同类型元素组成的数组集合；（内部元素类型相同）
2. ndarray对象中的每个元素都占有大小相同的内存块；（每个元素所占的内存空间相同）
3. ndarray对象可以使用索引或切片的方式获取数组中的每个元素；（通过切片或索引方式获取数组中元素）
4. ndarray对象有一个 dtype 属性，该属性用来描述元素的数据类型；
5. ndarray对象采用了数组的索引机制，将数组中的每个元素映射到内存块上，
   并且按照一定的布局对内存块进行排列，常用的布局方式有两种，即**按行**或者**按列**。

## 创建ndarray对象
通过 NumPy 的内置函数 array() 可以创建 ndarray 对象，其语法格式如下：
```
numpy.array(object, dtype=None, copy=True, order=None, ndmin=0)
```
参数说明如下：
+ object：表示一个数组序列。
+ dtype：可选参数，通过它可以更改数组的数据类型。
+ copy：可选参数，表示数组能否被复制，默认是 True。
+ order：以哪种内存布局创建数组，有 3 个可选值，分别是 C(行序列)/F(列序列)/A(默认)。
+ ndmin：用于指定数组的维度。

1. 创建一维数组
```python
import numpy

#使用列表构建一维数组
a=numpy.array([1,2,3])
print(a) # [1 2 3]

# ndarray数组类型
print(type(a)) # <class 'numpy.ndarray'>
```

2. 创建多维数组
```python
import numpy

b=numpy.array([[1,2,3],[4,5,6]])
print(b)
```

3. 改变数组数据类型
```python
import numpy

c=numpy.array([2,4,6,8],dtype="complex")
print(c)
```

## ndim查看数组维数
通过 ndim 可以查看数组的维度：
```python
import numpy as np 

arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]]) 
print(arr.ndim) 
```

使用 ndmin 参数创建不同维度的数组：
```python
import numpy as np

a = np.array([1, 2, 3,4,5], ndmin = 2)
print(a)
```

## reshape数组变维
数组的形状指的是多维数组的行数和列数。

reshape() 函数接受一个元组作为参数，用于指定了新数组的行数和列数。
```python
import numpy as np 

e = np.array([[1,2],[3,4],[5,6]]) 
print("原数组",e) 
e=e.reshape(2,3) 
print("新数组",e)  
```
