import json

json_data = open('requests\jira\JiraJsonData.json').read()
data = json.loads(json_data)