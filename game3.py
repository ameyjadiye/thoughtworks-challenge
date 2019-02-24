# importing the requests library 
import requests 
import json
from datetime import datetime

# api-endpoint 
URL = "https://http-hunt.thoughtworks-labs.net/challenge/input"

headers = {'userId': '45_wIXvrl','content-type': 'application/json'}


r = requests.get(url = URL, headers=headers) 

# extracting data in json format 
data = r.json() 

print json.dumps(data, indent=2)

out=0
result={}
for i in data:
    startDate=i['startDate']
    endDate=i['endDate'] if i['endDate'] else '9999-12-31'
    s=datetime.strptime(startDate,'%Y-%m-%d').date()
    e=datetime.strptime(endDate,'%Y-%m-%d').date()
    t=datetime.today().date()
    if s<=t and e>=t:
        if str(i['category']) in result:
            result[str(i['category'])] = result[str(i['category'])] + 1
        else:
            result[str(i['category'])]=1




r = requests.post(url = 'https://http-hunt.thoughtworks-labs.net/challenge/output', json=result, headers=headers)

data = r.json()

print json.dumps(data, indent=2)

