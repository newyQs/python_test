import socket

sv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sv_socket.bind(('127.0.0.1', 7856))

while True:
    print('等待客户端发来的数据：')
    client_data, server_addr = sv_socket.recvfrom(1024)

    client_data = client_data.decode('utf-8')
    if client_data == 'exit':
        print('服务器退出通信')
        sv_socket.sendto('exit'.encode('utf-8'), server_addr)
        break
    print(client_data)

    server_data = input('请输入要发送给客户端的消息：')
    sv_socket.sendto(server_data.encode('utf-8'), server_addr)

sv_socket.close()
