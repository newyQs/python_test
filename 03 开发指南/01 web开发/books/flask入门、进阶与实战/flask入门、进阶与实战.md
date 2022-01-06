# 第1章 Flask Web开发基础

## 1.1 Flask框架介绍

### 1.1.1 Flask框架的基本结构

+ Werkzeug：是一个WSGI工具集，是Web应用程序和多种服务器之间的标准接口

+ Jinja2：负责渲染模板，将由HTML、CSS和JavaScript组成的模板文件显示出来

### 1.1.2 Flask和Django的对比


## 1.2 安装Flask


### 1.2.1 快速安装Flask


### 1.2.2 使用Pycharm创建虚拟环境


## 1.3 初步认识Flask Web程序


### 1.3.1 编写第一个Flask Web程序
```
import flask  # 导入flask模块

app = flask.Flask(__name__)  # 实例化类Flask，后面的构造方法Flask使用当前模块的名称（__name__）作为参数


@app.route('/')  # 装饰器操作，实现URL地址
def hello():  # 定义业务处理函数helo()
    return '你好，这是第一个Flask程序!'


if __name__ == '__main__':
    app.run()  # 运行程序
```

### 1.3.2 使用Pycharm编写第一个Flask Web程序


## 1.4 分析Flask Web程序的基本结构


### 1.4.1 运行方法run()
app.run(host=None, port=None, debug=None)
+ host
+ port
+ debug


### 1.4.2 路由处理
1. 使用路由方法rout()
    ```
    @app.route('/hello')  
    def hello_world():  
        return "hello world"
    ```
    浏览器输入：http://127.0.0.1:5000/hello 即可显示返回结果
    
2. 使用路由方法add_url_rule()
    ```
    def hello_world():  
        return "hello world"
        
    app.add_url_rule('/','hello',hello_world)
    ```
    浏览器输入：http://127.0.0.1:5000/hello 即可显示返回结果
    
3. 将不同的URL映射到同一个函数
    在访问多个不同URL请求时，都会返回由同一个函数产生的响应内容
    ```
    import flask  
                      		
    app = flask.Flask(__name__) 
         	
    @app.route('/')           			
    @app.route('/aaa')        			
    def hello():
        return '你好，这是一个Flask程序！'
        
    if __name__ == '__main__':
        app.run() 
    ```
    浏览器输入：http://127.0.0.1:5000/或者http://127.0.0.1:5000/aaa 即可显示返回结果
    
### 1.4.3 处理URL参数
在Flask Web程序中，有时候URL地址中的参数是动态的，例如下面两种格式：
```
/hello/<name>    # 获取URL "/hello/wang"中的参数"wang"给变量"name"
/hello/<int:id>  # 获取URL "/hello/5"中的参数"5"给变量"id"
/hello/<float:num>  # 获取URL "/hello/2.3"中的参数"2.3"给变量"num"
```
所以想要获取和处理URL中传递来的参数，就需要在对应的处理函数的参数列表中声明该参数：
```
from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return '你好%s!' % name

if __name__ == '__main__':
    app.run(debug = True)
```

### 1.4.4 传递HTTP请求
在计算机应用中，HTTP协议是互联网中数据通信的基础，有如下5种HTTP请求方法：
+ GET       使用未加密的形式向服务器发送数据
+ POST      向服务器发送HTML表单中的数据，服务器不会缓存POST接受的数据
+ PUT       使用上传的内容替换指定的目标资源
+ HEAD      和GET方法相同，但是没有响应体
+ DELETE    删除由URL指定的目标资源

在Flask框架中，默认使用GET方法。通过URL装饰器的参数“方法类型”，可以让同一个URL的两种请求方法都映射到同一个函数上。
```
import flask  # 导入flask模块

# 变量html_txt初始化，作为GET请求的页面
html_txt = """        					
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
app = flask.Flask(__name__)  # 实例化类Flask


# URL映射，不管是‘GET’方法还是‘POST’方法，都被映射到helo()函数
@app.route('/aaa', methods=['GET', 'POST'])
def helo():  # 定义业务处理函数helo()
    if flask.request.method == 'GET':  # 如果接收到的请求是GET
        return html_txt  # 返回html_txt的页面内容
    else:  # 否则接收到的请求是POST
        return '我司已经收到POST请求！'


if __name__ == '__main__':
    app.run()  # 运行程序
```
另外，在Flask Web程序中处理URL请求时，可以使用网页重定向方法url_for()方法来到指定的URL
```
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
### 1.4.5 模拟实现用户登录系统
index.html
```
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
```
from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return '欢迎%s' % name + '登录本系统'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('biaodan')
        return redirect(url_for('success', name=user))  # URL重定向
    else:
        user = request.args.get('biaodan')
        return redirect(url_for('success', name=user))  # URL重定向


if __name__ == '__main__':
    app.run(debug=True)
```

## 1.5 Flask-Script扩展

### 1.5.1 Flask-Script扩展介绍


### 1.5.2 使用Flask-Script扩展
```
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
```
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
```
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@manager.command  # 创建命令
def hello():
    print('大江大河！')


if __name__ == '__main__':
    manager.run()
```
```
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


# 命令既可以用-n,也可以用--name，dest="name"用户输入的命令的名字作为参数传给了函数中的name
@manager.option('-n', '--name', dest='name',
                help='Your name',
                default='world')
# 命令既可以用-u,也可以用--url,dest="url"用户输入的命令的url作为参数传给了函数中的url
@manager.option('-u', '--url', dest='url',
                default='www.csdn.com')
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


# 第2章 使用Flask模板 

## 2.1 使用Jinja2模板引擎
moban.py
```
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()

