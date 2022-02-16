# 第10章 为镜像添加SSH服务
很多时候，系统管理员都习惯通过SSH服务来远程登录管理服务器，但是Docker的很多镜像是不带SSH服务的，那么用户如何来管理远程容器呢？

前面有介绍一些进入容器的办法，如使用attach和exec等命令，但是这些命令都无法解决远程管理容器的问题。

## 10.1 基于commit命令创建
Docker的docker commit命令，支持用户提交自己对制定容器的修改，并生成新的镜像。
命令格式为：docker commit CONTAINER [REPOSITORY[:TAG]]

1. 准备工作
    首先获取ubuntu:18.04镜像，并创建一个容器：
    ```
    docker pull ubuntu:18.04
    docker run -it ubuntu:18.04 bash
    ```

2. 配置软件源
    检查软件源，并使用apt-get update命令来更新软件源信息：
    ```
    apt-get update
    ```
    如果默认的官方镜像源速度慢的话，可以替换成国内163、sohu等镜像源，自行了解。
    
3. 安装和配置ssh服务
    (1)更新软件包缓存后可以安装SSH服务了，选用主流的open-server作为服务端：
    ```
    apt-get install openssh-server
    ```
    
    (2)如果需要正常启动SSH服务，则目录/var/run/sshd必须存在。下面手动创建它，并启动SSH服务：
    ```
    mkdir -p /var/run/sshd
    /usr/sbin/sshd -D
    ```
    
    (3)此时查看容器的22端口（SSH服务默认监听的端口），可以看见端口已经处于监听状态：
    ```
    netstat -tunlp
    ```
    
    (4)修改SSH服务的安全登录配置，取消pam登录限制：
    ```
    sed -ri 's/session required pam_loginuid.so'
    ```
    
    (5)在root用户目录下创建.ssh目录，并复制需要登录的公钥信息：
    ```
    mkdir root/.ssh
    vim /root/.ssh/authorized_keys
    ```
    
    (6)创建自动启动的SSH服务的可执行文件run.sh，并添加可执行权限：
    ```
    vim /run.sh
    chmod +x run.sh
    ```
    run.sh脚本内容如下：
    ```
    #!/bin/bash
    /usr/sbin/sshd -D
    ```
    
    (7)最后退出容器
    ```
    exit
    ```
    
4. 保存镜像
    将所退出的容器用docker commit 命令保存为一个新的sshd:ubuntu镜像。
    ```
    docker commit fcl sshd:ubuntu
    ```
    查看镜像：
    ```
    docker images
    ```

5. 使用镜像
    启动容器，并添加端口映射10022 -->22。其中10022是宿主主机的端口，22是容器的SSH服务监听端口：
    ```
    docker run -p 10022:22 -d sshd:ubuntu /run.sh
    ```
    查看容器运行情况
    ```
    docker ps
    ```
    在宿主主机（192.168.1.200）或其他主机上，可以通过SSH服务访问10022端口来登录容器：
    ```
    ssh 192.168.1.200 -p 10022
    ```
    
## 10.2 基于Dockerfile创建

1. 创建工作目录
    创建sshd_ubuntu工作目录，并在里面创建Dockerfile和run.sh文件
    ```
    mkdir sshd_ubuntu
    cd sshd_ubuntu
    touch Dockerfile run.sh
    ```  
    
2. 编写run.sh脚本和authorized_keys文件
    ```
    #!bin/bash
    /usr/sbin/sshd -D
    ```
    在宿主主机上生成SSH密钥对，并创建authorized_keys文件
    ```
    ssh-keygen -t rsa
    ```
    
3. 编写Dockerfile
    ```
    
    ```

4. 创建镜像
    在sshd_ubuntu目录下，使用docker build命令来创建镜像。这里用户需要注意在最后还有一个“·”，表示使用当前目录中的Dockerfile
    ```
    cd sshd_ubuntu
    docker build -t sshd:dockerfile .
    ```
    
5. 测试镜像运行容器
    ```
    docker run -d -p 10122:22 ssjd:dockerfile
    ```
    在宿主主机新打开一个终端，连接到新建的容器：
    ```
    ssh 192.168.1.200 -p 10122
    ```

10.3 本章小结
