# Scrapy入门

## 1. 本节目标
1. 创建一个Scrapy项目
2. 创建一个Spider来抓取站点和处理数据
3. 通过命令行将抓取的内容导出
4. 将抓取的内容保存到MongoDB数据库

## 2. 准备工作
最好创建一个单独的虚拟环境，安装好Scrapy库、MongoDB、PyMongo库。

## 3. 创建项目
使用如下命令在任意目录下创建一个Scrapy项目:tutorial
```
Scrapy startproject tutorial
```

## 4. 创建spider
spider是自己定义的类，Scrapy用它来从网页中抓取内容，并解析抓取的结果。

在tutorial目录下，使用如下命令创建一个spider
```
scrapy genspider quotes quotes.toscrape.com
```

## 5. 创建item
Item是保存爬取数据的容器，使用方法和字典类似。

## 6. 解析response


## 7. 使用item


## 8. 后续request


## 9. 运行
进入目录，运行如下命令：
```
scrapy crawl quotes
```

## 10. 保存到文件


## 11. 使用item pipeline

