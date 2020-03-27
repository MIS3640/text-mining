from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("Parasite")[0])
reviews = imdb.get_title_user_reviews("tt6751668")

import pprint
pprint.pprint(reviews)

print(reviews['reviews'][0]['author']['displayName'])
print(reviews['reviews'][0]['reviewText'])

from nltk.sentiment.vader import SentimentIntensityAnalyzer

score = SentimentIntensityAnalyzer().polarity_scores(reviews)
print(score)