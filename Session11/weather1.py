import urllib.request
import json
import pprint 

APIKEY = '6b983114b7354e5bf22e05a755abedde'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
# pprint.pprint(response_data)
temp= response_data['main']['temp']
print(temp)