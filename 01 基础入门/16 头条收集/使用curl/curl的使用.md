参考：

https://www.toutiao.com/i7054875398861144614/?tt_from=weixin&utm_campaign=client_share&wxshare_count=1&timestamp=1642946448&app=news_article&utm_source=weixin&utm_medium=toutiao_android&use_new_style=1&req_id=202201232200470101510922080FFDDCFE&share_token=01606de8-9fab-4f40-bfcc-58fc3f9dbf8b&group_id=7054875398861144614&wid=1642946512093

## curl介绍
curl 是 Linux 系统上一款网络工具，它的首字母 c 代表的是 client，表示它是客户端程序。通过 URL 方式，可以实现客户端与服务器之间传递数据。

它的功能非常强大，支持大部分常见的网络协议：HTTP、HTTPS、FTP。
功能特性也很丰富，支持 http、https、cookie、认证、代理、速率限制、断点续传，提供非常多的选项，熟练运用的话，基本可以取代 postman 这类图形工具。

## 与liburl关系
其实 curl 项目包括两部分：curl 和 libcurl，关系大概如图所示:

![](img/curl.png)

+ curl 是命令行工具，底层调用的是 libcurl 库。
+  libcurl 是以库形式存在，提供各种功能 C 接口，供其他程序调用，包括 curl 命令

## 安装使用
和 wget 不同，并非所有的 Linux 发行版中都安装了 curl，你可以使用包管理器自行安装
```
# ubuntu or debian
$ apt install curl

# centos or redhat
$ yum install curl
```
如果需要使用最新版本，或自定义安装，可以通过源码编译方式进行安装

源码的安装一般由3个步骤组成：配置（configure）、编译（make）、安装( make install ).
```
$ wget https://curl.se/download/curl-7.79.1.tar.gz
$ cd curl-7.79.1
$ ./configure
$ make && make install
```
通过 curl --version 可以验证命令是否安装准确

## 上手操作
我们先来看下 curl 最简单的使用方式，没有任何选项，将服务器响应的内容输出到屏幕上
```
$ curl http://linuxblogs.cn
```
有时我们不想显示错误和进度信息，可以使用 -s 选项开启静默模式
```
$ curl -s http://linuxblogs.cn
# 完全不输出任何内容，可以通过"echo $?"来判断命令成功或失败
$ curl -s -o /dev/null http://linuxblogs.cn
```
通过 -v 选项可以非常详细地显示 curl 的整个工作过程，相当于打开了调试模式

## 请求http

1. 发送 GET 请求

    curl 命令默认发送的是 GET 请求，响应内容直接打印在了屏幕上
    ```
    $ curl http://www.baidu.com
    ```
    使用 -i 选项，可以打印服务器响应的 HTTP 头部信息
    ```
    # 先打印请求头，空一行，再打印网页内容
    $ curl -i http://www.baidu.com
    ```
    如果只想测试该链接或资源是否正常，使用 -I 选项，可以只打印响应头信息，注意此时发送的是 HEAD 请求

2. 发送 POST 请求

    默认情况下，curl 发送的是 GET 请求，使用 -X 参数可以指定发送 POST 请求，使用 -d 参数可以指定请求数据
    ```
    # 无数据的 POST 请求
    $ curl -x POST http://www.domain.com
    # 发送 Form 数据
    $ curl -d 'user=foo&pass=123' -X POST http://google.com/login 
    # 等价于上边命令
    $ curl -d 'user=foo' -d 'pass=123' http://google.com/login
    ```
    使用 -d 选项后，默认就是 POST 请求，可以省略 -X 选项，另外，使用多个 -d 选项，可以使命令行显得更清晰
    
    下边命令可以读取本地文件，作为数据向服务器发送
    ```
    $ curl -d '@data.txt' http://google.com/login
    ```

