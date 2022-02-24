# Numpy创建数组

## 1. numpy.array()


## 2. numpy.empty()
numpy.empty() 创建未初始化的数组，可以指定创建数组的形状（shape）和数据类型（dtype），语法格式如下：
```
numpy.empty(shape, dtype=float, order='C')
```
参数说明如下：
+ shape：指定数组的形状；
+ dtype：数组元素的数据类型，默认值是值 float；
+ order：指数组元素在计算机内存中的储存顺序，默认顺序是“C”(行优先顺序)。

```python
import numpy as np 

arr = np.empty((3,2), dtype = int) 
print(arr) 
```
可以看到，numpy.empty() 返回的数组带有随机值，但这些数值并没有实际意义。切记 empty 并非创建空数组。

## 3. numpy.zeros()
该函数用来创建元素均为 0 的数组，同时还可以指定被数组的形状，语法格式如下：
```
numpy. zeros(shape, dtype=float, order="C")
```
参数说明如下：
+ shape：指定数组的形状大小。
+ dtype：可选项，数组的数据类型
+ order：“C”代表以行顺序存储，“F”则表示以列顺序存储

```python
import numpy as np

#默认数据类型为浮点数
a=np.zeros(6)
print(a)
b=np.zeros(6,dtype="complex64" )
print(b)
```

也可以使用自定义的数据类型创建数组，如下所示：
```python
import numpy as np

c = np.zeros((3,3), dtype = [('x', 'i4'), ('y', 'i4')]) 
print(c)
```

## 4. numpy.ones()
返回指定形状大小与数据类型的新数组，并且新数组中每项元素均用 1 填充，语法格式如下：
```
numpy.ones(shape, dtype=None, order='C')
```
示例如下：
```python
import numpy as np 

arr = np.ones((3,2), dtype = int) 
print(arr)  
```

## 5. numpy.asarray()
asarray() 与 array() 类似，但是它比 array() 更为简单。asarray() 能够将一个 Python 序列转化为 ndarray 对象，语法格式如下：
```
numpy.asarray（sequence，dtype=None ，order=None）
```
参数说明如下：
+ sequence：接受一个 Python 序列，可以是列表或者元组；
+ dtype：可选参数，数组的数据类型；
+ order：数组内存布局样式，可以设置为 C 或者 F，默认是 C。

示例 1，将列表转化为 numpy 数组：
```python
import numpy as np 

a = np.asarray([1,2,3,4,5,6,7] )
print(a) 
print(type(a)) 
```

示例 2，使用元组创建 numpy 数组：
```python
import numpy as np 

a = np.asarray((1,2,3,4,5,6,7))
print(a) 
print(type(a))  
```

示例 3，使用嵌套列表创建多维数组：
```python
import numpy as np 

a = np.asarray([[1,2,3,4,5,6,7],[8,9]] )
print(a) 
print(type(a))
```

## 6. numpy.frombuffer()
表示使用指定的缓冲区创建数组，语法格式如下：
```
numpy.frombuffer(buffer, dtype=float, count=-1, offset=0)
```
参数说明如下：
+ buffer：将任意对象转换为流的形式读入缓冲区；
+ dtype：返回数组的数据类型，默认是 float32；
+ count：要读取的数据数量，默认为 -1 表示读取所有数据；
+ offset：读取数据的起始位置，默认为 0。

示例如下：
```python
import numpy as np 

#字节串类型
l = b'hello world' 
print(type(l)) 
a = np.frombuffer(l, dtype = "S1") 
print(a) 
print(type(a)) 
```

## 7. numpy.fromiter()
该方法可以把迭代对象转换为 ndarray 数组，其返回值是一个一维数组：
```
numpy.fromiter(iterable, dtype, count = -1)
```
参数说明如下：
+ iterable：可迭代对象。
+ dtype：返回数组的数据类型。
+ count：读取的数据数量，默认为 -1，读取所有数据。

使用内置 range() 函数创建列表对象，然后使用迭代器创建 ndarray 对象，代码如下：
```python
import numpy as np

# 使用 range 函数创建列表对象 
lis=range(6)
#生成可迭代对象i
i=iter(lis)
#使用i迭代器，通过fromiter方法创建ndarray
array=np.fromiter(i, dtype=float)
print(array)
```
