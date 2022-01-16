"""

"""
import os
import sys
import json
import time
import math
import hashlib

import requests

from log import log

hostName = "http://abc.example.com"


class uploadFileSection:
    def __init__(self):
        self.user_id = '456414806'
        self.user_token = 'jeWeclbMoKXiipaUkYa1F4PsadOyyyoZ'

    def do_upload_slice(self, file_path, offset, size, file_name, file_md5, file_total_size, is_end):
        url = hostName + '/api/file/fileuploadSection'
        postData = {
            'userID': self.user_id,
            'userToken': self.user_token,
            'fileName': file_name,  # file的名字无效，这里重新告诉服务器文件的名字
            'fileMd5': file_md5,
            'fileOffset': offset,
            'fileTotalSize': file_total_size,
            'isEnd': is_end
        }

        targetFile = open(file_path, 'rb')
        targetFile.seek(offset)
        files = {
            'binaryFile': targetFile.read(size)  # 文件名无效，这里是纯二进制数据
        }
        targetFile.close()

        try:
            print('requests begin', url, file_path)
            print(json.dumps(postData, indent=2))
            response = requests.post(url, data=postData, files=files)

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

    def getFileMd5(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                data = f.read()
                return hashlib.md5(data).hexdigest()
        else:
            print(file_path, " doesn't exist, no md5")
            return ""

    def do_upload(self, file_path):
        file_total_size = os.path.getsize(file_path)
        chunk_size = 3000
        chunks = math.ceil(file_total_size / chunk_size)
        file_path = file_path.replace('\\', '/')
        file_names = file_path.split('/')
        file_name = file_names[-1]
        file_md5 = self.getFileMd5(file_path)

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


if __name__ == "__main__":
    work = uploadFileSection()
    work.do_upload('d:/222huojian.jpg')
