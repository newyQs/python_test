import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp的套接字
ss.setblocking(False)  # recv，send，connect，accept 都不是阻塞的
ss.bind(('127.0.0.1', 9999))
ss.listen(5)

sockslist = []  # 存储客户端的套接字

# 每个客户业务执行的时间粒度比较大
# 并发（是一种感觉）
# 异步

while True:
    try:
        server_sock, addr = ss.accept()  # 协议栈缓冲区没有套接字，抛出异常
        sockslist.append(server_sock)  # 来客户端连接把连上的套接字入队列
    except:
        pass

    for sock in sockslist:  # 循环遍历已连上的套接字做读写操作
        try:
            data = sock.recv(1024).decode("utf-8")  # 任务（对接一个客户端一个任务）异步并发（任务）
            if not data:
                print("客户端退出")
                sock.close()
                sockslist.remove(sock)
            else:
                print(data)
                sock.send("hello，我是python服务器".encode("utf-8"))
        except:
            pass
