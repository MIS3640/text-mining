from nltk.sentiment.vader import SentimentIntensityAnalyzer


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
print(explicit)
print(lyrics)

sentence = 'Software Design is my favorite class because learning Python is so cool!'
score = SentimentIntensityAnalyzer().polarity_scores(lyrics)
print(SentimentIntensityAnalyzer().polarity_scores("back"))
print(score)