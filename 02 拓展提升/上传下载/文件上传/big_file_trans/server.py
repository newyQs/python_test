#!/usr/bin/env python
# coding=utf-8

import os
from flask import Flask, request, Response, render_template as rt
from flask import json,jsonify
app = Flask(__name__)

file_dir = './upload'
@app.route('/', methods=['GET'])
def index():
    return rt('./index.html')

@app.route('/check',methods=['POST'])   #第一个参数是路由，第二个是请求方法
def check_file():
    recv_data = request.get_data()  #得到前端传送的数据
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        file_list.append(files) #当前路径下所有非目录子文件
    return jsonify({'file_list':file_list }) #返回数据

@app.route('/file/upload', methods=['POST'])
def upload_part():  # 接收前端上传的一个分片
    task = request.form.get('task_id')  # 获取文件的唯一标识符
    chunk = request.form.get('chunk', 0)  # 获取该分片在所有分片中的序号
    filename = '%s%s' % (task, chunk)  # 构造该分片的唯一标识符
    upload_file = request.files['file']
    upload_file.save(file_dir+'/%s' % filename)  # 保存分片到本地
    return rt('./index.html')

@app.route('/file/merge', methods=['GET'])
def upload_success():  # 按序读出分片内容，并写入新文件
    target_filename = request.args.get('filename')  # 获取上传文件的文件名
    task = request.args.get('task_id')  # 获取文件的唯一标识符
    chunk = 0  # 分片序号
    with open(file_dir+'/%s' % target_filename, 'wb') as target_file:  # 创建新文件
        while True:
            try:
                filename = file_dir+'/%s%d' % (task, chunk)
                source_file = open(filename, 'rb')  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
            except(IOError):
                break
            chunk += 1
    chunk = 0  # 分片序号
    while True:
        try:
            filename = file_dir+'/%s%d' % (task, chunk)
            os.remove(filename)  # 删除该分片，节约空间
        except(IOError):
            break
        chunk += 1
    return rt('./index.html')
'''
@app.route('/file/list', methods=['GET'])
def file_list():
    files = os.listdir(file_dir+'/')  # 获取文件目录
    files = map(lambda x: x if isinstance(x) else x.decode('utf-8'), files)  # 注意编码
    return rt('./list.html', files=files)

@app.route('/file/download/<filename>', methods=['GET'])
def file_download(filename):
    def send_chunk():  # 流式读取
        store_path = file_dir+'/%s' % filename
        with open(store_path, 'rb') as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(send_chunk(), content_type='application/octet-stream')
'''
if __name__ == '__main__':
    app.run(debug=False, threaded=True)
