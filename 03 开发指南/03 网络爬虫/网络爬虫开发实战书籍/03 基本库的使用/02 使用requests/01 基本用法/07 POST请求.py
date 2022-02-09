import requests

data = {
    'name': 'jack',
    'age': 18
}

r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
