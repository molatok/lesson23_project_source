import json
import requests

headers = {'content-type': 'application/json'}

url = "http://127.0.0.1:5000/perform_query"

payload = {
    'file_name': 'apache_logs.txt',
    'cmd1': 'filter',
    'value1': 'GET',
    'cmd2': 'map',
    'value2': '0'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.text)


