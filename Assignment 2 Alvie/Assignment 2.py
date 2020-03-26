import json
import urllib.request
import json
import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer


songs1969s = {
	# "Year" : "1969",
	"Sugar Sugar" : "The Archies",
	"Aquarius / Let the Sunshine In" : "The Fifth Dimension",
	"I Can't Get Next to You" : "The Temptations",
	"Honky Tonk Women" : "The Rolling Stones",
	"Everyday People" : "Sly and The Family Stone"
}
songs2019s = {
	# "Year" : "2019",
	"Bad Guy" : "Billie Eilish",
	"Truth Hurts" : "Lizzo",
	"Jonas Brothers" : "Sucker",
	"Old Town Road (Remix)" : "Lil Nas X feat. Billy Ray Cyrus",
	"A Lot" : "21 Savage feat. J. Cole"
}

list1songScores = {}
list2songScores = {}

apikey = "8060543fd6419371cfd33da85085cf02"
def compare(list1, list2):
	""""

	"""
	fullList = {}
	# print(list1)
	for song, artist in list1.items():
		# if song == "Year":
		# 	pass
		song = song.replace(" ", "%20")
		artist = artist.replace(" ", "%20")
		fullList[song] = artist
	# print(fullList)
	for song, artist in fullList.items():
		# print(fullList)
		url = f"https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track={song}&q_artist={artist}&apikey={apikey}"

		try:
			with urllib.request.urlopen(url) as p:
			    data = json.load(p)
			explicit = data['message']['body']['lyrics']['explicit'] #No 0, Yes 1
			lyrics = data['message']['body']['lyrics']['lyrics_body']
			lyrics = lyrics.split("******* This Lyrics is NOT")[0]
			score = SentimentIntensityAnalyzer().polarity_scores(lyrics)
			song = song.replace("%20", " ")
			list1songScores[song] = score #, explicit
			list1songScores[song]["explicit"] = explicit
			# break
		except Exception as e:
			# print(e)
			song = song.replace("%20", " ")
			list1songScores[song] = "Unable to determine score as no lyrics are given."
			# break
	with open('List1_Song_Data_Output.json', 'w') as json_file:
		json.dump(list1songScores, json_file)

	fullList = {}
	# print("n")
	# pprint.pprint(list2songScores)
	for song, artist in list2.items():
		song = song.replace(" ", "%20")
		artist = artist.replace(" ", "%20")
		fullList[song] = artist
	# print(fullList)
	for song, artist in fullList.items():
		url = f"https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track={song}&q_artist={artist}&apikey={apikey}"
		try:
			with urllib.request.urlopen(url) as p:
			    data = json.load(p)
			explicit = data['message']['body']['lyrics']['explicit'] #No 0, Yes 1
			lyrics = data['message']['body']['lyrics']['lyrics_body']
			lyrics = lyrics.split("******* This Lyrics is NOT")[0]
			score = SentimentIntensityAnalyzer().polarity_scores(lyrics)
			song = song.replace("%20", " ")
			list2songScores[song] = score
			list2songScores[song]["explicit"] = explicit
			# break
		except Exception as e:
			song = song.replace("%20", " ")
			list2songScores[song] = "Unable to determine score as no lyrics are given."

	with open('List2_Song_Data_Output.json', 'w') as json_file:
		json.dump(list2songScores, json_file)


def compareOutputs():
	with open('List1_Song_Data_Output.json', 'r') as p:
		data1 = json.load(p)

	# pprint.pprint(data1)
	oldSongsNeg = oldSongsPos = oldSongsNeu = oldSongsComp = 0.0
	newSongsNeg = newSongsPos = newSongsNeu = newSongsComp = 0.0
	oldSongsExp = newSongsExp = 0

	for song, rating in data1.items():
		oldSongsNeg += data1[song]["neg"]
		oldSongsPos += data1[song]["pos"]
		oldSongsNeu += data1[song]["neu"]
		oldSongsComp += data1[song]["compound"]
		oldSongsExp += data1[song]["explicit"]

	# print(oldSongsNeg, oldSongsPos, oldSongsNeu, oldSongsComp, oldSongsExp)

	with open('List2_Song_Data_Output.json', 'r') as p:
		data2 = json.load(p)

	for song, rating in data2.items():
		newSongsNeg += data2[song]["neg"]
		newSongsPos += data2[song]["pos"]
		newSongsNeu += data2[song]["neu"]
		newSongsComp += data2[song]["compound"]
		newSongsExp += data2[song]["explicit"]

	# pprint.pprint(data2)

	if oldSongsNeg - newSongsNeg > 0: 
		print(f"The old songs are {oldSongsNeg - newSongsNeg:.3f} more negative than the new songs (old, new: {oldSongsNeg:.3f}, {newSongsNeg:.3f}).")
	else:
		print(f"The new songs are {newSongsNeg- oldSongsNeg:.3f} more negative than the old songs (old, new: {oldSongsNeg:.3f}, {newSongsNeg:.3f}).")


	if oldSongsComp - newSongsComp > 0: 
		print(f"The old songs are {oldSongsComp - newSongsComp:.3f} more compound than the new songs ({oldSongsComp:.3f}, {newSongsComp:.3f}).")
	else:
		print(f"The new songs are {newSongsComp - oldSongsComp:.3f} more compound than the old songs ({oldSongsComp:.3f}, {newSongsComp:.3f}).")


	if oldSongsNeu - newSongsNeu > 0: 
		print(f"The old songs are {oldSongsNeu - newSongsNeu:.3f} more neutrality than the new songs ({oldSongsNeu:.3f}, {newSongsNeu:.3f}).")
	else:
		print(f"The new songs are {newSongsNeu - oldSongsNeu:.3f} more neutrality than the old songs ({oldSongsNeu:.3f}, {newSongsNeu:.3f}).")


	if oldSongsPos - newSongsPos > 0: 
		print(f"The old songs are {oldSongsPos - newSongsPos:.3f} more positive than the new songs ({oldSongsPos:.3f}, {newSongsPos:.3f}).")
	else:
		print(f"The new songs are {newSongsPos - oldSongsPos:.3f} more positive than the old songs ({oldSongsPos:.3f}, {newSongsPos:.3f}).")

	print(f"There are {oldSongsExp} explicit songs from the old music compared to {newSongsExp} of the new songs are explicit out of {len(data2)} songs ({oldSongsExp}, {newSongsExp}).")



compare(list1 = songs1969s, list2 = songs2019s)
# pprint.pprint(list1songScores)

compareOutputs()










