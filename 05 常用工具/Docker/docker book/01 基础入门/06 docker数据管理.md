# 第6章 docker数据管理

在生产环境中使用docker，往往需要对数据进行持久化，或者需要在多个容器之间进行数据共享，这必然涉及容器的数据管理操作。

容器中的管理数据主要有两种方式：
1. 数据卷：容器内数据直接映射到本地主机环境；
2. 数据卷容器：使用特定容器维护数据卷；

## 问题？

1. 如何在容器内创建数据卷，并将本地的目录或文件挂载到容器内的数据卷中？
2. 如何使用数据卷容器在容器和主机、容器和容器之间共享数据，并实现数据的备份和恢复？

## 6.1 数据卷

数据卷是一个可供容器使用的特殊目录，它将主机操作系统目录直接映射进容器，类似于linux的mount行为。

数据卷可以提供很多有用的特性：
1. 数据卷可以在容器之间共享和重用，容器间传递数据将变得高效与方便；
2. 对数据卷内数据的修改会立马生效，无论是容器内操作还是本地操作；
3. 对数据卷的更新不会影响镜像，解耦开应用和数据；
4. 卷会一直存在，直到没有容器使用，可以安全的卸载它。

1. 创建数据卷
```
docker volumn create -d local test
```
此时，查看/var/lib/docker/volume路径下，会发现所创建的数据卷位置。

除了create子命令外，docker还支持inspect（查看详细信息） ls（列举已有的数据卷） prune（清理无用数据卷） rm（删除数据卷）

2. 绑定数据卷
除了使用volume子命令来管理数据卷之外，还可以在创建容器时将主机本地的任意路径挂载到容器内作为数据卷，
这种形式创建的数据卷称为绑定数据卷。

在用docker [container] run命令时，可以使用-mount选项来使用数据卷。

--mount选项支持三种类型的数据卷，包括：
+ volume
+ bind
+ tmpfs

## 6.2 数据卷容器

如果用户需要在多个容器之间共享一些持续更新的数据，最简单的方式是使用数据卷容器。
数据卷容器也是一个容器，但是它的目的是专门提供数据卷给其他容器挂载。

## 6.3 利用数据卷容器来迁移数据

可以利用数据卷容器对其中的数据卷进行备份、恢复，以及实现数据的迁移。

1. 备份
```
docker run --volumes-from dbdata -v ${pwd}:/backup --name worker ubuntu tar cvf /backup/backup.tar /dbdata
```
2. 恢复
```
docker run -v /dbdata --name dbdata2 ubuntu /bin/bash
docker run --volumes-from dbdata2 -vb ${pwd}:/backup busybox tar xvf /backup/backup.tar
```

# 6.4 本章小结
```

```