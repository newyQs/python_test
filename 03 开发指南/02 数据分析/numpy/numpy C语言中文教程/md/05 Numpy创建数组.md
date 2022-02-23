# Numpy创建数组

## numpy.empty()
numpy.empty() 创建未初始化的数组，可以指定创建数组的形状（shape）和数据类型（dtype），语法格式如下：
```
numpy.empty(shape, dtype = float, order = 'C')
```
它接受以下参数：
+ shape：指定数组的形状；
+ dtype：数组元素的数据类型，默认值是值 float；
+ order：指数组元素在计算机内存中的储存顺序，默认顺序是“C”(行优先顺序)。

```python
import numpy as np 

arr = np.empty((3,2), dtype = int) 
print(arr) 
```
可以看到，numpy.empty() 返回的数组带有随机值，但这些数值并没有实际意义。切记 empty 并非创建空数组。

## numpy.zeros()
该函数用来创建元素均为 0 的数组，同时还可以指定被数组的形状，语法格式如下：
```
numpy. zeros(shape, dtype=float, order="C")
```
参数如下：
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