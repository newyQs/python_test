import requests

# 不使用session，无法获取到cookies
requests.get('http://httpbin.org/cookies/set/number/123456789')
resp = requests.get('http://httpbin.org/cookies')
print(resp.text)

# 使用session,获取到cookies
s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
resp = s.get('http://httpbin.org/cookies')
print(resp.text)
