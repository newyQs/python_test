# 创建客户端socket对象
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 服务端IP地址和端口号元组
server_address = ('127.0.0.1', 1688)
# 客户端连接指定的IP地址和端口号
clientsocket.connect(server_address)

while True:
    # 输入数据
    data = raw_input('please input:')
    if data == "q":
        break
    if not data:
        continue
    # 客户端发送数据
    clientsocket.send(data.encode("utf-8"))
    # 客户端接收数据
    server_data = clientsocket.recv(1024)
    print('客户端收到的数据：', server_data)
# 关闭客户端socket
clientsocket.close()