3. 发送 Json 格式数据请求

    curl 可以发送 json 格式的请求，需要设置 Content-Type 为 application/json
    ```
    $ curl -d '{"user":"foo","pass":"123"}' \
          -H 'Content-Type: application/json' \
          http://google.com/login
    ```
    -H 选项指定 Content-Type 请求头为 json 格式，这样 web 服务器就清楚数据类型，知道该怎么处理了

4. 构造查询字符串参数

    通过 -G 选项，可以构造查询字符串参数
    ```
    curl -G -d 'q=chopin' -d 'count=20' http://google.com/search
    # 等价于下边命令
    curl 'http://google.com/search?q=chopin&count=20'
    ```
    上述命令会发送 GET 请求，如果忽略 -G 选项，会发出一个 POST 请求

5. 添加请求头

    通过 -H 选项，可以为请求添加标头
    ```
    $ curl -H 'Accept-Language: en-US' http://google.com
    # 可以指定多个-H选项
    $ curl -H 'Accept-Language: en-US' -H 'Secret-Message: xyzzy' http://google.com
    ```

6. 设置重定向

    默认 curl 不会跟随重定向，指定 -L 选项会让请求跟随服务器重定向
    ```
    $ curl -L http://api.twitter.com/hello
    ```

7. 设置静默输出

    指定 -s 选项将不输出错误和进度信息，如果想让 curl 不产生任何输出，使用下面的命令
    ```
    $ curl -s -o /dev/null http://google.com
    ```

8. 详细的调试信息

    指定 -v 选项，会输出通信的整个过程，一般用于调试
    ```
    $ curl -v http://www.baidu.com
    ```
    --trace 选项也可以用来调试，还可以输出更详细的内容，比如原始的二进制数据
    ```
    $ curl --trace - http://www.baidu.com
    ```

9. 模拟浏览器访问

    -A 选项可以指定客户端的用户代理信息，即设置 UserAgent 请求头。
    ```
    $ curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' http://google.com
    ```
    上面命令将 UserAgent 设置成了 Chrome 浏览器的标识。其实也可以直接通过 -H 选项来指定
    ```
    $ curl -H "User-Agent: go/1.15" http://google.com
    ```

10. 伪造 refer 解决防盗链

    有时候，引用或下载某网站图片等资源时，会有防盗链的限制，可以通过设置 refer 请求头为站内域名来解决
    ```
    # -e 参数来设置 HTTP 请求头 Referer
    $ curl -e 'http://linuxblogs.cn' http://linuxblogs.cn/girl.jpg
    # -H 参数也可以直接设置请求头 Referer
    $ curl -H "Referer: http://linuxblogs.cn" http://linuxblogs.cn/girl.jpg
    ```

11. 设置 Cookie

    -b 选项用来向服务器发送 Cookie，该命令会生成一个请求头 Cookie: foo=bar，向服务器发送一个 Cookie
    ```
    $ curl -b 'foo=bar' http://google.com
    # 发送两个cookie
    $ curl -b 'foo=bar;name=mike' http://google.com
    ```
    也可以通过读取本地 cookie 文件，将其发送给服务器。-c 选项可以将服务器响应的 Cookie 写入一个文件
    ```
    $ curl -b cookie.txt http://google.com
    # 将cookie写入文件
    $ curl -c cookie.txt http://baidu.com
    ```

## 文件操作
1. 下载文件资源

    使用 -o 或 -O 选项，可以将网络资源保存到文件中
    ```
    # 等效于 wget
    $ curl -o chopin.html http://linuxblogs.cn
    # -O 选项，可以将 URL 的最后部分当做文件名
    $ curl -O http://linuxblogs.cn/bar.html
    ```
    如果想显示下载进度条，可以使用 -# 选项

2. 循环下载文件

    有时候要下载的多个文件，只有名称后缀不同，可以这样来下载
    ```
    $ curl -O http://linuxblogs.cn/dog[1-5].jpg
    ```

