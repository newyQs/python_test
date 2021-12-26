import requests

files = {
    'file': open('favicon.ico', 'rb')
}
resp = requests.post('http://httpbin.org/post', files=files)
import pdb
pdb.set_trace()
