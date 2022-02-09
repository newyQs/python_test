import json
import requests
import re
import time
from requests.exceptions import RequestException


def main(offset):
    """程序主入口"""
    # 请求地址，offset这里表示的是分页
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    # 请求页面，返回响应体response
    html = get_one_page(url)
    # 解析页面，按照一定的正则匹配规则，返回一个迭代器函数
    for item in parse_one_page(html):
        print(item)
        # 将解析结果保存至文件中
        write_to_file(item)


def get_one_page(url):
    """获取页面"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.101 Safari/537.36'
        }
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    """解析页面"""
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)  # --> list
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    """存入数据"""
    with open('result.txt', mode='a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    # 这里抓取10页
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
