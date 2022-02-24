# NumPy创建区间数组
所谓区间数组，是指数组元素的取值位于某个范围内，并且数组元素之间可能会呈现某种规律，比如等比数列、递增、递减等。

## 1. numpy.arange()
在 NumPy 中，您可以使用 arange() 来创建给定数值范围的数组，语法格式如下：
```
numpy.arange(start, stop, step, dtype)
```
参数说明以下：
+ start：起始值，默认是 0。
+ stop：终止值，注意生成的数组元素值不包含终止值。
+ step：步长，默认为 1。
+ dtype：可选参数，指定 ndarray 数组的数据类型。

根据start与stop指定的范围以及step步长值，生成一个 ndarray 数组，示例如下。
```python
import numpy as np

x = np.arange(8) 
print (x)
```

设置 start 、stop 值以及步长，最终输出 0-10 中的奇数：
```python
import numpy as np

x = np.arange(1,10,2) 
print (x)
```

## 2. numpy.linspace()
表示在指定的数值区间内，返回均匀间隔的一维**等差**数组，默认均分 50 份，语法格式如下：
```
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
```
参数说明如下：
+ start：代表数值区间的起始值；
+ stop：代表数值区间的终止值；
+ num：表示数值区间内要生成多少个均匀的样本。默认值为 50；
+ endpoint：默认为 True，表示数列包含 stop 终止值，反之不包含；
+ retstep：默认为 True，表示生成的数组中会显示公差项，反之不显示；
+ dtype：代表数组元素值的数据类型。

示例如下：
```python
import numpy as np

#生成10个样本
a = np.linspace(1,10,10)
print(a)
```

下面示例是 endpoint 为 Fasle 时，此时不包含终止值：
```python
import numpy as np 

arr = np.linspace(10, 20, 5, endpoint = False) 
print("数组数值范围 ：",arr)  
```

retstep 参数使用示例如下：
```python
import numpy as np

x = np.linspace(1,2,5, retstep = True)
print(x) 
```

## 3. numpy.logspace
该函数同样返回一个 ndarray 数组，它用于创建**等比**数组，语法格式如下：
```
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
```
其中 base 代表对数函数的底数，默认为 10，参数详细说明见下表：
+ start：序列的起始值：base**start。
+ stop：序列的终止值：base**stop。
+ num：数值范围区间内样本数量，默认为 50。
+ endpoint：默认为 True 包含终止值，反之不包含。
+ base：对数函数的 log 底数，默认为10。
+ dtype：可选参数，指定 ndarray 数组的数据类型。

使用示例如下：
```python
import numpy as np

a = np.logspace(1.0,2.0, num = 10)
print (a)
```

下面是 base=2 的对数函数，示例如下：
```python
import numpy as np

a = np.logspace(1,10,num = 10, base = 2)
print(a)
```
