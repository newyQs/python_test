#第3章 使用docker镜像
docker运行容器前需要本地存在对应的镜像，如果镜像不存在，docker会尝试先从默认镜像仓库下载（默认使用Docker Hub公共注册服务器中的仓库），用户也可以配置使用自定义的镜像仓库。

##问题？
1. 如何使用pull命令从Docker Hub仓库下载镜像至本地；
2. 如何查看本地已有的镜像信息和管理镜像标签；
3. 如何在远端仓库用search命令进行搜索和过滤；
4. 如果删除镜像标签和镜像文件；
5. 如果创建用户定制的镜像并且保存为外部文件；
6. 如何往Docker Hub仓库中推送自己的镜像；

##3.1 获取镜像
镜像是运行容器的前提。可以使用docker [image] pull 命令直接从Docker Hub仓库下载镜像：
```
docker [image] pull NAME[:TAG]
```
其中，NAME是镜像仓库名称（用来区分镜像），TAG是镜像的标签（往往用来表示版本信息）。通常情况下，描述一个镜像需要包括“名称+标签”信息。

例如，获取ubuntu18.04系统的基础镜像可以使用如下的命令：
```
docker pull ubuntu:18.04
```
对于Docker镜像来说，如果不显示的指定TAG，则会默认使用latest标签，这会下载仓库中最新版本的镜像。
```
docker pull ubuntu
相当于
docker pull ubuntu:latest
```
下载过程中可以看出，镜像文件一般由若干层（layer）组成，6c953ac5d795这样的串是层的唯一id（完整的id包含256比特，64个十六进制字符组成）。

使用docker pull命令下载中会获取并输出镜像的各层信息。当不同的镜像包括相同的层时，本地仅存储了层的一份内容，减小了存储空间。

```
docker pull ubuntu:18.04
docker pull registry.hub.docker.com/ubuntu:18.04
```
如果要在非官方的仓库下载，则需要在仓库名称前指定完整的仓库地址，如以下：
```
docker pull pub.c.163.com/public/ubuntu:18.04
```
pull子命令支持的选项主要包括：
+ -a --all-tags=true|false:是否获取仓库中的所有镜像，默认为否；
+ --disable-content-trust:取消镜像的内容校检，默认为否；

下载镜像到本地后，即可随时随地使用该镜像了，例如利用该镜像创建一个容器，在其中运行bash应用，执行打印“hello world”命令：
```
docker run -it ubuntu:18.04 bash
```

##3.2 查看镜像信息
###1. 使用docker images或者docker image ls命令可以列出本地主机上已有的镜像的基础信息
```
docker images
或
docker image ls
```
在列出的信息中，可以看到这几个字段信息：
+ 来自那个仓库
+ 镜像的标签信息
+ 镜像的ID（唯一标识镜像）
+ 创建时间
+ 镜像大小

images子命令主要支持以下选项：
+ -a, --all=true|false
+ -digests=true|false
+ -f, --filter=[]
+ --format="TEMPLATE"
+ --no-trunc=true|false
+ -q, --quiet=true|false

###2. 使用tag命令添加镜像标签
为了方便在后续工作中使用特定镜像，还可以为本地镜像添加新的标签
```
docker tag ubuntu:latest myubuntu:latest
```

###3. 使用inspect命令查看详细信息
获取镜像的详细信息，包括制作者，适应架构，各层的数字摘要等；
```
docker [image] inspect ubuntu:18.04
```

###4. 使用history查看镜像历史
揖让镜像文件由多个层组成，那么怎么知道各个层的内容具体是什么呢？这时候可以使用history命令，该命令可以列出各层的创建信息。
```
docker histoty ubuntu:18.04
```

##3.3 搜寻镜像
```
docker search [option] keyword
```
支持的子命令包括：
+ -f, --filter filter:过滤输出内容；
+ -format string：格式化输出内容；
+ limit int：限制输出的结果个数，默认为25个；
+ --no-trunc：不截断输出结果；

例如，搜索官方提供的带nginx关键字的镜像
```
docker search --filter-offical=true nginx
```
例如，搜索所有收藏数超过4的关键字包括tensorflow的镜像：
```
docker search --filter=starts=4 tensorflow
```

