import logging
import requests

logging.captureWarnings(True)
resp = requests.get('https://www.12306.cn', verify=False)
print(resp.status_code)
