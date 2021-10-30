from urllib.parse import parse_qs

query='name=jack&age=22'

print(parse_qs(query))