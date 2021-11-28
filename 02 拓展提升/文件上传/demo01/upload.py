import os
import sys
import json
import time
import math
import hashlib
import requests

host_name = "http://abc.example.com"


class UploadFileSection:
    def __init__(self):
        self.user_id = '456414806'
        self.user_token = 'jeWeclbMoKXiipaUkYa1F4PsadOyyyoZ'

    def do_upload_slice(self, file_path, offset, size, file_name, file_md5, file_total_size, is_end):
        url = host_name + '/api/file/fileuploadSection'
        post_data = {
            'userID': self.user_id,
            'userToken': self.user_token,
            'fileName': file_name,  # file的名字无效，这里重新告诉服务器文件的名字
            'fileMd5': file_md5,
            'fileOffset': offset,
            'fileTotalSize': file_total_size,
            'isEnd': is_end
        }

        target_file = open(file_path, 'rb')
        target_file.seek(offset)
        files = {
            'binaryFile': target_file.read(size)  # 文件名无效，这里是纯二进制数据
        }
        target_file.close()

        try:
            print('requests begin', url, file_path)
            print(json.dumps(post_data, indent=2))
            response = requests.post(url, data=post_data, files=files)
            data = json.loads(response.content)
            print(json.dumps(data, ensure_ascii=False, indent=2))
            if data['statusCode'] == 0:
                print(time.strftime("%Y-%m-%d %H:%M:%S"), sys._getframe().f_code.co_name, " success")
                return True
            else:
                print(time.strftime("%Y-%m-%d %H:%M:%S"), sys._getframe().f_code.co_name, " failed")
                return False
        except Exception as e:
            print(time.strftime("%Y-%m-%d %H:%M:%S"), sys._getframe().f_code.co_name, " get except ", e)
            print(response.content)
            exit()
            return False

    def do_upload(self, file_path):
        file_total_size = os.path.getsize(file_path)
        chunk_size = 3000
        chunks = math.ceil(file_total_size / chunk_size)
        file_path = file_path.replace('\\', '/')
        file_names = file_path.split('/')
        file_name = file_names[-1]
        file_md5 = self.get_file_md5(file_path)

        print('file', file_path, 'size', file_total_size, 'chunk_size', chunk_size, 'chunks', chunks)

        for i in range(chunks):
            print('chunk', i)
            if i + 1 == chunks:
                is_end = 1
                current_size = file_total_size % chunk_size
            else:
                is_end = 0
                current_size = chunk_size

            self.do_upload_slice(file_path, i * chunk_size, current_size, file_name, file_md5, file_total_size, is_end)

    @staticmethod
    def get_file_md5(file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                data = f.read()
                return hashlib.md5(data).hexdigest()
        else:
            print(file_path, " doesn't exist, no md5")
            return ""


if __name__ == "__main__":
    work = UploadFileSection()
    work.do_upload('d:/abc.jpg')

"""
原理：
1.request每次读取部分文件内容上传，这样文件的名字，大小就要用另外的参数来表示了
2.后端需要在接收到文件后，根据md5，文件大小，文件名判断该追加写入哪个临时文件，当文件传输完毕后，将临时文件move到指定位置进行处理
"""
