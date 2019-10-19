import requests
import time

url = 'https://api.github.com/user'
response = requests.get(url)
print(response.json())

time.sleep(2)
#github developer settings, generate token
response = requests.get(url, headers={'Authorization': 'Bearer 45a412f521310b6fda54fa31622eb56822e799e3'})
print(response.json())

#parsing data

#print each key
my_json = response.json()
for key in my_json.keys():
    print(key)

time.sleep(2)
print('My id: ' + str(my_json['id']))