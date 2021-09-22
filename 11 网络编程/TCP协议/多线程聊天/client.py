import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8092))

while True:
    client_data = input('请输入要发送给服务器的消息：')
    client_socket.send(client_data.encode('utf-8'))

    server_data = client_socket.recv(1024).decode('utf-8')
    if server_data == 'exit' or not server_data:
        break

    print(f'收到服务器发来的消息：{server_data}')

client_socket.close()
