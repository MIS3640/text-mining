import json
import pprint

with open('test.json', 'r') as p:
	data = json.load(p)
	# pprint.pprint(data)

# print(data)
# print(data.get('message'))
# pprint.pprint(data.get('message'))
pprint.pprint(data['message']['body']['lyrics'])
# print(len(data['message']['body']['lyrics']['explicit']))
explicit = data['message']['body']['lyrics']['explicit'] #No 0, Yes 1
lyrics = data['message']['body']['lyrics']['lyrics_body']
lyrics = lyrics.split("******* This Lyrics is NOT")[0]
print(explicit)
print(lyrics)
