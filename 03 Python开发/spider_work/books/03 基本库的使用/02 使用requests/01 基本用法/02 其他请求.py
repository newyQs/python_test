import requests

r1 = requests.post('http://httpbin.org/post')
r2 = requests.put('http://httpbin.org/put')
r3 = requests.delete('http://httpbin.org/delete')
r4 = requests.head('http://httpbin.org/head')
r5 = requests.options('http://httpbin.org/options')

print('post===>', r1)
print('put===>', r2)
print('delete===>', r3)
print('head===>', r4)
print('options===>', r5)