##3.4 删除镜像
1. 使用标签删除镜像
    ```
    docker rmi IMAGE [IMAGE...]
    ```
    注：其中IMAGE可以为标签或者ID
    
    支持选项包括：
    + -f, force：强制删除镜像，即使有容器依赖它；
    + -no-prune：不要清理未带标签的父镜像；
    
    ```
    docker rmi ubuntu:18.04
    或
    docker image rm ubuntu:18.04
    ```
    当镜像只剩下一个标签时，此时使用docker rmi命令会彻底删除这个镜像；

2. 使用镜像ID来删除镜像

   当使用docker rmi 命令，并且后面跟上镜像的ID（也可以是能区分的部分ID串前缀）时，会先尝试删除所有指向所有该镜像的标签，然后删除这个镜像文件本身；
   
   注意，当有该镜像创建的容器存在时，镜像文件默认是无法被删除的；
   ```
   docker run ubuntu:18.04 echo 'hello world'
   ```
   使用docker ps -a 可以查看本机上存在的所有容器；
   ```
   docker ps -a
   ```
   当试图删除镜像时，docker会提示有容器在运行，无法被删除；
   
   如果想要强行删除，可以添加-f 参数：
   ```
   docker rmi -f ubuntu:18.04
   ```
   注意，通常不推荐直接使用 -f 参数删除一个存在容器依赖的镜像，正确的步骤是先删除依赖该镜像的所有容器，再来删除镜像。
   
##3.5 清理镜像
```
docker image prune 
```
支持选项为：
+ -a, -all：删除所有无用的镜像，不光是临时镜像；
+ -filter filter：只清理符合给定过滤器的镜像；
+ -f, -force：强制删除镜像，而不进行提示确认；

##3.6 创建镜像
1. 基于已有容器创建
    ```
    docker [container] commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
    ```
    主要选项包括：
    + -a, --author=" "
    + -c, --change=[ ]
    + -m, --message=" "
    + -p, --pause=true
    
2. 基于本地模板导入
    ```
    docker [image] import [OPTIONS] file|URL -[REPOSITORY] [:TAG]
    ```
3. 基于Dockerfile创建
    ```
    FROM debian:stretch-slim
    LABEL version="1.0" maintainer="docker user <docker_user>@github>"
    RUN apt-get update && \
        apt-get install -y python3 && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*
    ```   
    创建镜像的过程可以使用docker [image] build命令，编译成功后本地将多出个python:3镜像:
    ```
    docker [image] build -t python3
    ```
##3.7 存出和载入镜像
1. 存出镜像
    如果要导出镜像到本地文件，可以使用docker [image] save命令。该命令支持-o 、-output string参数，导出镜像到指定的文件中。
    ```
    docker [image] save
    ```
    例如，导出本地的ubuntu:18.04镜像为文件ubuntu_18.04.tar，如下所示：
    ```
    docker save -o ubuntu_18.04.tar ubuntu:18.04
    ```
    之后，用户就可以通过复制ubuntu_18.04.tar文件将该镜像分享给他人。
2. 载入镜像 
    可以使用docker [image] load 将导出的tar文件再导入到本地镜像库，支持-i、-input string选项，从指定文件中读取镜像内容。
    ```
    docker [image] load  
    ```
    例如，从文件ubuntu_18.04.tar文件导入镜像至本地镜像列表，如下所示：
    ```
    docker load -i < ubuntu_18.04.tar
    或者
    docker load < ubuntu_18.04.tar
    ```
    这将导入镜像及其相关的元数据信息（包括标签等）。

##3.8 上传镜像
可以使用docker [image] push命令上传镜像到仓库，默认上传到Docker Hub官方仓库（需要登录）
```
docker [image] push NAME[:TAG] | [REGISTRY_HOST[:REGISTRY_PROT]/]NAME[:TAG]
```
例如，用户user上传本地的test:latest镜像，可以先添加新的标签user/test:latest，然后使用docker image push命令上传镜像：
```
docker tag test:latest user/test:latest
docker push user/test:latest
```