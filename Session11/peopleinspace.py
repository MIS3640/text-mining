import urllib.request
import json
import pprint
 
url = "http://api.open-notify.org/astros.json"
 
with urllib.request.urlopen(url) as f:  
    response_text = f.read().decode('utf-8')
    j = json.loads(response_text)
    pprint.pprint(j)
    




# How many people are in the space?
d = {"people": [{"craft": "ISS", "name": "Andrew Morgan"}, {"craft": "ISS", "name": "Oleg Skripochka"}, {"craft": "ISS", "name": "Jessica Meir"}], "message": "success", "number": 3}
# for i in d: 
#     print(i)
print(j['number'])
print(len(j['people']))


# Who are they?
for i in j['people']: 
    print(person['name'])


# What craft(s) are they in?