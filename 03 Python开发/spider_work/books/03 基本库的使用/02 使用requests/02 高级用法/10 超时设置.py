import requests

# 设置超时响应时间
# 实际，请求分为连接和读取,timeout为连接和读取时间的总和
# 可以设置一个元组分别指定时间
resp = requests.get('https://ww.taobao.com', timeout=1)  # timeout=(1,1)
print(resp.status_code)
