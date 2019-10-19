import requests
import time

url = 'https://api.github.com/user'
response = requests.get(url)
print(response.json())

time.sleep(2)
#github developer settings, generate token
response = requests.get(url, headers={'Authorization': 'Bearer 1d292656fce9ce91c5e9233e8788f2eff0b0d9e3'})
print(response.json())