import pprint
import json


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


compareOutputs()


