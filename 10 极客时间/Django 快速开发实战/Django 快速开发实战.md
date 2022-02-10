https://time.geekbang.org/course/intro/100061901?tab=catalog

Linux下开发：
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
    
