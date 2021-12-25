import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.03 爬虫基本原理.03 爬虫基本原理.1', 9999))

while True:
    client_data = input("请输入数据：")
    s.send(client_data.encode("utf-8"))
    try:
        recv_data = s.recv(1024).decode("utf-8")
        print(recv_data)
    except:
        s.close()
        break

s.close()
