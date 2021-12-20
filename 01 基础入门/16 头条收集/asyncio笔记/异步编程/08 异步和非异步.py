"""

"""
import asyncio
import requests


async def download_image(url):
    # 发送网络请求，下载图片（遇到网络下载图片的IO请求，自动的切换到其他任务）
    print("开始下载：", url)

    loops = asyncio.get_event_loop()
    future = loops.run_in_executor(None, requests.get, url)

    resp = await future
    print("下载完成")

    # 图片保存
    file_name = url.rsplit("_")[-1]
    with open(file_name, mode="wb") as f:
        f.write(resp.content)


if __name__ == '__main__':
    url_list = [

    ]

    tasks = [download_image(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
