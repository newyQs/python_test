https://www.toutiao.com/i7054798704535929358/?tt_from=weixin&utm_campaign=client_share&wxshare_count=1&timestamp=1642951296&app=news_article&utm_source=weixin&utm_medium=toutiao_android&use_new_style=1&req_id=202201232321350101511732221AFDCAE0&share_token=9e563937-6026-490e-a65b-dad1406a78f7&group_id=7054798704535929358

# Pydantic—强大的数据校验工具，比DRF的校验器还快12倍
Pydantic 是一个使用Python类型注解进行数据验证和管理的模块。安装方法非常简单，打开终端输入：
```
pip install pydantic
```
它类似于 Django DRF 序列化器的数据校验功能，不同的是，
Django里的序列化器的Field是有限制的，如果你想要使用自己的Field还需要继承并重写它的基类：
```
# Django 序列化器的一个使用例子，你可以和下面Pydantic的使用作对比
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.CharField(max_length=32)
    publish = models.CharField(max_length=32)
```
而 Pydantic 基于Python3.7以上的类型注解特性，实现了可以对任何类做数据校验的功能：
```
# Pydantic 数据校验功能
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int 
    name = 'John Doe'
    signup_ts: Optional[datetime] = None 
    friends: List[int] = []   
    
external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
    
user = User(**external_data)

print(user.id)    
print(type(user.id))
#> 123
#> <class 'int'>

print(repr(user.signup_ts))
#> datetime.datetime(2019, 6, 1, 12, 22)

print(user.friends)
#> [1, 2, 3]

print(user.dict)
"""
{
'id': 123,
'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
'friends': [1, 2, 3],
'name': 'John Doe',
}
"""
```
从上面的基本使用可以看到，它甚至能自动帮你做数据类型的转换，
比如代码中的 user.id, 在字典中是字符串，但经过Pydantic校验器后，它自动变成了int型，因为User类里的注解就是int型。

当我们的数据和定义的注解类型不一致时会报这样的Error：
```
# Pydantic 数据校验功能
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int 
    name = 'John Doe'
    signup_ts: Optional[datetime] = None 
    friends: List[int] = []   
    
external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:222', # 这里有差别
    'friends': [1, 2, '3'],
}
    
user = User(**external_data)
```
即 "invalid datetime format", 因为我传入的 signup_ts 不是标准的时间格式（多了个2）。
