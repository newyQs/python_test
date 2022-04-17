
## 1.1 Django简史

MTV架构
+ 模型(Model):**数据存取层**，处理与数据相关的所有事务，例如如何存取，如何验证有效性，包含哪些行为及数据之间的关系。
+ 模板(Template):**表现层**，处理与表现相关的决定，例如如何再页面或其他类型的文档中进行显示。
+ 视图(View):**业务逻辑层**，存取模型及调取恰当模块的相关逻辑，模型与模板的桥梁。

Django具有如下特点：
+ 对象关系映射
+ URL设计
+ 模板系统
+ 表单处理
+ Cache系统
+ Auth认证系统
+ 国际化
+ Admin系统

## 1.2 Django与WSGI

Web服务器、WSGI和Web应用框架之间的联系:
+ Web服务器，如Apache，Nginx
+ WSGI，Web服务网关接口
+ Web应用框架，如Django，Flask，Tornado，Bottle

开发阶段：
客户端(HTTP) - WSGI Server(uWSGI, wsgiref) - WSGI Application

上线阶段：
客户端(HTTP) - 代理服务器(Nginx) - WSGI Server(uWSGI) - WSGI Application

## 1.3 HTML、CSS和Javascript

## 1.4 搭建开发环境


## 1.5 创建Django项目
1. 内置命令
django-admin startproject <项目名>
python manage.py startapp <应用app名>
python manage.py runserver 0.0.0.0:8000

2. pycharm创建


## 1.6 程序调试技巧
