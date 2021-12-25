import socket, select
server = socket.socket()
server.bind(("127.03 爬虫基本原理.03 爬虫基本原理.1", 1688))
server.listen(5)
msgs = []
fd_socket = {server.fileno(): server}
epoll = select.epoll()

# 注册服务器的 写就绪
epoll.register(server.fileno(), select.EPOLLIN)

while True:
    for fd, event in epoll.poll():
        sock = fd_socket[fd]
        print(fd, event)
        # 返回的是文件描述符 需要获取对应socket
        if sock == server:  # 如果是服务器 就接受请求
            client, addr = server.accept()
            # 注册客户端写就绪
            epoll.register(client.fileno(), select.EPOLLIN)
            # 添加对应关系
            fd_socket[client.fileno()] = client
        # 读就绪
        elif event == select.EPOLLIN:
            data = sock.recv(2018).decode("utf-8")
            if not data:
                # 注销事件
                epoll.unregister(fd)
                # 关闭socket
                sock.close()
                # 删除socket对应关系
                del fd_socket[fd]
                print(" somebody fuck out...")
                continue

            print(data.decode("utf-8"))
            # 读完数据 需要把数据发回去所以接下来更改为写就绪=事件
            epoll.modify(fd, select.EPOLLOUT)
            # 记录数据
            msgs.append((sock,data.upper()))
        elif event == select.EPOLLOUT:
            for item in msgs[:]:
                if item[0] == sock:
                    sock.send(item[1].encode("utf-8"))
                    msgs.remove(item)
            # 切换关注事件为写就绪
            epoll.modify(fd,select.EPOLLIN)