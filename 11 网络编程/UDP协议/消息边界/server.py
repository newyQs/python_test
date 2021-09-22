import socket

sv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字
sv_socket.bind(('127.0.0.1', 8889))  # 绑定的 IP 和端口
while True:
    # 接收数据:
    input("输入任何字符开始接收数据......")
    client_data, server_addr = sv_socket.recvfrom(1024)  # 接收客户端信息
    client_data = client_data.decode("utf-8")  # 解码字节流
    if client_data == "exit":  # 判断服务器是否申请结束会话
        break
    print(client_data)

sv_socket.close()
