"""
http://httpbin.org/
"""
import requests

resp = requests.get("http://httpbin.org/json")

# with open("./t.png", mode="wb") as f:
#     f.write(resp.content)

print(resp.text)
