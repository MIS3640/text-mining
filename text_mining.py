from imdbpie import Imdb
import random

imdb = Imdb()
print(imdb.search_for_title("Parasite")[0])
reviews = imdb.get_title_user_reviews("tt6751668")

print(imdb.search_for_title("Joker")[0])
review2 = imdb.get_title_user_reviews("tt7286456")


print(imdb.search_for_title("Unplanned")[0])
review3 = imdb.get_title_user_reviews("tt9024106")

print(imdb.search_for_title("The Godfather")[0])
reviews3 = imdb.get_title_user_reviews("tt0068646")

print(imdb.search_for_title("Disaster Movie")[0])
reviews2 = imdb.get_title_user_reviews("tt1213644")


# print(reviews)
# import pprint
# pprint.pprint(reviews)
# pprint.pprint(review2)
# pprint.pprint(review3)
# pprint.pprint(reviews3)
# pprint.pprint(reviews2)


# print(reviews['reviews'][0:]['author']['displayName'])
# print(reviews['reviews'][0]['reviewText'])


def printreviews(reviews):
    p = []
    for n in reviews['reviews']:
        p.append(random.choice(n['reviewText']))
    return p


parasitereviews = printreviews(reviews)
parasitereviews = ",".join(parasitereviews)
print(parasitereviews)

jokerreviews = printreviews(review2)
jokerreviews = ",".join(jokerreviews)
print(jokerreviews)

unplannedreviews = printreviews(review3)
unplannedreviews = ",".join(unplannedreviews)
print(unplannedreviews)

godfather = printreviews(reviews3)
godfather = ",".join(godfather)
print(godfather)

DisasterMovie = printreviews(reviews2)
DisasterMovie = ",".join(DisasterMovie)
print(DisasterMovie)

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


score = SentimentIntensityAnalyzer().polarity_scores(parasitereviews)
print(score)

score2 = SentimentIntensityAnalyzer().polarity_scores(jokerreviews)
print(score2)

score3 = SentimentIntensityAnalyzer().polarity_scores(unplannedreviews)
print(score3)

score5 = SentimentIntensityAnalyzer().polarity_scores(godfather)
print(score5)

score4 = SentimentIntensityAnalyzer().polarity_scores(DisasterMovie)
print(score4)
