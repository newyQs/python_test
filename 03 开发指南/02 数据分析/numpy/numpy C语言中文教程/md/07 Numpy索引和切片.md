# Numpy索引和切片

## 基本切片
NumPy 内置函数 slice() 可以用来构造切片对象，该函数需要传递三个参数值分别是 start（起始索引）、stop（终止索引） 和 step（步长），通过它可以实现从原数组的上切割出一个新数组。

示例如下：
```python
import numpy as np

a = np.arange(10)
#生成切片对象
s = slice(2,9,3)#从索引2开始到索引9停止，间隔时间为2
print(a[s])
```

也可以通过冒号来分割切片参数，最终也能获得相同结果，示例如下：
```python
import numpy as np

a = np.arange(10)
b = a[2:9:2]
print(b)
```

下面对冒号切片做简单地说明：
+ 如果仅输入一个参数，则将返回与索引相对应的元素。 对于上述示例来说[3] 就会返回 3。
+ 如果在其前面插入“:”如[:9]，则会返回 0-8 的所有数字（不包含9）。
+ 如是 [2:] 则会返回 2-9 之间的数字。
+ 如果在两个参数之间，如[2:9]，则对两个索引值之间的所有元素进行切片（不包括停止索引）。

下面对冒号类型的切片做了简单的实例演示：

示例 1：
```python
import numpy as np

a = np.arange(10)
b = a[3]
print (b)
```

示例 2：
```python
import numpy as np

a = np.arange(10)
print (a[2:])
```

示例 3：
```python
import numpy as np

a = np.arange(10)
print(a[2:5])
```

## 多维数组切片
多维数组切片操作，实例如下：
```python
import numpy as np

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
# 从[1:]索引处开始切割
print(a[1:])
```
注意：切片还可以使用省略号“…”，如果在行位置使用省略号，那么返回值将包含所有行元素，反之，则包含所有列元素。

实例演示如下：
```python
import numpy as np

#创建a数组
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
#返回数组的第二列
print (a[...,1]) 
#返回数组的第二行
print (a[1,...])
#返回第二列后的所有项
print (a[...,1:])
```
