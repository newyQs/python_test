"""

"""
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

m = MultipartEncoder(
    fields={
        'field0': 'value',
        'field1': 'value',
        'field2': ('filename', open('file.txt', 'rb'), 'text/plain')
    }
)

resp = requests.post('http://httpbin.org/post', data=m, headers={'Content-Type': m.content_type})

print(resp.text)
