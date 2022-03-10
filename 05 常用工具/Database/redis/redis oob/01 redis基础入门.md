https://www.runoob.com/redis/redis-tutorial.html
# redis介绍，原理，安装，配置

## Windows 下安装:
https://github.com/tporadowski/redis/releases
```
# 开启redis服务端：在安装目录里执行
redis-server.exe redis.windows.conf 

# 启动redis客户端:打开另一个终端执行
redis-cli.exe -h 127.0.0.1 -p 6379
```

## Linux 源码安装:
https://redis.io/download
```
# 下载源码包
wget http://download.redis.io/releases/redis-6.0.8.tar.gz

# 解压压缩包
tar xzf redis-6.0.8.tar.gz

cd redis-6.0.8

# 编译
make

cd src

启动 redis 服务
./redis-server 
# 或指定配置文件
./redis-server ../redis.conf

启动 redis 客户端
cd src
./redis-cli
```

## Ubuntu apt 命令安装:
```
apt update && apt install redis-server

启动redis:
redis-server

查看redis是否启动：
redis-cli
```

## redis连接
redis-cli -h host -p port -a password

以下为连接到主机为10.61.67.6，端口为6379，密码为passname的redis服务器上
```
redis-cli -h 10.61.67.6 -p 6379 -a passname
```

## redis配置
