# !/usr/bin/python
# -*- coding: utf-8 -*-
import asyncio
import os
import time
import math
from tqdm import tqdm
from aiohttp import ClientSession

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
size = 10241000 * 10  # 分割的每个视频长度


def get_range(content_length):
    """
    :param content_length: 视频长度
    :return: 请求头：Range
    """
    # count = int(content_length) // size  # 分割成几个视频
    count = math.ceil(int(content_length) / size)
    range_list = []
    for i in range(count):
        start = i * size

        if i == count - 1:
            end = content_length
        else:
            end = start + size
        if i > 0:
            start += 1
        rang = {'Range': f'bytes={start}-{end}'}
        range_list.append(rang)
    return range_list


async def async_main(video_url, section_path):
    """
    分割视频，即设置请求头
    :param video_url: 视频地址
    :param section_path: 保存位置
    """
    async with ClientSession() as session:
        async with session.get(video_url, headers=headers) as resp:
            content_length = resp.headers['Content-Length']  # 获取视频长度
            range_list = get_range(content_length)
            sem = asyncio.Semaphore(80)  # 限制并发数量
            if not os.path.exists(section_path):
                os.mkdir(section_path)

            # 进度条
            with tqdm(desc="Process", total=int(content_length), unit='', unit_scale=True, colour="green") as bar:
                down_list = os.listdir(section_path)
                tasks = []
                for i, headers_range in enumerate(range_list):
                    # 判断是否已经下载
                    if f'{section_path}/{i}' not in down_list:
                        headers_range.update(headers)
                        task = down_f(session, video_url, headers_range, i, section_path, sem, bar)
                        tasks.append(task)
                    else:
                        bar.update(size)
                await asyncio.gather(*tasks)


async def down_f(session, video_url, headers_range, i, section_path, sem, bar):
    """
    下载
    """
    async with sem:  # 限制并发数量
        async with session.get(video_url, headers=headers_range) as resp:
            chunks = ""
            async for chunk in resp.content.iter_chunked(1024):
                chunks += chunk

            with open(f'{section_path}/{i}', 'wb') as f:
                f.write(chunks)
                bar.update(size)  # 更新进度条


def main(video_url, section_path):
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(async_main(video_url, section_path))
    loop.run_until_complete(task)


def file_merge(path, path_name):
    """
    :param path: 小段视频保存文件夹路径
    :param path_name: 合并后保存位置+视频名字+格式
    """
    ts_list = os.listdir(path)
    ts_list.sort()
    print(ts_list)
    with open(path_name, mode='ab+') as fw:
        for i in range(len(ts_list)):
            # 小段视频路径
            path_name_i = os.path.join(path, f'{i}')
            with open(path_name_i, mode='rb') as fr:
                buff = fr.read()
                fw.write(buff)
            # 删除文件
            os.remove(path_name_i)
    print('合并完成：', path)


if __name__ == '__main__':
    start_time = time.time()
    url = 'https://pic.ibaotu.com/00/51/34/88a888piCbRB.mp4'
    path = './test2'
    main(url, path)
    end_time = time.time()
    print(f"下载完成,共花费了{end_time - start_time}")

    file_merge('./test2', './test2/merge.mp4')
