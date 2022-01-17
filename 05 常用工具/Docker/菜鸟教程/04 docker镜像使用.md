1. 列出本地主机上所有镜像
    docker images

2. 查找镜像
    docker search ubuntu:18.04

3. 拉取镜像
    docker pull ubuntu:18.04

4. 删除镜像
    docker rmi <image_id>

5. 创建镜像
    1、从已经创建的容器中更新镜像，并且提交这个镜像
    先创建一个容器：
        docker run -t -i ubuntu:15.10 /bin/bash
    再作修改：
        apt-get update
    提交成新的镜像：
        docker commit -m="message" -a "author" <container_id> IMAGE:TAG
    查看镜像：
        docker images
    
    2、使用 Dockerfile 指令来创建一个新的镜像
    新建一个Dockerfile文件
        Dockerfile
        ```
        FROM    centos:6.7
        MAINTAINER      Fisher "fisher@sudops.com"
        
        RUN     /bin/echo 'root:123456' |chpasswd
        RUN     useradd runoob
        RUN     /bin/echo 'runoob:123456' |chpasswd
        RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
        EXPOSE  22
        EXPOSE  80
        CMD     /usr/sbin/sshd -D
        ```
    构建镜像
        docker built -t IMAGE:TAG .
        + -t ：指定要创建的目标镜像名
        + . ：Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径
        
6. 设置镜像标签
    docker tag <image_id> NEW_IMAGE:TAG
    或者
    docker tag OLD_IMAGE:TAG NEW_IMAGE:TAG