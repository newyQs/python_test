import urllib.request

response = urllib.request.urlopen('https://www.python.org')

print(type(response))  # <class 'http.client.HTTPResponse'>

print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

# print(dir(response))