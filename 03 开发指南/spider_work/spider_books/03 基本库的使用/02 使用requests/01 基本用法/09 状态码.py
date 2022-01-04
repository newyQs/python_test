import requests

r = requests.get('http://www.jianshu.com')
if not r.status_code == requests.codes.ok:
    exit()
else:
    print('Request Successfully')
