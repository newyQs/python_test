import requests

# 不使用session，无法获取到cookies
requests.get('http://httpbin.org/cookies/set/number/123456789')
resp = requests.get('http://httpbin.org/cookies')
print(resp.text)

# 使用session,获取到cookies
sess = requests.session()
sess.get('http://httpbin.org/cookies/set/number/123456789')
resp = sess.get('http://httpbin.org/cookies')
print(resp.text)

# 使用with方式
with requests.session() as session:
    session.get('http://httpbin.org/cookies/set/number/123456789')
    resp = session.get('http://httpbin.org/cookies')
    print(resp.text)
