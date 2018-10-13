import requests

# print("hello world")

url = 'http://127.0.0.1:5000/HelloWorld'
urlUserCreate = 'http://127.0.0.1:5000/api/register'
expectedStatus = 200
# expectedText = {"hello": "world"}

print(requests.get(url).status_code)
assert requests.get(url).status_code == expectedStatus

print(requests.get(urlUserCreate).status_code)
assert requests.get(urlUserCreate).status_code == expectedStatus