3. 压缩下载

    使用 --compressed 选项，允许你要求 HTTP 和 HTTPS 服务器提供数据的压缩版本，这在带宽有限的情况下，可以帮你节约不少时间
    ```
    curl --compressed http://linuxblogs.cn/foo.txt
    ```

4. 限制下载速度

    如果带宽不是很充足，多人共享带宽，curl 支持限速功能
    ```
    $ curl http://linuxblogs.cn --limit-rate 200K
    ```
    另外一个用法，就是模拟测试慢网速的场景，用于做开发测试

5. 分块下载

    有时文件会很大，我们采用可以分段的方式进行下载，最后合并为完成的文件
    ```
    $ curl -r 0-100 -o part1.mp4 http://linuxblogs.cn/cang.mp4
    $ curl -r 100-200 -o part2.mp4 http://linuxblogs.cn/cang.mp4
    $ curl -r 200- -o part3.mp4 http://linuxblogs.cn/cang.mp4
    $ cat part*.mp4 > cang.mp4
    ```

6. 断点续传

    有时候网络不太好，通过 curl 下载大文件时，可能发生中断的现象。使用 -C 选项可以实现断点续传，非常实用
    ```
    $ curl -C -O http://linuxblogs.cn/girl.mp4
    ```
    在弱网环境下，加上 --retry N 选项，可以在失败的时候多次重试，对下载操作更友好一些。

7. 通过 FTP 下载文件

    支持下载 FTP 文件，curl 提供两种下载的语法
    ```
    $ curl -O -u user:pass ftp://linuxblogs.cn/dog.jpg
    $ curl -O ftp://user:pass@linuxblogs.cn/dog.jpg
    ```

8. 上传文件

    平时开发时，可以通过 curl 实现文件的上传功能，非常高效。
    ```
    # 命令会给 HTTP 加上请求头 Content-Type: multipart/form-datas
    $ curl -F 'file=@苍老师.mp4' http://linuxblogs.cn/upload
    ```
    -F 选项还可以指定 MIME 类型和文件名
    ```
    $ curl -F 'file=@苍老师.mp4;type=image/png' http://linuxblogs.cn/upload
    # 还可以支持修改文件名，而不是默认的
    $ curl -F 'file=@苍老师.mp4;file=天空.mp4' http://linuxblogs.cn/upload
    ```

## https相关
目前大多数站点采用的都是 https，这里给出几个常见的用法

1. 忽略证书验证

    有时访问 https 站点时，服务器证书过期或是自签证书，使用 curl 访问时会报错，可以指定 -k 选项来忽略证书有效性验证。
    ```
    $ curl -k https://linuxblogs.cn
    ```

2. 指定客户端证书

    有时需要双向验证，服务器也要验证客户端，用来确定客户端的真实身份。可以使用 --cert 和 --key 指定客户端证书
    ```
    $ curl --cert client.pem --key key.pem https://linuxblogs.cn
    ```

3. 使用证书链验证服务器证书

    在平时开发时，证书一般是自签的，可以通过指定 CA 证书链进行证书的验证
    ```
    $ curl --cacert caChain.pem https://linuxblogs.cn
    ```

## 高级功能
（一）设置代理

1. 命令行

    通过命令行，可以很简单的实现 curl 代理功能
    ```
    $ curl -x "http://user:pwd@127.0.0.1:1234" "http://linuxblogs.cn"
    ```

2. 使用环境变量

    通过设置环境的方式也很简单
    ```
    $ export http_proxy="http://user:pwd@127.0.0.1:1234"
    ```

3. 使用配置文件

    使用配置文件 ~/.curlrc，修改内容如下：
    ```
    proxy="http://user:pwd@127.0.0.1:1234"
    ```

（二）格式化

在平时使用 curl 时，可能希望能够获取更多信息，如请求耗时、访问时延、请求大小等信息。
比如在生产环境要测试某个接口，可以通过如下的方式，获取你想要的数据，非常方便。
```
# 只获取http状态码
$ curl -s -w '%{http_code}' https://baidu.com -o /dev/null
```
