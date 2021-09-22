import socket

client_socket = socket.socket()  # 创建套接字
ip_port = ("127.0.0.1", 8889)  # 要连接的服务器的 ip 和端口
client_socket.connect(ip_port)  # 连接服务器
input("已经连接服务器成功......")  # 让代码阻塞在此处，防止客户端退出
client_socket.close()
