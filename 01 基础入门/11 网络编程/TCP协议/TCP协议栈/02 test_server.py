import socket

sv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sv_ipport = ("0.0.0.0", 8889)
sv_socket.bind(sv_ipport)
sv_socket.listen(2)  # 协议栈缓冲区最大套接字存放个数
print('启动服务器，等待客户端连接......')

while True:
    input("阻塞中......")  # 让代码阻塞在此处
    server_socket, addr = sv_socket.accept()  # 从协议栈缓冲区中取出一个套接字

server_socket.close()  # 关闭套接字