```
index.html
```
<h1>Hello World!</h1>
```
user.html
```
<h1>Hello, {{ name }}!</h1>
<h1>Hello, {{ name }}!</h1>
```

## 2.2 Jinja2模板的基本元素

### 2.2.1 变量
index.html
```
<p>一个来自字典的值:{{mydict['key']}}</p>
<p>一个来自列表的值{{mylist[2]}}</p>
<p>一个来自具有变量索引的列表的值:{{mylist[myintvar]}}</p>
<p>一个来自对象方法的值:{{myobj.get_name()}}</p>
```
app.py
```
from flask import Flask
from flask import render_template


class Myobj(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


app = Flask(__name__)


@app.route('/')
def index():
    mydict = {'key1': '123', 'key': 'hello'}
    mylist = (123, 234, 345, 789)
    myintvar = 0
    myobj = Myobj('Hyman')
    return render_template('index.html', mydict=mydict, mylist=mylist, myintvar=myintvar, myobj=myobj)


if __name__ == '__main__':
    app.run()
```

### 2.2.2 使用控制结构

index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{title | reverse | upper}}</h1>
    <br>
    {{list2 | listreverse}}
    <br>
    <ul>
        {% for item in my_list %}
        <li>{{item.id}}----{{item.value}}</li>
        {% endfor %}
    </ul>

    {% for item in my_list %}
        {% if loop.index==1 %}
            <li style="background-color: red;">{{ loop.index }}--{{ item.get('value') }}</li>
        {% elif loop.index==2 %}
            <li style="background-color: blue;">{{ loop.index }}--{{ item.get('value') }}</li>
        {% elif loop.index==3 %}
            <li style="background-color: green;">{{ loop.index }}--{{ item.get('value') }}</li>
        {% else %}
            <li style="background-color: yellow;">{{ loop.index }}--{{ item.get('value') }}</li>
        {% endif %}
    {% endfor %}
</body>
</html>
```
app.py
```
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    list1 = list(range(10))
    my_list = [{"id": 1, "value": "我爱工作"},
               {"id": 2, "value": "工作使人快乐"},
               {"id": 3, "value": "沉迷于工作无法自拔"},
               {"id": 4, "value": "日渐消瘦"},
               {"id": 5, "value": "以梦为马，越骑越傻"}]
    return render_template(
        # 渲染模板语言
        'index.html',
        title='hello world',
        list2=list1,
        my_list=my_list
    )


# step1 定义过滤器
def do_list_reverse(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li


# step2 添加自定义过滤器
app.add_template_filter(do_list_reverse, 'listreverse')

if __name__ == '__main__':
    app.run(debug=True)
```
### 2.2.3 包含页和宏
base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
        {% include 'yhead.html' %}
    {% endblock %}
</head>
<body>
    <header>{% block header %}{% endblock %}</header>
    <div>{% block content %}<p>Python大神</p>{% endblock %}</div>

    {% for item in items %}
        <li>{% block loop_item scoped %}{{ item }}{% endblock %}</li>
    {% endfor %}

    <footer>
        {% block footer %}
        <p>Python</p>
            <p>联系我们:<a href="someone@example.com">xxxxx@example.com</a> </p>
        {% endblock %}
    </footer>
</body>
</html>
```
index.html
```
{% extends 'base.html' %}
{% import 'yhong.html' as ui %}

{% block title %}{{ title_name }}{% endblock %}

{% block content %}
{% set links = [
    ('主页',url_for('.index')),
    ('产品',url_for('.service')),
    ('联系我们',url_for('.about')),
] %}

<nav>
    {% for label,link in links %}
        {% if not loop.first %}|{% endif %}
        <a href="{% if link is current_link %}#
        {% else %}
        {{ link }}
        {% endif %}
        ">{{ label }}</a>
    {% endfor %}
</nav>
    <p>{{ self.title() }}</p>
    {{ ui.input('username') }}
    {{ ui.input('password',type='password') }}
{% endblock content %}

{% block footer %}
    <hr>
    {{ super() }}
{% endblock %}
```
yhead.html
```
<meta charset="UTF-8">
<link href="{{ url_for('static',filename='site.css') }}" rel="stylesheet">
<title>{% block title %}{% endblock %}</title>
```
yhong.html
```
{# 定义宏 #}
{% macro input(name,value='',type='text',size=20) %}
    <input type="{{ type }}"
        name="{{ name }}"
        value="{{ value }}"
        size="{{ size }}"/>
{% endmacro %}
```
app.py
```
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title_name='欢迎来到主页')


@app.route('/service')
def service():
    return '产品页面'


@app.route('/about')
def about():
    return '关于我们'


@app.template_test('current_link')
def is_current_link(link):
    return link == request.path


if __name__ == '__main__':
    app.run(debug=True)
```

## 2.3 使用Flask-Bootstrap扩展

### 2.3.1 Flask-Bootstrap扩展基础


### 2.3.2 在Flask Web中使用Flask-Bootstrap扩展


### 2.3.3 自定义错误页面


## 2.4 使用Flask-Moment扩展本地化处理日期和时间


### 2.4.1 Flask-Moment基础


### 2.4.2 使用Flask-Moment显示时间


## 2.5 静态文件

### 2.5.1 静态文件介绍


### 2.5.2 使用静态文件


## 2.6 可插拔视图

### 2.6.1 使用可插拔视图


### 2.6.2 可插拔视图实战演练



