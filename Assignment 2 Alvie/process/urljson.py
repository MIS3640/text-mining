import urllib.request
import json
import pprint


test2url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track=Bad%20Guy&q_artist=Billie%20Eilish&apikey=8060543fd6419371cfd33da85085cf02"
test1url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track=A%20Lot&q_artist=21%20Savage%20feat.%20J.%20Cole&apikey=8060543fd6419371cfd33da85085cf02"
songName = "High%A%20Lot"
artist = "21%20Savage%20feat.%20J.%20Cole"
apikey = "8060543fd6419371cfd33da85085cf02"
url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track=" + songName + "&q_artist=" + artist + "&apikey=" + apikey

# url = test1url
print(url)

with urllib.request.urlopen(url) as p:  
    # response_text = f.read().decode('utf-8')
    data = json.load(p)
	# pprint.pprint(data)

# print(data)
# print(data.get('message'))
# pprint.pprint(data.get('message'))
pprint.pprint(data['message']['body']['lyrics'])
# print(len(data['message']['body']['lyrics']['explicit']))
explicit = data['message']['body']['lyrics']['explicit'] #No 0, Yes 1
lyrics = data['message']['body']['lyrics']['lyrics_body']
print(explicit)
print(lyrics)