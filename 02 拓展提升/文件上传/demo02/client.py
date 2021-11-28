import socket
import os
import hashlib
import json

sk = socket.socket()
sk.connect(('127.0.0.1', 8000))

md5 = hashlib.md5()
# 上传文件前先检查文件的md5值,如果服务端存在就续传,否则从0开始上传
# 临时文件的名称是md5值,上传成功后修改文件名称为真实文件名称
while True:
    file_name = input('请输入需要上传的文件的名称:').strip()
    # 获取文件的md5值
    with open(file_name, 'rb') as f:
        for line in f:
            md5.update(line)
    md5_value = md5.hexdigest()

    # 获取文件的总大小
    total_size = os.path.getsize(file_name)

    # 组合发送的数据
    dic = {'file_md5_value': md5_value, 'file_total_size': total_size, 'origin_file_name': file_name}
    dic_str_bytes = json.dumps(dic).encode('utf8')
    # 发送数据
    sk.sendall(dic_str_bytes)

    # 判断code值,是否从0开始上传
    has_code_msg = json.loads(sk.recv(1024).decode('utf8'))
    code = has_code_msg['code']
    if code == 1001:
        # 从0开始上传
        try:
            f = open(file_name, 'rb')
            upload_size = 0
            while upload_size < total_size:
                data = f.read(1024)
                sk.sendall(data)
                upload_size += len(data)
                # break # 测试断点
        finally:
            f.close()
    else:
        # 断点续传
        # 先获取已经上传过的大小
        has_send_size = has_code_msg['has_recive_size']
        try:
            f = open(file_name, 'rb')
            upload_size = has_send_size
            f.seek(has_send_size)
            while upload_size < total_size:
                data = f.read(1024)
                sk.sendall(data)
                upload_size += len(data)
        finally:
            f.close()
