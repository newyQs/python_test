import requests

r = requests.post('http://httpbin.org/post')
r1 = requests.put('http://httpbin.org/put')
r2 = requests.delete('http://httpbin.org/delete')
r3 = requests.head('http://httpbin.org/head')
r4 = requests.options('http://httpbin.org/options')

print('r===>', r)
print('r1===>', r1)
print('r2===>', r2)
print('r3===>', r3)
print('r4===>', r4)
