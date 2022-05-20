import socket
import os
import json
import hashlib

sk = socket.socket()
sk.bind(('127.0.0.1', 8000))
sk.listen(5)
conn, addr = sk.accept()

while True:
    # 接受客户端发送的数据,看是否存在存在md5文件名称
    recive_msg = json.loads(conn.recv(1024).decode('utf8'))
    # md5文件名
    md5_file_name = recive_msg['file_md5_value']

    # 文件大小
    file_total_size = recive_msg['file_total_size']

    # 原始文件大小
    origin_file_name = recive_msg['origin_file_name']

    # 判断文件是否存在,存在的话续传.否则从0开始传
    is_exists = os.path.exists('./upload/' + md5_file_name)
    if not is_exists:
        # 从0开始上传
        conn.sendall(json.dumps({'code': 1001, 'msg': '从0开始上传'}).encode('utf8'))
        # 接受从客户端传来的数据
        recive_size = 0
        f = open('./upload/' + md5_file_name, 'wb')
        while recive_size < file_total_size:
            data = conn.recv(1024)
            f.write(data)
            # 主动将内存中的数据刷到到文件中去
            f.flush()
            recive_size += len(data)
        f.close()
        # 上传完毕后,修改文件的文件名为原始文件名
        if os.path.getsize('./upload/' + md5_file_name) == file_total_size:
            os.rename('./upload/' + md5_file_name, './upload/' + origin_file_name)
    else:
        # 断点续传, （先把已经接收到的文件的大小发送给客户端）
        # 已接收到的大小
        has_receive_size = os.path.getsize('./upload/' + md5_file_name)
        conn.sendall(json.dumps({'code': 1002, 'msg': '断点续传', 'has_recive_size': has_receive_size}).encode('utf8'))

        receive_size = has_receive_size
        f = open('./upload/' + md5_file_name, 'ab')
        while receive_size < file_total_size:
            data = conn.recv(1024)
            f.write(data)
            # 主动将内存中的数据刷到到文件中去
            f.flush()
            receive_size += len(data)
        f.close()

        # 上传完毕后,修改文件的文件名为原始文件名
        if os.path.getsize('./upload/' + md5_file_name) == file_total_size:
            os.rename('./upload/' + md5_file_name, './upload/' + origin_file_name)
    break
conn.close()
sk.close()
