1. 获取镜像
    不跟标签，默认最新的:latest
    ```
    docker pull ubuntu
    ```
    拉取指定标签的镜像
    ```
    docker pull ubuntu:18.04
    ```
2. 启动容器
    ```
    docker run -it ubuntu:18.04 /bin/bash
    ```  
    参数说明：  
    + -i：交互式操作
    + -t：终端
    + ubuntu：镜像
    + /bin/bash：命令。交互式的shell 
    
    **docker run** 后面有很多参数，需要重点关注。

3. 查看容器
    ```
    docker ps
    ```
    查看所有容器（包括停止的）
    ```
    docker ps -a 
    ```
 
4. 启动已经停止的容器
    ```
    docker start <container_id>
    ```
    ```
    docker restart <container_id> 
    ```  
    注：这两个有啥区别：启动和重启？？？

5. 后台运行容器
    ```
    docker run -itd --name ubuntu-test ubuntu:18.04 /bin/bash 
    ```     
    注意：加了 -d 参数默认不会进入容器，想要进入容器需要使用指令 docker exec

6. 停止一个容器
    ```
    docker stop <container_id>
    ```
    
7. 重启已经停止的容器
    ```
    docker restart <container_id>
    ```
    
8. 进入容器
    ```
    docker attach <container_id>
    ```
    ```
    docker exec -it <container_id> /bin/bash 
    ```      
    推荐使用 docker exec 命令，因为此退出容器终端，不会导致容器的停止。

9. 导出容器
    ```
    docker export <container_id> > <name>
    ```    
    示例：
    ```    
    docker export 1e560fca3906 > ubuntu.tar
    ```
    
10. 导入容器
    ```
    docker import  
    ```  
    示例：
    ```   
    cat docker/ubuntu.tar | docker import - test/ubuntu:v1.0 
    ```      
    也可以指定URL或者某个目录导入：
    ```
    docker import http://example.com/exampleimage.tgz example/imagerepo
    ```
    
11. 删除容器
    ```
    docker rm -f <container_id>
    ```
    删除镜像是 rmi 注意区别：
    ```
    docker rmi <image_id>
    ```
12. 清理所有处于终止状态下的容器
    ```
    docker container prune
    ```



