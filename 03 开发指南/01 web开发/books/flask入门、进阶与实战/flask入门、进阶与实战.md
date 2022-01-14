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
···

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
app.py
```
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)  # Flask扩展一般都在创建实例时初始化，这行代码是Flask-Bootstrap的初始化方法


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
```
base.html
```
{% extends "bootstrap/base.html" %} <!-- base.html模板继承自bootstrap/base.html -->
{% block title %}Flask{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
 <div class="container">
 <div class="navbar-header">
 <button type="button" class="navbar-toggle" data-toggle="collapse" data-taget=".navbar-collapse">
 <span class="sr-only">Toggle navigation</span>
 <sapn class="icon-bar"></sapn>
 <span class="icon-bar"></span>
 <span class="icon-bar"></span>
 </button>
 <a class="navbar-brand" href="/">Flasky</a>
 </div>
 <div class="navbar=collapse collapse">
 <ul class="nav navbar-nav">
 <li>
 <a href="/">Home</a>
 </li>
 </ul>
 </div>
 </div>
</div>
{% endblock %}


{% block content %}
<div class="container">
 {% block page_content %}{% endblock %}
</div>
{% endblock %}

<!--title、navbar、content都是bootstrap/base.html中定义的块。navbar是显示导航栏，其中的代码比较多，作用是添加Flasky和Home两个链接-->
<!--以后的html页面直接继承base.html就可以了-->
```
index.html
```
{% extends "base.html" %}
{% block title %}首页{% endblock %}
{% block page_content %}
<h2>这里是首页，welcome</h2>
Technorati Tags: flask
{% endblock %}
```

### 2.3.3 自定义错误页面


## 2.4 使用Flask-Moment扩展本地化处理日期和时间


### 2.4.1 Flask-Moment基础


### 2.4.2 使用Flask-Moment显示时间
app.py
```
from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
```
404.html
```
{% extends "base.html" %}

{% block title %}Flasky - Page Not Found{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Not Found</h1>
</div>
{% endblock %}
```
500.html
```
{% extends "base.html" %}

{% block title %}Flasky - Internal Server Error{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Internal Server Error</h1>
</div>
{% endblock %}
```
base.html
```
{% extends "bootstrap/base.html" %}

{% block title %}Flasky{% endblock %}

{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
{% endblock %}

{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}

{% block content %}
<div class="container">
    {% block page_content %}{% endblock %}
</div>
{% endblock %}

{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}
```
index.html
```
{% extends "base.html" %}

{% block title %}Flask教程{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Hello World!</h1>
</div>
<p>当前时间是：{{ moment(current_time).format('LLL') }}.</p>
<p>这是{{ moment(current_time).fromNow(refresh=True) }}.</p>
{% endblock %}
```
user.html
```
{% extends "base.html" %}

{% block title %}Flask教程{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Hello World!</h1>
</div>
<p>当前时间是：{{ moment(current_time).format('LLL') }}.</p>
<p>这是{{ moment(current_time).fromNow(refresh=True) }}.</p>
{% endblock %}
```
## 2.5 静态文件

### 2.5.1 静态文件介绍


### 2.5.2 使用静态文件
app.py
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)
```
index.html
```
<html>
   <head>
      <script type = "text/javascript"
         src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
   </head>
   <body>
      <input type = "button" onclick = "sayHello()" value = "点击我啊" />
   </body>
</html>
```
## 2.6 可插拔视图

### 2.6.1 使用可插拔视图


### 2.6.2 可插拔视图实战演练
error_handlers.py
```
from flask import render_template, jsonify
from routing import app
from myexceptions import *

#错误处理程序
@app.errorhandler(404)
def unexpected_error(error):
    """ 未知错误的错误处理程序 """
    return render_template('error.html'), 404

@app.errorhandler(AuthenticationException)
def auth_error(error):
    """ 用户输入数据发生异常时的错误处理程序用 """
    return jsonify({'error': error.get_message()})
