# 第24章 docker 三剑客之 Compose

## 24.1 Compose简介
compose负责实现对基于docker容器的多应用服务的快速编排。

前面已经介绍使用一个Dockerfile模板文件，可以让用户很方便的定义一个单独的应用容器。
但是在日常生活中，经常会碰到需要多个容器相互配合来实现某项任务的情况。
例如，实现一个web项目，除了web服务容器本身，往往还需要加上后端的数据库服务容器，甚至还包括前端的负载均衡容器等。
compose恰恰满足这样的需求，它允许用户通过一个单独的docker-compose.yml模板文件来定义一组相关联的应用容器为一个服务栈。

compose中的几个重要的概念：
- 任务：
- 服务：
- 服务栈：


## 24.2 安装与卸载

1. pip安装


2. 二进制包


3. 容器中执行


4. 卸载
如果是二进制包方式安装的，删除二进制文件即可：
```
sudo rm /usr/local/bin/docker-compose
```
如果是通过python pip安装的，如下卸载：
```
sudo pip uninstall docker-compose
```


## 24.3 Compose模板文件
默认的模板文件即docker-compose.yml，目前最新的版本为v3。

compose模板文件说明：
1. build

2. cap_add, cap_drop

3. command

4. configs

5. cgroup_parent

6. container_name

7. devices

8. depends_on

9. dns

10. dns_search

11. dockerfile

12. entrypoint

13. env_file

14. environment

15. expose

16. extends

17. external_links

18. extra_hosts

19. healthcheck

20. image

21. isolation

22. labels

23. links

24. logging

25. network_mode

26. networks

27. pid

28. ports

29. secrets

30. security_opt

31. stop_grace_period

32. stop_signal

33. sysctls

34. ulimits

35. userns_mode

36. volumes

37. restart

38. deploy

39. 其他指令

40. 读取环境变量

41. 扩展特性


## 24.4 Compose命令说明

1. build

2. bundle

3. config

4. down

5. events

6. exec

7. help

8. images

9. kill

10. logs

11. pause

12. port

13. ps

14. pull

15. push 

16. restart

17. rm

18. run

19. scale

20. start

21. stop

22. top

23. unpause

24. up

25. version

## 24.5 Compose环境变量



## 24.6 Compose应用案例一：Web负载均衡

1. web子目录

2. haproxy目录

3. docker-compose.yml

4. 运行compose项目



## 24.7 Compose应用案例二：大数据的Spark集群

1. 准备工作
    (1) docker-compose.yml文件
    (2) master服务
    (3) work服务

2. 启动集群


3. 执行应用



## 24.8 本章小结


