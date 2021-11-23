import socket
import threading


def tcp_link(sock, addr):
    print(f'有新的客户端连接到来：{addr}--{addr}')

    while True:
        client_data = sock.recv(1024).decode('utf-8')
        if client_data == 'exit' or not client_data:
            break

        print(f'收到客户端发来的消息：{client_data}')

        server_data = input('请输入要发送给客户端的消息：')
        sock.send(server_data.encode('utf-8'))

    sock.close()


if __name__ == '__main__':
    sv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sv_socket.bind(('127.0.0.1', 8092))

    sv_socket.listen(5)
    print('启动服务器，等待客户端的连接......')

    while True:
        acc_socket, addr = sv_socket.accept()
        t = threading.Thread(target=tcp_link, args=(acc_socket, addr))
        t.start()
