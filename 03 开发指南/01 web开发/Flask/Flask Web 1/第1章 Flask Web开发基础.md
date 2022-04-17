# 第1章 Flask Web开发基础
Flask的设计目标是实现一个**WSGI**的微框架，其核心代码十分简单，并且具有扩展性。

## 1.1 Flask框架介绍

### 1.1.1 Flask框架的基本结构
+ Werkzeug：是一个WSGI工具集，是Web应用程序和多种服务器之间的标准接口;
+ Jinja2：负责渲染模板，将由HTML、CSS和JavaScript组成的模板文件显示出来;

### 1.1.2 Flask和Django的对比
1. Flask框架诞生于2010年，其最大优点是简单易学，而Django诞生于2006年，是一个非常成熟的框架，难学一点；
2. Flask框架面向于中小型企业级项目，而Django面向于大型企业级项目；
3. Django使用开箱即用的ORM实现数据库处理，而Flask需要额外选择如何存储项目中的数据；

## 1.2 安装Flask

### 1.2.1 快速安装Flask
1. 使用pip install flask安装；
2. 下载源码包，然后使用python setup.py install ,并且需要安装2个依赖：Jinja2 和 werkzeug；

### 1.2.2 使用Pycharm创建虚拟环境
···

## 1.3 初步认识Flask Web程序

### 1.3.1 编写第一个Flask Web程序
```python
import flask 

app = flask.Flask(__name__)  # 实例化类Flask，后面的构造方法Flask使用当前模块的名称（__name__）作为参数


@app.route('/')  # 该装饰器将URL和函数hello()联系起来，使得服务器收到对应的请求时，调用该函数，返回这个函数产生的数据
def hello():  # 定义业务处理函数hello()
    return '你好，这是第一个Flask程序!'


if __name__ == '__main__':
    app.run()  
```
使用命令：`python flask.py` 启动该程序

### 1.3.2 使用Pycharm编写第一个Flask Web程序
···

## 1.4 分析Flask Web程序的基本结构

### 1.4.1 运行方法run()
app.run(host=None, port=None, debug=None)

参数:
+ host：IP地址，默认localhost 或者 127.0.0.1
+ port：端口号，默认5000
+ debug：是否显示调试信息，默认为False，建议设置成True

### 1.4.2 路由处理
在当前Web开发领域，主流的第三方框架使用路由技术来实现URL访问导航的功能。

在Flask框架中，在客户端浏览器把访问请求发送给Web服务器，Web服务器再把请求发送给Flask Web程序。
1. 使用路由方法：route(rule, endpoint, **options)
```python
import flask  
                        
app = flask.Flask(__name__) 

@app.route('/hello')  
def hello_world():  
    return "hello world"
```
浏览器输入：`http://127.0.0.1:5000/hello` 即可显示返回结果
    
2. 使用路由方法：add_url_rule(rule, endpoint=None, view_func=None, provide_automatic_options=None, **options)

```python
import flask  
                        
app = flask.Flask(__name__) 

def hello_world():  
    return "hello world"
    
app.add_url_rule('/','hello',hello_world)
```
浏览器输入：`http://127.0.0.1:5000/hello` 即可显示返回结果
    
3. 将不同的URL映射到同一个函数

目的是在访问多个不同URL请求时，都会返回由同一个函数产生的响应内容
```python
import flask  
                        
app = flask.Flask(__name__) 
        
@app.route('/')           			
@app.route('/aaa')        			
def hello():
    return '你好，这是一个Flask程序！'
    
if __name__ == '__main__':
    app.run() 
```
浏览器输入：`http://127.0.0.1:5000/` 或 `http://127.0.0.1:5000/aaa` 即可显示返回结果
    
### 1.4.3 处理URL参数
在Flask Web程序中，有时候URL地址中的参数是动态的，例如下面3种格式：
```python
/hello/<name>    # 获取URL "/hello/wang"中的参数"wang"给变量"name"
/hello/<int:id>  # 获取URL "/hello/5"中的参数"5"给变量"id"
/hello/<float:num>  # 获取URL "/hello/2.3"中的参数"2.3"给变量"num"
```