```
myexceptions.py
```
class AuthenticationException(Exception):
    """
        与身份验证相关的异常
    """
    def __init__(self, message_text):
        self.message_text = message_text

    def get_message(self):
        return self.message_text

```
routing.py
```
from flask import Flask
from views import UserView

#App配置
app= Flask(__name__)

#URLs
app.add_url_rule('/users', view_func=UserView.as_view('user_view'), methods=['GET'])

from error_handlers import *

if __name__ == '__main__':
    app.run()
```
views.py
```
from flask.views import View
from flask import render_template

from myexceptions import AuthenticationException

class ParentView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = self.get_objects()
        return self.render_template(context)

class UserView(ParentView):
    def get_template_name(self):
        raise AuthenticationException('test')
        return 'users.html'

    def get_objects(self):
        return {}
```
error.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h7>这是模板文件Error.html</h7>
</body>
</html>
```
user.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h7>这是模板文件User.html</h7>
</body>
</html>
```

# 第3章 实现表单操作


## 3.1 使用Flask-WTF扩展

### 3.1.1 Flask-WTF基础

### 3.1.2 使用Flask-WTF处理表单


## 3.2 重定向和会话处理

### 3.2.1 Flask中的重定向和会话处理

### 3.2.2 实现重定向和会话处理


## 3.3 Flash闪现提示

### 3.3.1 Flash基础

###  3.3.2 使用模板渲染flash()函数的闪现提示信息


## 3.4 文件上传

### 3.4.1 简易文件上传程序

### 3.4.2 查看上传的图片

### 3.4.3 使用Flask-WTF实现文件上传

### 3.4.4 使用Flask-Uploads扩展上传文件


## 3.5 登录验证

0### 3.5.1 验证两次密码是否相同

### 3.5.2 注册验证和登录验证
form.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    <form method="post">
        <lable>用户名：</lable><input type="text" name="username"><br>
        <lable>输入密码：</lable><input type="password" name="password"><br>
        <label>确认密码：</label><input type="password" name="password2"><br>
        <input type="submit" value="提交"><br>
    </form>
    {# 使用遍历获取闪现的消息 #}
    {% for message in get_flashed_messages() %}
        {{ message }}
    {% endfor %}

</body>
</html>
```
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>
```


# 第4章 Flask数据库操作

## 4.1 关系型数据库和非关系型数据库

### 4.1.1 关系型数据库

### 4.1.2 非关系型数据库

## 4.2 Python语言的数据库框架

### 4.2.1 程序文件

### 4.2.2 模板文件

## 4.3 使用Flask-SQLAlchemy管理数据库

### 4.3.1 Flask-SQLAlchemy基础

### 4.3.2定义模型

### 4.3.3 关系

## 4.4 使用Flask-SQLAlchemy操作数据库

### 4.4.1 新建表

### 4.4.2 添加行

### 4.4.3 修改行

### 4.4.4 删除行

### 4.4.5 查询行

### 4.4.6 在视图函数中操作数据库

### 4.4.7 使用Flask-SQLAlchemy实现一个简易的登录系统

### 4.4.8 使用Flask-SQLAlchemy实现小型BBS系统

## 4.5 将数据库操作集成到Python shell

## 4.6 使用Flask-Migrate实现数据库迁移

### 4.6.1 创建Virtualenv虚拟环境

### 4.6.2 创建迁移仓库

### 4.6.3 创建迁移脚本

### 4.6.4 更新数据库

## 4.7 使用CouchDB数据库

### 4.7.1 搭建开发环境

### 4.7.2 图书发布系统

### 4.7.3 文件上传系统

## 4.8 Virtualenv+Flask+MySQL+SQLAlchemy信息发布系统

### 4.8.1 创建Virtualenv虚拟环境

### 4.8.2 使用Flask实现数据库迁移

### 4.8.3 具体实现


## 4.9 流行电影展示系统

### 4.9.1 TheMovieDB简介

### 4.9.2 开发流程介绍

### 4.9.3 具体实现