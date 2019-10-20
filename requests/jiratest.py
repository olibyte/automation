import requests
import time
import json

canvas_id = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20%221.%20Selected%20for%20Action%22%20AND%20resolution%20%3D%20Unresolved%20AND%20%22Auto%20Migration%20Status%22%20%3D%20Success%20AND%20Faculty%20in%20(%22Architecture%2C%20Building%20and%20Planning%22%2C%20%22Medicine%2C%20Dentistry%20and%20Health%20Sciences%22)%20ORDER%20BY%20priority%20DESC&fields=customfield_12231'
bb_id = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20%221.%20Selected%20for%20Action%22%20AND%20resolution%20%3D%20Unresolved%20AND%20%22Auto%20Migration%20Status%22%20%3D%20Success%20AND%20Faculty%20in%20(%22Architecture%2C%20Building%20and%20Planning%22%2C%20%22Medicine%2C%20Dentistry%20and%20Health%20Sciences%22)%20ORDER%20BY%20priority%20DESC&fields=customfield_12266'
# response = requests.get(url)
# print(response.json())
import base64
cred =  "Basic " + base64.b64encode(b'me@me.com:ACCESSTOKEN').decode("utf-8")
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization": cred
}
time.sleep(2)
canvas_response = requests.get(canvas_id, headers=headers)
bb_response = requests.get(bb_id, headers=headers)
# print(response.json())

#parsing data
#print each key
canvas_json = canvas_response.json()

# status_counts = {}
# for project in my_json['projects']:
for issue in canvas_json['issues']:
    for field in issue['fields']:
        print(issue['fields'][field])

bb_json = bb_response.json()
for issue in bb_json['issues']:
    for field in issue['fields']:
        print(issue['fields'][field])
        