"""
{
  "args": {},
  "data": "",
  "files": {
    "file": "data:application/octet-stream;base64,AAAAAA...="
  },
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "6665",
    "Content-Type": "multipart/form-data; boundary=809f80b1a2974132b133ade1a8e8e058",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.10.0",
    "X-Amzn-Trace-Id": "Root=1-61d26f9b-5706757808ed321b3af1f60b"
  },
  "json": null,
  "origin": "60.207.237.16",
  "url": "http://httpbin.org/post"
}
"""
import requests

files = {
    'file': open('favicon.ico', 'rb')
}
resp = requests.post('http://httpbin.org/post', files=files)
print(resp.text)
