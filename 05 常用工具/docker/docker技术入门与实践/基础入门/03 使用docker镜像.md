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

如，获取UBuntu18.04系统的基础镜像可以使用如下的命令：
```
docker pull ubuntu:18.04
```
对于Docker镜像来说，如果不显示的指定TAG，则会默认使用latest标签，这会下载仓库中最新版本的镜像。
```
docker pull ubuntu
相当于：
docker pull ubuntu:latest
```
下载过程中可以看出，镜像文件一般由若干层（layer）组成，完整的id包含256比特，64个十六进制组成。

```
docker pull ubuntu:18.04
docker pull registry.hub.docker.com/ubuntu:18.04
```

##3.2 查看镜像信息
###1. 使用docker images或者docker image ls命令查看本地主机上已有的镜像的基础信息
```
docker images
docker image ls
```

###2. 使用tag命令添加镜像标签
```
docker tag ubuntu:latest myubuntu:latest
```

###3. 使用inspect命令查看详细信息
```
docker [image] inspect ubuntu:18.04
```

###4. 使用history查看镜像历史
```
docker histoty ubuntu:18.04
```

##3.3 搜寻镜像
```
docker search [option] keyword
```

##3.4 删除镜像
```
docker rmi ubuntu:18.04
docker image rm  ubuntu:18.04
```

##3.5 清理镜像
```
docker image prune 
```

##3.6 创建镜像
1. 基于已有容器创建
    ```
    docker [container] commit
    ```
2. 基于本地模板导入
    ```
    docker [image] import [OPTIONS] file|URL -[REPOSITORY] [:TAG]
    ```
3. 基于Dockerfile创建
    ```
    
    ```   
##3.7 存出和载入镜像
1. 存出镜像
    ```
    docker [image] save
    ```
2. 载入镜像 
    ```
    docker [image] load  
    ```

##3.8 上传镜像
```
docker [image] push NAME[:TAG]
```