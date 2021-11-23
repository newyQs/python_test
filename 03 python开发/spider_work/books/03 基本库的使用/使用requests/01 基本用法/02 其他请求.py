import requests

r = requests.post('http://httpbin.org/post')
r1 = requests.put('http://httpbin.org/put')
r2 = requests.delete('http://httpbin.org/delete')
r3 = requests.head('http://httpbin.org/head')
r4 = requests.options('http://httpbin.org/options')

print('post===>', r)
print('put===>', r1)
print('delete===>', r2)
print('head===>', r3)
print('options===>', r4)
