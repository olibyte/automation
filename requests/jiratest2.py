import requests
import time
import json
from jira import JIRA

import base64
cred =  "Basic " + base64.b64encode(b'').decode("utf-8")
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization": cred
}

curl -D- -u fred:fred -X PUT --data {see below} -H "Content-Type: application/json" http://kelpie9:8081/rest/api/2/issue/QA-31

{
   "fields": {
       "assignee":{"name":"harry"}
   }
}
url = "https://uomouajv.atlassian.net/rest/api/3/issue/37168/assignee"
data = json.dumps({"name":'oliver.bennett'})
r = requests.put(url, data, auth=(''), headers=headers)
print(r.status_code)
# requests.put(url='https://uomouajv.atlassian.net/rest/api/3/issue/37168/assignee', json={"name":"-1"})
# jira = 'https://uomouajv.atlassian.net'

# all_canvas_id = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project+%3D+CSM+AND+issuetype+%3D+Subject+AND+status+in+%28%221.+Selected+for+Action%22%2C+Backlog%29+AND+resolution+%3D+Unresolved+AND+%22Auto+Migration+Status%22+%3D+Success+AND+Faculty+in+%28%22Architecture%2C+Building+and+Planning%22%2C+%22Medicine%2C+Dentistry+and+Health+Sciences%22%29+ORDER+BY+priority+DESC&fields=customfield_12266'
# all_bb_id = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project+%3D+CSM+AND+issuetype+%3D+Subject+AND+status+in+%28%221.+Selected+for+Action%22%2C+Backlog%29+AND+resolution+%3D+Unresolved+AND+%22Auto+Migration+Status%22+%3D+Success+AND+Faculty+in+%28%22Architecture%2C+Building+and+Planning%22%2C+%22Medicine%2C+Dentistry+and+Health+Sciences%22%29+ORDER+BY+priority+DESC&fields=customfield_12231'
# try:
    # requests.put(['https://uomouajv.atlassian.net/rest/api/3/CSM-7729/assignee'], data=json.dumps({'name':'shane.smits'}))