# 第2章 使用Flask模板 
在Flask Web程序中，通过业务逻辑函数得到数据后，接下来需要根据这些数据生产HTTP响应（HTML文件或者json数据）。

官方文档：https://jinja.palletsprojects.com/en/3.0.x/

## 2.1 使用Jinja2模板引擎
app.py
```python
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
```python
from flask import Flask
from flask import render_template

app = Flask(__name__)

class Myobj(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

@app.route('/')
def index():
    mydict = {'key1': '123', 'key': 'hello'}
    mylist = (123, 234, 345, 789)
    myintvar = 0
    myobj = Myobj('Hyman') # 可以识别出各种数据类型
    return render_template('index.html', mydict=mydict, mylist=mylist, myintvar=myintvar, myobj=myobj)


if __name__ == '__main__':
    app.run()
```
Jinja2模板中的过滤器：
1. safe：在渲染变量值时不进行转义
2. capitalize：把变量值的首字母转换成大写，将其他字母转换成小写
3. lower：把变量值全部转换成小写
4. upper：把变量值全部转换成大写
5. title：把所有变量值中的每个单词的首字母都转换成大写
6. trim：删除变量值中的首、尾空格
7. striptags：在渲染前删除变量值中所有的HTML标签

完整的过滤器列表在Jinja2官方文档（http://jinja.pocoo.org/docs/templates/#builtin-filters）中查看

https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters

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
```python
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
```python
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
使用`pip install flask-bootstrap`安装

### 2.3.2 在Flask Web中使用Flask-Bootstrap扩展
app.py
```python
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
功能是将日期处理类库moment.js集成到Jinja2模板中。

使用pip install flask-moment

### 2.4.1 Flask-Moment基础
Moment.js是一个轻量级的JavaScript日期处理类库。开发者可以在浏览器和NodeJS中运行，通过该类库可以实现如下功能：
+ 将指定的任意日期转换成多种不同的显示格式；
+ 实现常用的日期计算功能，例如在两个日期之间相差多少天；
+ 内置了能够显示各种日期格式的函数；
+ 支持多语言，开发者可以选择或者新增一种语言包；

### 2.4.2 使用Flask-Moment显示时间
app.py
```python
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
```python
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
可插拔视图的含义是，可以在一个文件中编写多个功能类，每一个功能类对应显示一个视图功能。

### 2.6.1 使用可插拔视图
可插拔视图的灵感来自于Django框架中的通用视图，其基本原理是使用类来代替函数。

### 2.6.2 可插拔视图实战演练
error_handlers.py
```python
from flask import render_template, jsonify
from routing import app
from my_exceptions import *

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
my_exceptions.py
```python
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
```python
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
```python
from flask.views import View
from flask import render_template
from my_exceptions import AuthenticationException

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