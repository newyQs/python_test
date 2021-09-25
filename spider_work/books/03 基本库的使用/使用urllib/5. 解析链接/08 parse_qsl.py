from urllib.parse import parse_qsl

query = 'name=jack&age=22'
print(parse_qsl(query))
