import threading
import time
import socket


def terminate():
    global flag_running
    flag_running = False


def func():
    sv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
    sv_ipport = ("0.0.0.0", 8889)  # 监听的 ip 和端口
    sv_socket.bind(sv_ipport)  # 绑定服务地址
    sv_socket.listen(5)  # 协议栈缓冲区最大套接字存放个数
    print('启动服务器，等待客户端连接......')

    sv_socket.settimeout(5)  # 设置 5 秒钟收不到网络发来的数据，阻塞出就抛出超时异常，
    while flag_running:
        try:
            server_socket, addr = sv_socket.accept()  # 等待新客户端的连接请求数据
            break
        except socket.timeout:
            print("继续等待连接请求...")
            continue
    return


if __name__ == '__main__':
    flag_running = True
    t = threading.Thread(target=func)
    t.start()

    count = 20
    while count:  # 主线程 20 秒后退出
        count -= 1
        if count == 10:  # count 等于 10 让子线程退出
            terminate()
        time.sleep(1)
