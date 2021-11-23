import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字
server_ipport = ("127.0.0.1", 8889)  # 通信的服务器的 ip 和端口

# 发送数据
client_data = "hello"
client_socket.sendto("老鸟".encode("utf-8"), server_ipport)  # 发送信息
client_socket.sendto("python".encode("utf-8"), server_ipport)  # 发送信息
client_socket.sendto("exit".encode("utf-8"), server_ipport)  # 发送信息
client_socket.close()  # 关闭套接字
