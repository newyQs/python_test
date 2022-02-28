# NumPy 字符串函数

以下函数用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作。它们基于 Python 内置库中的标准字符串函数。

![](img/NumPy%20字符串函数.png)

## 1. numpy.char.add()
numpy.char.add() 函数依次对两个数组的元素进行字符串连接。
```python
import numpy as np 
 
print ('连接两个字符串：')
print (np.char.add(['hello'],[' xyz']))
print ('\n')
 
print ('连接示例：')
print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))
```

## 2. numpy.char.multiply()
numpy.char.multiply() 函数执行多重连接。
```python
import numpy as np 
 
print (np.char.multiply('Runoob ',3))
```

## 3. numpy.char.center()
numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充。
```python
import numpy as np 
 
# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print (np.char.center('Runoob', 20,fillchar = '*'))
```

## 4. numpy.char.capitalize()
numpy.char.capitalize() 函数将字符串的第一个字母转换为大写：
```python
import numpy as np 
 
print (np.char.capitalize('runoob'))
```

## 5. numpy.char.title()
numpy.char.title() 函数将字符串的每个单词的第一个字母转换为大写：
```python
import numpy as np
 
print (np.char.title('i like runoob'))
```

## 6. numpy.char.lower()
numpy.char.lower() 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower。
```python
import numpy as np 
 
#操作数组
print (np.char.lower(['RUNOOB','GOOGLE']))
 
# 操作字符串
print (np.char.lower('RUNOOB'))
```

## 7. numpy.char.upper()
numpy.char.upper() 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper。
```python
import numpy as np 
 
#操作数组
print (np.char.upper(['runoob','google']))
 
# 操作字符串
print (np.char.upper('runoob'))
```

## 8. numpy.char.split()
numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格。
```python
import numpy as np 
 
# 分隔符默认为空格
print (np.char.split ('i like runoob?'))
# 分隔符为 .
print (np.char.split ('www.runoob.com', sep = '.'))
```

## 9. numpy.char.splitlines()
numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组。
```python
import numpy as np 
 
# 换行符 \n
print (np.char.splitlines('i\nlike runoob?')) 
print (np.char.splitlines('i\rlike runoob?'))
```

## 10. numpy.char.strip()
numpy.char.strip() 函数用于移除开头或结尾处的特定字符。
```python
import numpy as np 
 
# 移除字符串头尾的 a 字符
print (np.char.strip('ashok arunooba','a'))
 
# 移除数组元素头尾的 a 字符
print (np.char.strip(['arunooba','admin','java'],'a'))
```

## 11. numpy.char.join()
numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
```python
import numpy as np 
 
# 操作字符串
print (np.char.join(':','runoob'))
 
# 指定多个分隔符操作数组元素
print (np.char.join([':','-'],['runoob','google']))
```

## 12. numpy.char.replace()
numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串。
```python
import numpy as np 
 
print (np.char.replace ('i like runoob', 'oo', 'cc'))
```

## 13. numpy.char.encode()
numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。
```python
import numpy as np 
 
a = np.char.encode('runoob', 'cp500') 
print (a)
```

## 14. numpy.char.decode()
numpy.char.decode() 函数对编码的元素进行 str.decode() 解码。
```python
import numpy as np 
 
a = np.char.encode('runoob', 'cp500') 
print (a)
print (np.char.decode(a,'cp500'))
```