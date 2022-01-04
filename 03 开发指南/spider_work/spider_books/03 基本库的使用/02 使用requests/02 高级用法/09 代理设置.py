import requests

# 当大规模请求网站时，网站可能会弹出验证码或者跳转到登录验证页面，甚至会封禁客户端导致无法登录
# 因此，这时候需要使用代理来解决这些问题
# 使用代理
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

proxies = {
    'http': 'http://user:password@10.10.1.10:3128'
}
resp = requests.get('https://www.taobao.com', proxies=proxies)
