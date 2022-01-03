import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.77 Safari/537.36'
}
resp = requests.get('https://www.zhihu.com/explore', headers=headers)
print(resp.text)
print(resp.content)
