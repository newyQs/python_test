import socket

sv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
sv_socket.bind(('127.0.0.1', 8089))  # 套接字绑定ip和端口号

sv_socket.listen(5)  # 协议栈缓存区最大套接字存放数量
print('服务器已启动，等待客户端连接......')

acc_socket, addr = sv_socket.accept()
print(acc_socket, addr)
while True:
    client_data = acc_socket.recv(1024).decode('utf-8')  # 接收消息：bytes==>str
    if client_data == 'exit' or not client_data:
        break

    print(f'收到客户端消息：{client_data}')

    server_data = input('请输入要发送给客户端的消息：')
    acc_socket.send(server_data.encode('utf-8'))  # 发送消息：str==>bytes

acc_socket.close()
