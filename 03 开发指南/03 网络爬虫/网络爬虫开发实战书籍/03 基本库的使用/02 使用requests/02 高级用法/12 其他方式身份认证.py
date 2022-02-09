"""
https://requests-oauthlib.readthedocs.org/
"""
import requests
from requests_oauthlib import OAuth1

# 需要安装pip install requests_oauthlib


url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(
    'YOUR_APP_KEY',
    'YOUR_APP_SECRET',
    'USER_OAUTH_TOKEN',
    'USER_OAUTH_TOKEN_SECRET'
)

requests.get(url, auth=auth)
