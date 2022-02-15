# 第11章 Web服务与应用

## 11.1 Apache
Apache是一种高稳定性、商业级别的开源web服务器。跨平台性和安全性。

1. 使用DockerHub镜像
    (1) 创建Dockerfile文件：
    ```
    FROM httpd:2.4
    COPY ./public-html /usr/local/apache2/htdocs/
    ```
    
    (2) 创建项目目录public-html，并在里面创建index.html文件
    ```html
    <!DOCTYPE html>
    <html>
    <body>
        <p>Hello Docker!</p>
    </body>
    </html>
    ```
    
    (3) 构建自定义镜像：
    ```
    docker build -t apache2-image .
    ```
    
    (4) 访问资源
    通过本地的80端口即可访问静态页面。
    
    (5) 目录映射
    可以不创建镜像，而通过映射目录的方式来访问apache服务器：
    ```
    docker run -it --rm --name my-apache-app -p 80:80 -v "$PWD":/usr/local/apche2/htdocs/ httpd:2.4
    ```

2. 使用自定义镜像
    (1) 创建apache_ubuntu工作目录，在其中创建Dockerfile文件，run.sh文件和sample目录。
    ```
    mkdir apache_ubuntu && cd apache_ubuntu
    touch Dockerfile run.sh
    mkdir sample
    ```
    
    (2) 编写Dockerfile文件
    ```
    # 设置继承于哦用户创建的sshd镜像
    FROM sshd:dockerfile
    
    # 创建者的基本信息
    MAINTAINER docker_user (user@docker.com)
    
    # 设置环境变量，所有操作都是非交互式的
    ENV DEBIAN_FRONTEND noninterachtive
    
    # 安装
    RUN apt-get -yq install apache2 && \
        rm -rf /var/lib/apt/list/* 
    
    # 修改系统的时区    
    RUN echo "Asia/Shanghai" > /etc/timezone && \
        dpkg-reconfigure -f nointeractive tzdata
    
    # 添加用户的脚本，并设置权限，这会覆盖之前放在这个位置的脚本
    ADD run.sh /run.sh
    RUN chmod 755 /*.sh
    
    # 添加一个示例的web站点。
    RUN mkdir -p /var/lock/apache2 && \
        mkdir -p /app && \
        rm -rf /var/www/html && \
        ln -s /app /var/www/html
        
    COPY sample /app
    
    ENV APACHE_RUN_USER www-data
    ENV APACHE_RUN_GROUP www-data
    ENV APACHE_LOG_DIR /var/log/apache2
    ENV APACHE_PID FILE /var/log/apache2.pid
    ENV APACHE_RUN_DIR /var/run/apache2
    ENV APACHE_LOCK_DIR /var/lock/apache2
    ENV APACHE_SERVERADMIN admin@localhost
    ENV APACHE_SERVERNAME localhost
    ENV APACHE_SERVERALTAS docker.localhost
    ENV APACHE_DOCUMENTROOT /var/www
    
    EXPOSE 80
    WORKDIR /app
    CMD ["/run.sh"]
    ```
    
    (3) index.html文件和run.sh文件内容
    ```html
    <!DOCTYPE html>
    <html>
    <body>
        <p>Hello Docker!</p>
    </body>
    </html>
    ```
    ```
    #!/bin/bash
    /usr/sbin/sshd &
    exec apche2 -D FOREGROUND
    ```
    
    (4) 构建镜像
    ```
    docker build -t apche:ubuntu .
    ```
    (5) 测试镜像
    ```
    docker run -d -P apache:ubuntu
    ```
    
3. 相关资源


## 11.2 Nginx
Nginx是一款开源强大的反向代理服务器，支持HTTP、HTTPS、SMTP、POP3、IMAP等协议。它可以作为负载均衡器、HTTP缓存或Web服务器。
专注于高性能、高并发。

1. 使用DockerHub镜像
```
docker run -d -p 80:80 --name weserver nginx
```


2. 自定义Web页面


3. 参数优化


4. 相关资源


## 11.3 Tomcat

1. 准备工作


2. Dockerfile文件和其他脚本文件


3. 创建和测试镜像


4. 相关资源


## 11.4 Jetty

1. 使用官方镜像
```
docker run -d jetty

docker run -d -p 80:8080 -p 443:8443 jetty
```

2. 相关资源


## 11.5 LAMP
LAMP(Linux-Apache-MySQL-PHP)是目前流行的Web工具栈。

1. 使用官方镜像


2. 相关资源


## 11.6 持续开发与管理
CI
    集成通过自动化的构建来完成，包括自动编译，发布和测试，从而尽快的发现错误。

CD
    

1. Jenkins及官方镜像
    https://www.jenkins.io/zh/doc/
    
    Jenkins能实时监控集成中存在的错误，提供详细的日志文件和提醒功能，并用图表的形式形象的展示项目构建的趋势和稳定性。
    
    ```
    docker run -p 8080:8080 -p 50000:50000 jenkins
    ```
    
    
2. Gitlab及其官方镜像
    Gitlab是一款强大的开源源码管理系统。
    ```
    
    ```


## 11.7 本章小结

