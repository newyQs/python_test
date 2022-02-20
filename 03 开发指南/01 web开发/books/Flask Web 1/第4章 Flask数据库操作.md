# 第4章 Flask数据库操作

## 4.1 关系型数据库和非关系型数据库

### 4.1.1 关系型数据库

### 4.1.2 非关系型数据库
非关系型数据库简称NoSQL。主要有Redis，MongoDB和Neo4j等。
1. 高性能并发读写
2. 快速访问
3. 面向可扩展型的分布式数据库

## 4.2 Python语言的数据库框架

### 4.2.1 程序文件
app.py
```python
# -*- encoding:utf-8 -*-
import os
import flask
from flask import g, request, render_template, session, redirect, url_for
from sqlite3 import connect

DBNAME = 'test.db'

app = flask.Flask(__name__)
app.secret_key = 'dfadff#$#5dgfddgssgfgsfgr4$T^%^'


@app.before_request
def before_request():
    g.db = connect(DBNAME)


@app.teardown_request
def teardown_request(e):
    db = getattr(g, 'db', None)
    if db:
        db.close()
    g.db.close()


@app.route('/')
def index():
    if 'username' in session:
        return "你好，" + session['username'] + '<p><a href="/logout">注销</a></p>'
    else:
        return '<a href="/login">登录</a>,<a href="/signup">注册</a>'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        name = 'name' in request.form and request.form['name']
        passwd = 'passwd' in request.form and request.form['passwd']
        if name and passwd:
            cur = g.db.cursor()
            cur.execute('insert into user (name,passwd) values (?,?)', (name, passwd))
            cur.connection.commit()
            cur.close()
            session['username'] = name
            return redirect(url_for('index'))
        else:
            return redirect(url_for('signup'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = 'name' in request.form and request.form['name']
        passwd = 'passwd' in request.form and request.form['passwd']
        if name and passwd:
            cur = g.db.cursor()
            cur.execute('select * from user where name=?', (name,))
            res = cur.fetchone()
            if res and res[1] == passwd:
                session['username'] = name
                return redirect(url_for('index'))
            else:
                return '登录失败!'
        else:
            return '参数不全!'


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


def init_db():
    if not os.path.exists(DBNAME):
        cur = connect(DBNAME).cursor()
        cur.execute('create table user (name text,passwd text)')
        cur.connection.commit()
        print('数据库初始化完成!')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

login.html
```html
<!DOCTYPE html>
<html>
    <body>
        <form method='post'>
        <input type='text' name='name' placeholder='用户名' />
        <input type='password' name='passwd' placeholder='密码' />
        <input type='submit' value='登录' />
        </form>
    </body>
</html>
```

signup.html
```html
<!DOCTYPE html>
<html>
    <body>
        <form method='post'>
        <input type='text' name='name' placeholder='用户名' />
        <input type='password' name='passwd' placeholder='密码' />
        <input type='submit' value='注册' />
        </form>
    </body>
</html>
```
### 4.2.2 模板文件

## 4.3 使用Flask-SQLAlchemy管理数据库
Flask-SQLAlchemy是一个功能强大的关系型数据库框架，不但提供了高层ORM功能，而且也提供了使用数据库原生SQL的底层功能。

### 4.3.1 Flask-SQLAlchemy基础
使用pip install flask-sqlalchemy安装。

在使用Flask-SQLAlchemy扩展时，需要使用URL设置要操作的数据库，语法如下：
```
MySQL
mysql://username:password@hostname/database

Postgres
postgres://username:password@hostname/database

SQLite(Unix)
sqlite:////absolute/path/to/database

SQLite(Windows)
sqlite:///c:/absolute/path/to/database
```

### 4.3.2定义模型
在软件开发领域中，将在程序中使用的持久化实体称为模型。
在Python的ORM中，一个模型对应一个Python类，类中的各个属性分别对应数据库表中的列，这一点和Django框架中的Models相似。
假如在程序中需要用到2个数据库表user和rank，那么可以在Python程序中定义模型Rank和User
```

```

### 4.3.3 关系


## 4.4 使用Flask-SQLAlchemy操作数据库

### 4.4.1 新建表
在Flask-SQLAlchemy中，可以通过方法db.create_all()根据模型类创建数据库。

db_create_all()和db_drop_all()

### 4.4.2 添加行

### 4.4.3 修改行

### 4.4.4 删除行

### 4.4.5 查询行

### 4.4.6 在视图函数中操作数据库

### 4.4.7 使用Flask-SQLAlchemy实现一个简易的登录系统
app.py
```python
import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(FlaskForm):
    name = StringField('请输入名字?', validators=[Required()])
    submit = SubmitField('提交')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('看来你改了名字!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    db.create_all()
    manager.run()
```


### 4.4.8 使用Flask-SQLAlchemy实现小型BBS系统
app.py
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:66688888@localhost/bloguser"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'b_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), unique=True)
    content = db.Column(db.String(100))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Category %r>' % self.title


class User(db.Model):
    __tablename__ = 'b_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(16))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # 删除所有的表
    db.drop_all()
    # 创建表
    db.create_all()

```
runserver.py
```
from myBlog.__init__ import app


if __name__ == '__main__':
    app.run(port=8000, debug=True)
```
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