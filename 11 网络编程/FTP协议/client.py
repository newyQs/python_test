from ftplib import FTP

# 登录FTP
ftp = FTP(host='127.0.0.1', user='user', passwd='123456')

# 设置编码方式
ftp.encoding = 'utf-8'

# 切换目录
ftp.cwd('04 collections')

# 列出文件夹的内容
ftp.retrlines('LIST')  # ftp.dir()

# 从服务器端下载 node.txt
ftp.retrbinary('RETR node.txt', open('node.txt', 'wb').write)

# 上传本地文件
ftp.storbinary('STOR bird.png', open('bird.png', 'rb'))

# 查看目录下的文件详情
for f in ftp.mlsd(path='/04 collections'):
    print(f)
