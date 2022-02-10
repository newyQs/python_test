# Scrapy框架介绍
上一章介绍了pyspider框架的用法，缺点是可配置化程度不高，异常处理能力有限等，对于一些反爬程度高的网站的爬取显得力不从心。

Scrapy是一个基于Twisted的异步处理框架，纯python实现的，架构清晰，模块之间耦合度低，可扩展性强，可以完成各种需求。

## 1.架构介绍
![](img/Scrapy架构.jpg)
+ Engine:引擎
+ Item：项目
+ Scheduler：调度器
+ Downloader：下载器
+ Spiders：蜘蛛
+ Item Pipeline：项目管道
+ Download Middlewares：下载器中间件
+ Spider Middlewares：蜘蛛中间件

## 2. 数据流
Scrapy中的数据流由引擎控制，数据流的过程如下：
1. 


## 3. 项目结构
```
scrapy.cfg
project/
    __init__.py
    items.py
    pipelines.py
    settings.py
    middlewares.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...
```
各个文件功能的描述如下：
+ scrapy.cfg
+ items.py
+ pipelines.py
+ settings.py
+ middlewares.py
+ spiders