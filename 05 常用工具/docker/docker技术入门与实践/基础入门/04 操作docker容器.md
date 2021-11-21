#第4章 使用dccker容器
简单来说，容器就是一个镜像运行的实例。所不同的是，镜像是静态的只读文件，而容器带有运行时需要的可写文件层，同时，容器中的应用进程处于运行状态。

如果认为虚拟机是模拟运行的一整套操作系统（包括内核，应用运行态环境和其他系统环境）和跑在上面的应用。那么docker容器就是独立运行的一个（或一组）应用，以及它们必需的运行环境。

##4.1 创建容器
1. 新建容器
    ```
    docker [container] create 
    docker create -it ubuntu:latest
    ```
    使用docker [container] create命令新建的容器处于停止状态，可以使用docker [container] start命令来启动它。
    
    由于容器是整个docker技术栈的核心，create命令和后续的run命令支持的选项都十分复杂，后续需要在实践中体会。

2. 启动容器
    
3. 新建并启动容器
    ```
    docker [container] run 
    ```
4. 守护态运行
    ```
    
    ```
5. 查看容器输出
    ```
    docker [container] logs
    ```

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
    
    ```
2. exec命令
    ```
    
    ```

##4.4 删除容器

##4.5 导入和导出容器

##4.6 查看容器

##4.7 其他容器命令
