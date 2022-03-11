https://time.geekbang.org/course/intro/100061901?tab=catalog

## Linux下开发：
mkdir .env
cd .env
python3 -m venv django
source .env/bin/django
pip install --upgrade pip
pip install django

django-admin startproject my_django
python manage.py runserver 0.0.0.0:8000
这里出现sqlite错误，解决如下：

    1.下载源码包并解压
    mkdir -p /usr/local/sqlite && cd /usr/local/sqlite
    wget https://www.sqlite.org/2021/sqlite-autoconf-3370200.tar.gz（这里上官网https://www.sqlite.org自己找一下）
    tar -zxvf sqlite-autoconf-3370200.tar.gz
    
    2. 初始化并编译安装：
    cd sqlite-autoconf-3370200
    ./configure --prefix=/usr/local/sqlite
    make && make install
    
    3. 重命名并软链
    mv /usr/bin/sqlite3 /usr/bin/sqlite3.bak
    ln -s /usr/local/sqlite/bin/sqlite3 /usr/bin/sqlite3
    
    4. 配置环境变量并生效：
    vim /etc/profile  source /etc/profile
    export LD_LIBRARY_PATH="/usr/local/sqlite/lib"
    
    5. 检查版本：
    sqlite3 --version
    

## windows下开发
https://github.com/stacklens/django_blog_tutorial

注意windows下的路径分隔符不是/ 而是 \

1. 配置虚拟环境
mkdir django_project && cd django_project
python -m venv django2.2
django2.2\Scripts\activate

2. 安装django==2.2
pip install django==2.2

3. 创建django项目
django-admin startproject my_blog

4. 开启服务器
python manage.py runserver 0.0.0.0:8000

5. 打开浏览器
http://127.0.0.1:8000/

6. 创建一个app
python manage.py startapp article
注意：每创建一个app需要到项目根路径下的settings里的INSTALLED_APPS添加创建的app名称。

7. 配置访问路径
在项目根路径下的urlpatterns里面配置path，一般情况我们会将路由分发给每个单独的app处理，给定了include参数。

8. 编写model层


9. 生成数据迁移脚本，并执行迁移
每当你修改了models.py文件，都需要用makemigrations和migrate这两条指令迁移数据。
python manage.py makemigrations
python manage.py migrate

10. 编写views层


11. 创建管理员账号（Superuser）
python manage.py createsuperuser


12. 将新创建的app注册到admin管理后台



项目开启后的一些必要的配置：
1. 设置地区和语言
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

2. 
