# Scrapy入门

## 1. 本节目标
1. 创建一个Scrapy项目
2. 创建一个Spider来抓取站点和处理数据
3. 通过命令行将抓取的内容导出
4. 将抓取的内容保存到MongoDB数据库

## 2. 准备工作
创建一个单独的虚拟环境，安装好Scrapy、MongoDB、PyMongo库

## 3. 创建项目
使用如下命令在任意目录下创建一个Scrapy项目:tutorial
```
Scrapy startproject tutorial
```

## 4. 创建spider
spider是自己定义的类，Scrapy用它来从网页中抓取内容，并解析抓取的结果。

进入刚才创建的tutorial文件夹，然后执行genspider命令。第一个参数是Spider的名称，第二个参数是网站域名。
```
cd tutorial
scrapy genspider quotes quotes.toscrape.com
```

quotes.py
```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name="quotes"
    allowed_domains=["quotes.toscrape.com"]
    start_urls=["http://quotes.toscrape.com/"]
    
    def parse(self, response, **kwargs):
        pass
```
name，它是每个项目唯一的名字，用来区分不同的Spider
allowed_domains，它是允许爬取的域名，如果初始和后续的请求链接不是这个域名下的，则请求链接会被过滤掉
start_urls，它包含了Spider在启动时爬取的url列表，初始请求是由它来定义的
parse，它是Spider的一个方法，在默认情况下，被调用时start_urls里面的链接构成的请求完成下载执行后，返回的响应就会作为唯一的参数传递给这个函数。该方法负责解析返回的响应、提取数据或者进一步生成要处理的请求。


## 5. 创建item
Item是保存爬取数据的容器，使用方法和字典类似。

items.py
```python
import scrapy

class QuoteItem(scrapy.Item):
    text=scrapy.Field()
    author=scrapy.Field()
    tags=scrapy.Field()
```

## 6. 解析response

改写parse方法
```python
def parse(self, response, **kwargs):
    quotes=response.css(".quote")
    for quote in quotes:
        text=quote.css(".text::text").extract_first()
        author=quote.css(".author::text").extract_first()
        tags=quote.css(".tags .tag::text").extract()
```

## 7. 使用item

改写QuotesSpider类
```python
import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name="quotes"
    allowed_domains=["quotes.toscrape.com"]
    start_urls=["http://quotes.toscrape.com/"]
    
    def parse(self, response, **kwargs):
        quotes=response.css(".quote")
        for quote in quotes:
            item=QuoteItem()
            item["text"]=quote.css(".text::text").extract_first()
            item["author"]=quote.css(".author::text").extract_first()
            item["tags"]=quote.css(".tags .tag::text").extract()
            yield item

```
## 8. 后续request

前面操作实现了从初始页面抓取内容。那么，下一页的内容该如何抓取？

```python
import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name="quotes"
    allowed_domains=["quotes.toscrape.com"]
    start_urls=["http://quotes.toscrape.com/"]
    
    def parse(self, response, **kwargs):
        quotes=response.css(".quote")
        for quote in quotes:
            item=QuoteItem()
            item["text"]=quote.css(".text::text").extract_first()
            item["author"]=quote.css(".author::text").extract_first()
            item["tags"]=quote.css(".tags .tag::text").extract()
            yield item
        
        next=response.css(".pager .next a::attr('href')").extract_first()
        url=response.urljoin(next)
        yield scrapy.Request(url=url,callback=self.parse)
```


## 9. 运行
进入目录，运行如下命令：
```
scrapy crawl quotes
```

## 10. 保存到文件

保存成JSON文件
```text
scrapy crawl quotes -o quotes.json
```
```text
scrapy crawl quotes -o quotes.jl
```
```text
scrapy crawl quotes -o quotes.jsonlines
```

输出其他格式：
```text
scrapy crawl quotes -o quotes.csv
scrapy crawl quotes -o quotes.xml
scrapy crawl quotes -o quotes.pickle
scrapy crawl quotes -o quotes.marshal
scrapy crawl quotes -o ftp://user:pass@ftp/example.com/path/to/quotes.csv

```


## 11. 使用item pipeline

