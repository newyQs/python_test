import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 7856)

while True:
    client_data = input('请输入要发送给服务器的消息：')
    client_socket.sendto(client_data.encode('utf-8'), ip_port)  # 向服务端发送的消息,附带ip_port

    server_data, addr = client_socket.recvfrom(1024)
    # print(f'server_data:{server_data};addr:{addr}')   # b'...';('127.0.0.1', 7856)

    server_data = server_data.decode('utf-8')
    if server_data == 'exit':
        print('客户端退出通讯')
        client_socket.sendto('exit'.encode('utf-8'), ip_port)
        break

    print(f'收到服务器信息：{server_data}')

client_socket.close()
