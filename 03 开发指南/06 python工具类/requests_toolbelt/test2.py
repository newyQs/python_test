"""

"""
import requests
from requests_toolbelt import MultipartEncoder

# encoder = MultipartEncoder({'field': 'value','other_field': 'other_value'})

# encoder = MultipartEncoder([('field', 'value'), ('other_field', 'other_value')])

encoder = MultipartEncoder({'field': ('file_name', b'{"a": "b"}', 'application/json', {'X-My-Header': 'my-value'})})

r1 = requests.post('https://httpbin.org/post', data=encoder,
                   headers={'Content-Type': encoder.content_type})

# 如果您不需要利用流式传输帖子正文
r2 = requests.post('https://httpbin.org/post',
                   data=encoder.to_string(),
                   headers={'Content-Type': encoder.content_type})

print(r1.text)
# print(r2.text)
