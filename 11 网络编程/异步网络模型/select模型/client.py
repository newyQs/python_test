import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9898))

while True:
    data = input("请输入数据：")
    s.send(data.encode("utf-8"))
    try:
        data = s.recv(1024).decode("utf-8")
        print(data)
    except:
        s.close()

s.close()