所以想要获取和处理URL中传递来的参数，就需要在对应的处理函数的参数列表中声明该参数：
```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return '你好%s!' % name

@app.route('/blog/<int:mid>')
def show_blog(mid):
   return '我的年龄是：%d' % mid + '岁！'

@app.route('/rev/<float:no>')
def revision(no):
   return '我身上只有%f' % no + '元钱了！'

if __name__ == '__main__':
   app.run()
```

### 1.4.4 传递HTTP请求
在计算机应用中，HTTP协议是互联网中数据通信的基础，主要有如下5种HTTP请求方法：
+ GET       使用未加密的形式向服务器发送数据
+ POST      向服务器发送HTML表单中的数据，服务器不会缓存POST接受的数据
+ PUT       使用上传的内容替换指定的目标资源
+ HEAD      和GET方法相同，但是没有响应体
+ DELETE    删除由URL指定的目标资源

其他的方法呢？

在Flask框架中，默认使用GET方法，通过URL装饰器的参数“methods”，可以让同一个URL的多种请求方法都映射到同一个函数上。
```python
import flask

app = flask.Flask(__name__)

# 变量html初始化，作为GET请求的页面
html = """        					
<!DOCTYPE html>
<html>
    <body>
        <h2>如果收到了GET请求</h2>
        <form method='post'>       		#设置请求方法是“post”
            <input type='submit' value='按下我发送POST请求' />
        </form>
    </body>
</html>
"""

# URL映射，不管是‘GET’方法还是‘POST’方法，都被映射到hello()函数
@app.route('/aaa', methods=['GET', 'POST'])
def hello():  
    if flask.request.method == 'GET': 
        return html  
    else:  
        return '我司已经收到POST请求！'

if __name__ == '__main__':
    app.run()  
```

另外，在Flask Web程序中处理URL请求时，可以使用网页重定向方法url_for()跳转到指定的URL：
```python
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return '你好管理员！'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return '你好%s ，你是游客！' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
```
url_for(endpoint,**values)
+ endpoint：表示要传递的函数名;
+ values：表示传递给函数的关键字参数；

### 1.4.5 模拟实现用户登录系统
index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
   <body>
      <form action = "http://localhost:5000/login" method = "post">
         <p>请输入名字:</p>
         <p><input type = "text" name = "biaodan" /></p>
         <p><input type = "submit" value = "登录" /></p>
      </form>
   </body>
</html>
```
login.py
```python
from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return '欢迎%s' % name + '登录本系统'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('biaodan') # 获取标签中name=biaodan的值
        return redirect(url_for('success', name=user))  # URL重定向
    else:
        user = request.args.get('biaodan')
        return redirect(url_for('success', name=user))  # URL重定向


if __name__ == '__main__':
    app.run(debug=True)
```

## 1.5 Flask-Script扩展
Flask被设计成可扩展形式，因此没有内置的数据库操作和用户认证。

### 1.5.1 Flask-Script扩展介绍
Flask-Script主要为Flask Web应用程序提供一个命令行解释器。

使用pip install flask-script安装。

### 1.5.2 使用Flask-Script扩展
```python
from flask import Flask
from flask_script import Manager  # 引用扩展

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    manager.run()
```

### 1.5.3 创建命令
```python
from flask import Flask
from flask_script import Manager, Server
from flask_script import Command

app = Flask(__name__)

manager = Manager(app)


class Hello(Command):
    def run(self):
        print('大江大河！')


manager.add_command('hello', Hello())  # 自定义命令hello
manager.add_command("runserver", Server())  # 自定义命令runserver

if __name__ == '__main__':
    manager.run()
```
上述代码中，类Command创建了两条自定义命令：
+ hello：运行此命令可以调用函数Hello()
+ runserver：调用函数Server()

```python
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@manager.command  
def hello():
    print('大江大河！')


if __name__ == '__main__':
    manager.run()
```

```python
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


# 命令既可以用-n,也可以用--name，dest="name"用户输入的命令的名字作为参数传给了函数中的name
@manager.option('-n', '--name', dest='name',help='Your name',default='world')               
# 命令既可以用-u,也可以用--url,dest="url"用户输入的命令的url作为参数传给了函数中的url
@manager.option('-u', '--url', dest='url',default='www.csdn.com')             
def hello(name, url):
    print('hello', name)
    print(url)


if __name__ == '__main__':
    manager.run()
```

## 1.6 系统配置

### 1.6.1 基础配置


### 1.6.2 使用配置信息


### 1.6.3 实例文件夹
