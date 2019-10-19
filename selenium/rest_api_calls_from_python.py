import requests
import time

# url = 'https://jsonplaceholder.typicode.com/photos'
# response = requests.get(url)
# print(response.json())

jsonPayload = {'albumId':1, 'title': 'test', 'url':'nothing.com', 'thumbnailUrl': 'nothing.com'}
# time.sleep(2)
# response = requests.post(url, json=jsonPayload)
# print(response.json())

url = 'https://jsonplaceholder.typicode.com/photos/100'
response = requests.put(url, json=jsonPayload)
print(response.json())

time.sleep(2)

response = requests.delete(url)
print(response.json())
