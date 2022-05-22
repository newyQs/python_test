# 第4章 使用docker容器

简单来说，容器就是一个镜像运行的实例。所不同的是，镜像是静态的只读文件，而容器带有运行时需要的可写文件层，同时，容器中的应用进程处于运行状态。

如果认为虚拟机是模拟运行的一整套操作系统（包括内核，应用运行态环境和其他系统环境）和跑在上面的应用，那么docker容器就是独立运行的一个（或一组）应用，以及它们必需的运行环境。

## 问题？

1. 如何创建一个容器；
2. 如何启动一个容器；
3. 如何终止一个容器；
4. 如何进入到容器内执行操作，删除容器和通过导入导出容器来实现容器迁移等。

## 4.1 创建容器

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
    启动刚刚创建的容器：
    ```
    docker start af
    ```
    查看容器运行情况：
    ```
    docker ps
    ```
    
3. 新建并启动容器
    ```
    docker [container] run 
    ```
    示例：
    ```
    docker run ubuntu /bin/echo "hello world"
    docker run -it ubuntu:18.04 /bin/bash
    ```
    其中，-t选项让docker分配一个伪终端并绑定到容器的标准输入上，-i则让容器的标准模式打开。更多的命令使用man docker-run命令来查看。
    
    用户可以通过Ctl+d或者输入exit命令退出容器。
    
4. 守护态运行
    更多的时候，需要docker容器在后台以守护态形式运行，此时可以通过添加-d参数来实现。
    ```
    docker run -d ubuntu /bin/sh "while true;do echo hello world; sleep 1;done"
    ```
    容器启动后会返回唯一的id，也可以通过docker ps或docker container ls命令来查看容器信息:
    ```
    docker ps
    docker container ls
    ```
    
5. 查看容器输出
    要获取容器的输出信息，可以通过docker [container] logs命令。
    ```
    docker [container] logs
    ```
    该命令支持的选项有：
    + -details：打印详细信息
    + -f, -follow：持续保持输出
    + -since string：输出从某个时间开始的日志
    + -tail string：输出最近的若干日志
    + -t, -timestamps：显示时间戳信息
    + -until string：输出某个时间之前的日志
    
    示例：
    ```
    docker logs ce5457846d
    ```
    
## 4.2 停止容器

1. 暂停容器
    ```
    docker [container] pause CONTAINER [CONTAINER...]
    ```
    示例：
    ```
    docker run --name test --rm -it ubuntu bash
    docker pause test
    docker ps
    ```
    处于paused状态的容器，可以恢复，如下：
    ```
    docker [container] unpause CONTAINER [CONTAINER ...]
    ```
    
2. 终止容器
    ```
    docker [container] stop [-t | --time[=10]] [CONTAINER...]
    ```
    该命令会首先向容器发送SIGTERM信息，等待一段超时时间后（默认为10s），再发送SIGKILL信号来终止容器：
    ```
    docker stop ce5
    ```
    此时执行docker container prune命令，会自动清除所有处于停止状态的容器。
    
    此外，还可以通过docker [container] kill直接发送SIGKILL信号来强行终止容器。
    
    当docker容器中指定的应用终结时，容器也会自动停止。例如，上一节中只启动了一个终端的容器，
    用户通过exit或者Ctl+d来退出终端时，所创建的容器立刻终止，处于stopped状态。
    
    可以使用docker ps -qa命令查看所有容器的ID。
    
    处于终止状态的容器，可以再次通过docker [container] start 命令来重新启动。
    
    docker [container] restart命令则是让一个运行态的容器先终止，然后再重新启动。
    
## 4.3 进入容器

在使用-d参数时，容器启动后会进入后台，用户无法看到容器中的信息，也无法进行操作。

这个时候如果需要进入容器进行操作，就需要使用官方的attach或exec命令。
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

## 4.4 删除容器

可以使用docker [container] rm 命令来删除处于终止或退出状态的容器，命令格式为：
```
docker [container] rm [-f|force] [-l|--link] [-v|--volumns] CONTANIER [CONTAINER...]
```
主要支持的选项包含：
+ -f, --force=false：是否强制终止并删除一个运行中的容器；
+ -l, --link=false：删除容器的连接，但保留容器；
+ -v, --volumes=false：删除容器挂载的数据卷； 

## 4.5 导入和导出容器

有时候，需要将容器从一个系统迁移到另一个系统，此时可以使用docker的导入和导出功能。
1. 导出容器
    ```
    docker [container] export [-o|--output[=""]] CONTAINER
    ```
    
2. 导入容器
    ```
    docker import [-c|--change[=[]]] [-m|--message[=MESSAGE]] file|URL|-[REPOSITORY[:TAG]]
    ```

## 4.6 查看容器

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

## 4.7 其他容器命令

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

# 总结
```

```