"""

"""
import requests
from requests.auth import HTTPBasicAuth

# 在访问网站的时候，可能会跳出身份验证页面
# 此时使用requests自带的身份验证功能
resp = requests.get(
    'http://localhost:5000', auth=HTTPBasicAuth('username', 'password') # 简写：auth=('username', 'password')
)
print(resp.status_code)
