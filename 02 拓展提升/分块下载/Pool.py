# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import requests
from multiprocessing.pool import Pool


def get_range_by_chunks(url):
    """获取分割文件的位置"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    size = 10241000 * 10  # 10M
    res = requests.get(url, headers=headers, stream=True)
    content_length = res.headers['Content-Length']  # 141062
    count = int(content_length) // size

    headers_list = []
    for i in range(count):
        start = i * size
        if i == count - 1:
            end = content_length
        else:
            end = start + size
        if i > 0:
            start += 1

        rang = {'Range': f'bytes={start}-{end}'}
        rang.update(headers)
        headers_list.append(rang)
    return headers_list


def exec_download_file(url, headers, i, path):
    """
    :param url: 视频地址
    :param headers: 请求头
    :param i: 小段视频保存名称
    :param path: 保存位置
    """
    content = requests.get(url, headers=headers).content
    with open(f'{path}/{i}', 'wb') as f:
        f.write(content)


def exec_file_merge(path, path_name):
    """
    :param path: 小段视频保存文件夹路径
    :param path_name: 合并后保存位置+视频名字+格式
    """
    ts_list = os.listdir(path)
    ts_list.sort()  # 将小块文件按先后顺序
    print(ts_list)
    with open(path_name, mode='ab+') as fw:
        for i in range(len(ts_list)):
            path_name_i = os.path.join(path, f'{i}')
            with open(path_name_i, mode='rb') as fr:
                buff = fr.read()
                fw.write(buff)
            os.remove(path_name_i)
    print("合并完成：", path)


if __name__ == '__main__':
    start_time = time.time()
    url = 'https://pic.ibaotu.com/00/51/34/88a888piCbRB.mp4'
    header_list = get_range_by_chunks(url)
    path = './test'
    pool = Pool(8)  # 进程池
    if not os.path.exists(path):
        os.mkdir(path)

    for i, headers in enumerate(header_list):
        ts_list = os.listdir(path)
        if f'{i}' not in ts_list:
            pool.apply_async(exec_download_file, args=(url, headers, i, path))

    pool.close()
    pool.join()
    end_time = time.time()
    print(f"下载完成,共花费了{end_time - start_time}")

    exec_file_merge('./test', "./test/merge.mp4")
