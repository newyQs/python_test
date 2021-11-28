from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'jack'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
