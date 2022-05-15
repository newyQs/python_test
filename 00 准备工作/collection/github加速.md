第一步：获取 github 的 global.ssl.fastly 地址
    访问：http://github.global.ssl.fastly.net.ipaddress.com/#ipinfo 获取cdn和ip域名：
    如：199.232.69.194

第二步：获取github.com地址
    访问：https://github.com.ipaddress.com/#ipinfo 获取cdn和ip：
    如：140.82.112.3

添加到host文件：
    C:\Windows\System32\drivers\etc\host

    添加内容：示例
        199.232.69.194 github.global.ssl.fastly.net
        140.82.112.3 github.com