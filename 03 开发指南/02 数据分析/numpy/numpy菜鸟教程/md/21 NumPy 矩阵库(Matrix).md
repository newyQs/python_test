# NumPy 矩阵库(Matrix)
NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。

一个 的矩阵是一个由行（row）列（column）元素排列成的矩形阵列。

矩阵里的元素可以是数字、符号或数学式。

## 转置矩阵
NumPy 中除了可以使用 numpy.transpose 函数来对换数组的维度，还可以使用 T 属性。。

例如有个 m 行 n 列的矩阵，使用 t() 函数就能转换为 n 行 m 列的矩阵。

![](img/转置矩阵1.gif)

![](img/转置矩阵2.svg)


## matlib.empty()
matlib.empty() 函数返回一个新的矩阵，语法格式为：
```
numpy.matlib.empty(shape, dtype, order)
```
参数说明：
+ shape: 定义新矩阵形状的整数或整数元组
+ Dtype: 可选，数据类型
+ order: C（行序优先） 或者 F（列序优先）
```python
import numpy.matlib 
import numpy as np
 
print (np.matlib.empty((2,2)))
# 填充为随机数据
```
## numpy.matlib.zeros()
numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵。
```python
import numpy.matlib 
import numpy as np 
 
print (np.matlib.zeros((2,2)))
```

## numpy.matlib.ones()
numpy.matlib.ones()函数创建一个以 1 填充的矩阵。
```python
import numpy.matlib 
import numpy as np 
 
print (np.matlib.ones((2,2)))
```

## numpy.matlib.eye()
numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
```
numpy.matlib.eye(n, M,k, dtype)
```
参数说明：
+ n: 返回矩阵的行数
+ M: 返回矩阵的列数，默认为 n
+ k: 对角线的索引
+ dtype: 数据类型
```python
import numpy.matlib 
import numpy as np 
 
print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))
```
## numpy.matlib.identity()
numpy.matlib.identity() 函数返回给定大小的单位矩阵。

单位矩阵是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为 1，除此以外全都为 0。

![](img/单位矩阵.png)

```python
import numpy.matlib 
import numpy as np 
 
# 大小为 5，类型位浮点型
print (np.matlib.identity(5, dtype =  float))
```

## numpy.matlib.rand()
numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
```python
import numpy.matlib 
import numpy as np 
 
print (np.matlib.rand(3,3))
```
矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。
```python
import numpy.matlib 
import numpy as np  
 
i = np.matrix('1,2;3,4')  
print (i)
```

```python
import numpy.matlib 
import numpy as np  
 
j = np.asarray(i)  
print (j)
```

```python
import numpy.matlib 
import numpy as np  
 
k = np.asmatrix (j)  
print (k)
```
