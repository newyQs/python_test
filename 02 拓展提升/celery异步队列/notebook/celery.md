https://www.cnblogs.com/zepc007/p/14869179.html

Celery是由Python开发、简单、灵活、可靠的分布式任务队列，是一个处理异步任务的框架，其本质是生产者消费者模型，生产者发送任务到消息队列，消费者负责处理任务。Celery侧重于实时操作，但对调度支持也很好，其每天可以处理数以百万计的任务。特点：
+ 简单：熟悉celery的工作流程后，配置使用简单
+ 高可用：当任务执行失败或执行过程中发生连接中断，celery会自动尝试重新执行任务
+ 快速：一个单进程的celery每分钟可处理上百万个任务
+ 灵活：几乎celery的各个组件都可以被扩展及自定制

Celery由三部分构成：
+ 消息中间件(Broker)：官方提供了很多备选方案，支持RabbitMQ、Redis、Amazon SQS、MongoDB、Memcached 等，官方推荐RabbitMQ
+ 任务执行单元(Worker)：任务执行单元，负责从消息队列中取出任务执行，它可以启动一个或者多个，也可以启动在不同的机器节点，这就是其实现分布式的核心
+ 结果存储(Backend)：官方提供了诸多的存储方式支持：RabbitMQ、 Redis、Memcached,SQLAlchemy, Django ORM、Apache Cassandra、Elasticsearch等

![](celery.png)

工作原理：
1. 任务模块Task包含异步任务和定时任务。其中，异步任务通常在业务逻辑中被触发并发往消息队列，而定时任务由Celery Beat进程周期性地将任务发往消息队列；
2. 任务执行单元Worker实时监视消息队列获取队列中的任务执行；
3. Woker执行完任务后将结果保存在Backend中;

## django应用Celery
django框架请求/响应的过程是同步的，框架本身无法实现异步响应。但是我们在项目过程中经常会遇到一些耗时的任务, 比如：发送邮件、发送短信、大数据统计等等，这些操作耗时长，同步执行对用户体验非常不友好，那么在这种情况下就需要实现异步执行。异步执行前端一般使用ajax，后端使用Celery。

django项目应用celery，主要有两种任务方式，一是异步任务（发布者任务），一般是web请求，二是定时任务

### 异步任务redis

(1) 安装celery
```text
pip install celery
```

(2) celery.py
```python
import os
import django
from celery import Celery
from django.conf import settings


# 设置系统环境变量，安装django，必须设置，否则在启动celery时会报错
# celery_study 是当前项目名
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_demo.settings.py')
django.setup()

app = Celery('celery_demo')
app.config_from_object('django.conf.settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
```

(3) settings.py
```python
# Broker配置，使用Redis作为消息中间件
BROKER_URL = 'redis://127.0.0.1:6379/0' 

# BACKEND配置，这里使用redis
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0' 

# 结果序列化方案
CELERY_RESULT_SERIALIZER = 'json' 

# 任务结果过期时间，秒
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 

# 时区配置
CELERY_TIMEZONE='Asia/Shanghai'
```

(4) tasks.py
```python
from celery import shared_task

@shared_task
def add(x, y):
    return x + y
```

(5) views.py
```python
from celery_app.tasks import add

def index(request):
    ar = add.delay(10, 6)
    return HttpResponse(f'已经执行celery的add任务调用,task_id:{ar.id}')
```

(6) 启动celery
```text
celery worker -A celery_demo -l info
```
+ -A celery_demo：指定项目app
+ worker： 表明这是一个任务执行单元
+ -l info：指定日志输出级别

(7) 获取任务结果
views.py
```python
def get_result(request):
    task_id = request.GET.get('task_id')
    ar = result.AsyncResult(task_id)
    if ar.ready():
        return JsonResponse({"status": ar.state, "result": ar.get()})
    else:
        return JsonResponse({"status": ar.state, "result": ""})
```
AsyncResult类的常用的属性和方法：
+ state: 返回任务状态，等同status；
+ task_id: 返回任务id；
+ result: 返回任务结果，同get()方法；
+ ready(): 判断任务是否执行以及有结果，有结果为True，否则False；
+ info(): 获取任务信息，默认为结果；
+ wait(t): 等待t秒后获取结果，若任务执行完毕，则不等待直接获取结果，若任务在执行中，则wait期间一直阻塞，直到超时报错；
+ successful(): 判断任务是否成功，成功为True，否则为False；

### 定时任务

(1) settings.py
```python
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'mul_every_10_seconds': {   
        'task': 'celery_app.tasks.mul', # 任务路径
        'schedule': 10, # 每10秒执行一次
        'args': (10, 5)
    },
    'xsum_week1_20_20_00': {
        'task': 'celery_app.tasks.xsum',
        'schedule': crontab(hour=20, minute=20, day_of_week=1), # 每周一20点20分执行
        'args': ([1,2,3,4],),
    },
}
```
参数说明如下：
+ task：任务函数
+ schedule：执行频率，可以是整型（秒数），也可以是timedelta对象，也可以是crontab对象，也可以是自定义类（继承celery.schedules.schedule）
+ args：位置参数，列表或元组
+ kwargs：关键字参数，字典
+ options：可选参数，字典，任何 apply_async() 支持的参数
+ relative：默认是False，取相对于beat的开始时间；设置为True，则取设置的timedelta时间

(2) 启动celery

分别启动worker和beat
```text
celery worker -A celery_demo -l debug 
celery beat -A celery_demo -l debug
```

### 任务绑定

```python
@shared_task(bind=True)
def add(self, x, y):
    try:
        logger.info('-add' * 10)
        logger.info(f'{self.name}, id:{self.request.id}')
        raise Exception
    except Exception as e:
        # 出错每4秒尝试一次，总共尝试4次
        self.retry(exc=e, countdown=4, max_retries=4)
    return x + y
```
说明如下：
+ 在装饰器中加入参数 bind=True
+ 在task函数中的第一个参数设置为self，self对象是celery.app.task.Task的实例，可以用于实现重试等多种功能

接着我们在views.py文件中，写入如下视图函数
```python
def get_result(request):
    task_id = request.GET.get('task_id')
    ar = result.AsyncResult(task_id)
    if ar.successful():
        return JsonResponse({"status": ar.state, "result": ar.get()})
    else:
        return JsonResponse({"status": ar.state, "result": ""})
```

### 任务钩子


### 任务编排


### celery管理和监控