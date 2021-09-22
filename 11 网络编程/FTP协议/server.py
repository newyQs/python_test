from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter
import logging

# 记录日志，默认情况下日志仅输出到屏幕（终端），这里既输出到屏幕又输出到文件，方便日志查看
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='myftpserver.log', encoding='utf-8')  # 日志文件
ch.setFormatter(LogFormatter())
fh.setFormatter(LogFormatter())
logger.addHandler(ch)  # 将日志输出至屏幕
logger.addHandler(fh)  # 将日志输出至文件

# 实例化虚拟用户，这是 FTP 验证首要条件
authorizer = DummyAuthorizer()

'''
添加用户权限和路径，括号内的参数是（用户名、密码、用户目录、权限），可以为不同的用户添加不同的目录和权限
读权限：
e: 改变文件目录；l: 列出文件； r: 从服务器接收文件
写权限：
a: 文件上传； d: 删除文件； f: 文件重命名； m: 创建文件； w: 写权限；
M: 文件传输模式（通过FTP设置文件权限）
'''
authorizer.add_user("user", "123456", r"ftp", perm="elradfmw")

# 添加匿名用户，只需要路径
authorizer.add_anonymous(r"ftp")


# 初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer

# 添加被动端口范围
handler.passive_ports = range(2000, 2333)

# 下载上传速度设置
dtp_handler = ThrottledDTPHandler
dtp_handler.read_limit = 300 * 1024  # 300kb/s
dtp_handler.write_limit = 300 * 1024  # 300kb/s
handler.dtp_handler = dtp_handler

# 监听 IP 和端口，我们使用 21 端口
server = FTPServer(("0.0.0.0", 21), handler)

# 最大连接数
server.max_cons = 150
server.max_cons_per_ip = 15

# 开始服务，自带日志打印信息
server.serve_forever()