import requests
import time
import json
import jira

test_can = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20%222.%20Comparative%20Check%20%26%20Fixes%22%20AND%20resolution%20%3D%20Unresolved%20AND%20%22Auto%20Migration%20Status%22%20%3D%20Success%20AND%20Faculty%20in%20(%22Architecture%2C%20Building%20and%20Planning%22%2C%20%22Medicine%2C%20Dentistry%20and%20Health%20Sciences%22)%20AND%20assignee%20in%20(EMPTY%2C%20currentUser())%20ORDER%20BY%20priority%20DESC&fields=customfield_12231'
test_bb = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20%222.%20Comparative%20Check%20%26%20Fixes%22%20AND%20resolution%20%3D%20Unresolved%20AND%20%22Auto%20Migration%20Status%22%20%3D%20Success%20AND%20Faculty%20in%20(%22Architecture%2C%20Building%20and%20Planning%22%2C%20%22Medicine%2C%20Dentistry%20and%20Health%20Sciences%22)%20AND%20assignee%20in%20(EMPTY%2C%20currentUser())%20ORDER%20BY%20priority%20DESC&fields=customfield_12266'

# canvas_id = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20%221.%20Selected%20for%20Action%22%20AND%20resolution%20%3D%20Unresolved%20AND%20%22Auto%20Migration%20Status%22%20%3D%20Success%20AND%20Faculty%20in%20(%22Architecture%2C%20Building%20and%20Planning%22%2C%20%22Medicine%2C%20Dentistry%20and%20Health%20Sciences%22)%20ORDER%20BY%20priority%20DESC&fields=customfield_12231'
# bb_id = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20%221.%20Selected%20for%20Action%22%20AND%20resolution%20%3D%20Unresolved%20AND%20%22Auto%20Migration%20Status%22%20%3D%20Success%20AND%20Faculty%20in%20(%22Architecture%2C%20Building%20and%20Planning%22%2C%20%22Medicine%2C%20Dentistry%20and%20Health%20Sciences%22)%20ORDER%20BY%20priority%20DESC&fields=customfield_12266'
#from bb url parse course id string
bb_url = '' 
#from canvas url parse course id string
canvas_url = ''
import base64
cred =  "Basic " + base64.b64encode(b'').decode("utf-8")
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization": cred
}
time.sleep(2)
canvas_response = requests.get(test_can, headers=headers)
bb_response = requests.get(test_bb, headers=headers)
# print(response.json())

#parsing data
#print each key
canvas_json = canvas_response.json()
canvas_shell_list = []
bb_shell_list = []

# print('Available Canvas source ids:')
for issue in canvas_json['issues']:
    for field in issue['fields']:
        # print(issue['fields'][field])
        canvas_shell_list.append(issue['fields'][field])

# print('Available BB source IDs')
bb_json = bb_response.json()
for issue in bb_json['issues']:
    for field in issue['fields']:
        # print(issue['fields'][field])
        bb_shell_list.append(issue['fields'][field])

print(canvas_shell_list)
print(bb_shell_list)
actionable_canvas = str(len(canvas_shell_list))
actionable_bb = str(len(bb_shell_list))
print('actionable_canvas: ' + actionable_canvas)
print('actionable_bb: ' + actionable_bb)
