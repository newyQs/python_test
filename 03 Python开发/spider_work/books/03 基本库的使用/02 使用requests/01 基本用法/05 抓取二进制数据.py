import requests

resp = requests.get('https://github.com/favicon.ico')
# print(resp.text)
# print(resp.content)

with open('favicon.ico', 'wb') as f:
    f.write(resp.content)
