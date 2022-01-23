# Nginx实现负载均衡
https://www.jianshu.com/p/4c250c1cd6cd

## 轮询
轮询方式是Nginx负载默认的方式，顾名思义，所有请求都按照时间顺序分配到不同的服务上，如果服务Down掉，可以自动剔除，
如下配置后轮询10001服务和10002服务:
```
upstream  dalaoyang-server {
       server    localhost:10001;
       server    localhost:10002;
}
```

## 权重
指定每个服务的权重比例，weight和访问比率成正比，通常用于后端服务机器性能不统一，将性能好的分配权重高来发挥服务器最大性能，
如下配置后10002服务的访问比率会是10001服务的二倍:
```
upstream  dalaoyang-server {
       server    localhost:10001 weight=1;
       server    localhost:10002 weight=2;
}
```

## ip_hash
每个请求都根据访问ip的hash结果分配，经过这样的处理，每个访客固定访问一个后端服务，
如下配置（ip_hash可以和weight配合使用）:
```
upstream  dalaoyang-server {
       ip_hash; 
       server    localhost:10001 weight=1;
       server    localhost:10002 weight=2;
}
```

## 最少连接
将请求分配到连接数最少的服务上:
```
upstream  dalaoyang-server {
       least_conn;
       server    localhost:10001 weight=1;
       server    localhost:10002 weight=2;
}
```

# Nginx配置
以轮训为例，如下是nginx.conf完整代码
```
worker_processes  1;

events {
    worker_connections  1024;
}

http {
   upstream  dalaoyang-server {
       server    localhost:10001 weight=1;
       server    localhost:10002 weight=2;
   }

   server {
       listen       10000;
       server_name  localhost;

       location / {
        proxy_pass http://dalaoyang-server;
        proxy_redirect default;
      }

    }

}
```