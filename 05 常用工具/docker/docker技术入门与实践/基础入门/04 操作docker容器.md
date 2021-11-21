#第4章 使用dccker容器
简单来说，容器就是一个镜像运行的实例。所不同的是，镜像是静态的只读文件，而容器带有运行时需要的可写文件层，同时，容器中的应用进程处于运行状态。

如果认为虚拟机是模拟运行的一整套操作系统（包括内核，应用运行态环境和其他系统环境）和跑在上面的应用。那么docker容器就是独立运行的一个（或一组）应用，以及它们必需的运行环境。

##4.1 创建容器
1. 新建容器
    ```
    docker [container] create 
    docker create -it ubuntu:latest
    docker ps -a
    ```
    使用docker [container] create命令新建的容器处于停止状态，可以使用docker [container] start命令来启动它。
    
    由于容器是整个docker技术栈的核心，create命令和后续的run命令支持的选项都十分复杂，后续需要在实践中体会。

2. 启动容器
    ```
    docker [container] start
    ```
    例如，启动刚刚创建的容器
    ```
    docker start af
    ```
    查看容器运行情况
    ```
    docker ps
    ```
3. 新建并启动容器
    ```
    docker [container] run 
    ```
4. 守护态运行
    ```
    docker run -d ubuntu /bin/sh "while true;do echo hello world; sleep 1;done"
    ```
5. 查看容器输出
    ```
    docker [container] logs
    ```
    该命令支持的选项有：
    + -details
    + -f, -follow
    + -since string
    + -tail string
    + -t, -timestamps
    + -until string

##4.2 停止容器
1. 暂停容器
    ```
    docker [container] pause CONTAINER [CONTAINER...]
    ```
2. 终止容器
    ```
    docker [container] stop 
    ```
    
##4.3 进入容器
1. attach命令
    ```
    docker [container] attach [--detach-keys[=[]]] [--no-stdin] [--sog-proxy=[=true]] CONTAINER
    ```
    该命令支持三个主要选项：
    + --detach-keys[=[]]
    + --no-stdin=true|false
    + --sig-proxy=true|false
    
2. exec命令
    ```
    docker [container] exec [-d|--detach] [--detach-keys[=[]]] [-i|--interactive] [--privileged] [-t|--tty] [-u|--user[=USER]] CONTANIER COMMAND [ARG...]
    ```
    重要的参数有：
    + -d, --detach
    + --detach-keys=" "
    + -e, --env=[]
    + -i, --interactive=true|false
    + --privileged=true|false
    + -t, --tty=true|false
    + -u, --user=" "

##4.4 删除容器
```
docker [container] rm [-f|force] [-l|--link] [-v|--volumns] CONTANIER [CONTAINER...]
```
主要支持的选项包含：
+ -f
+ -l
+ -v

##4.5 导入和导出容器
有时候，需要将容器从一个系统迁移到另一个系统，此时可以使用docker的导入和导出功能。
1. 导出容器
    ```
    docker [container] export [-o|--output[=""]] CONTAINER
    ```
    
2. 导入容器
    ```
    docker import [-c|--change[=[]]] [-m|--message[=MESSAGE]] file|URL|-[REPOSITORY[:TAG]]
    ```

##4.6 查看容器
1. 查看容器详情
```
docker [container] inspect [OPTIONS] CONTAINER [CONTAINER...]
```
例如，查看某个容器的具体信息，会以json格式返回包括容器ID，创建时间，路径，状态，镜像，配置等在内的各项信息。
```
docker container inspect test
```

2. 查看容器内进程
```
docker [container] top [OPTIONS] CONTAINER [CONTAINER...]
```

3. 查看统计信息
```
docker [container] stats [OPTIONS] CONTAINER [CONTAINER...]
```

##4.7 其他容器命令
1. 复制文件
container cp命令支持在容器和主机之间复制文件。
```
docker [container] cp [OPTIONS] CONTAINER:SCR_PATH DEST_pATH|-
```
支持的选项包括：
+ -a, -archive
+ -L, -follow-link

例如将本地的路径data复制到test容器的/tmp路径下：
```
docker [container] cp data test:/tmp/
```

2. 查看变更
container diff查看容器内容文件系统的变更。
```
docker [container] diff CONTAINER
```
例如，查看test容器内的数据修改：
```
docker container diff test
```

3. 查看端口映射
container port命令可以查看容器的端口映射情况。
```
docker [container] port CONTAINER [PRIVATE_PORT[/PROTO]]
```
例如，查看test容器内容的端口映射情况
```
docker container port test
```

4. 更新配置
container update命令可以更新容器的一些运行时配置，主要是一些资源限制份额。
```
docker [container] update [OPTIONS] CONTAINER [CONTAINER...]
``` 
支持的选项包括：
