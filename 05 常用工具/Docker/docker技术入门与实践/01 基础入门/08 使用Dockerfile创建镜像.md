# 第8章 使用Dockerfile创建镜像
Dockerfile是一个文本格式的配置文件，用户可以通过Dockerfile来快速创建自定义的容器。

## 8.1 基本结构
一般而言，Dockerfile主体内容分为四个部分：基础镜像部分，维护者信息，镜像操作指定和启动时执行指令。

示例：
```
FROM debian:jessie
LABEL maintainer docker_user<docker_user@email.com>
ENV NGINX_VERSION 1.10.1~jessie
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC64107
```

## 8.2 指令说明
配置指令：13
+ ARG
+ FROM
+ LABEL
+ EXPOSE
+ ENV
+ ENTRYPOINT
+ VOLUME
+ USER
+ WORKDIR
+ ONBUILD
+ STOPSIGNAL
+ HEALTHCHECK
+ SHELL
 
操作指定：4
+ RUN
+ CMD
+ ADD
+ COPY

## 8.3 创建镜像
编写玩Dockerfile之后，可以通过docker [image] build 命令来创建镜像。

基本格式为：docker build [OPTIONS] PATH | URL | -

## 8.4 最佳实践
所谓最佳实践，就是从需求出发，来定制适合于自己，高效方便的镜像。

在生产镜像过程中，应该做到如下：
+ 精简镜像用途：
+ 选用合适的基础镜像：
+ 提供注释和维护者信息：
+ 正确使用版本号：
+ 减小镜像层数：
+ 恰当使用多步骤创建：
+ 使用.dockerignore文件：
+ 及时删除临时文件和缓存文件：
+ 提高生成速度：
+ 调整合理的指令顺序：
+ 减少外部源的干扰：
