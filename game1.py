# importing the requests library 
import requests 
import json

# api-endpoint 
URL = "https://http-hunt.thoughtworks-labs.net/challenge/input"

headers = {'userId': '45_wIXvrl','content-type': 'application/json'}


r = requests.get(url = URL, headers=headers) 

# extracting data in json format 
data = r.json() 

print json.dumps(data, indent=2)

item=len(data)

data = {'count': item}
outdata = json.dumps(data)

r = requests.post(url = 'https://http-hunt.thoughtworks-labs.net/challenge/output', json={"count": item}, headers=headers)

data = r.json()

print json.dumps(data, indent=2)

