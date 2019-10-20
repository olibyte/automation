# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
email = ''
token = ''
url = "https://uomouajv.atlassian.net/rest/api/3/project/{ProjectID}/role/{userID}"

auth = HTTPBasicAuth(email, token)

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))