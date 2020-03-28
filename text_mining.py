from imdbpie import Imdb
import random

imdb = Imdb()
parasite = (imdb.search_for_title("Parasite")[0])
reviews = imdb.get_title_user_reviews("tt6751668")

joker = (imdb.search_for_title("Joker")[0])
review2 = imdb.get_title_user_reviews("tt7286456")


unplanned = (imdb.search_for_title("Unplanned")[0])
review3 = imdb.get_title_user_reviews("tt9024106")

thegodfather = (imdb.search_for_title("The Godfather")[0])
reviews3 = imdb.get_title_user_reviews("tt0068646")

disastermovie = (imdb.search_for_title("Disaster Movie")[0])
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
        p.append(n['reviewText'])
    return p


parasitereviews = printreviews(reviews)
parasitereviews = ",".join(parasitereviews)
# print(parasitereviews)

jokerreviews = printreviews(review2)
jokerreviews = ",".join(jokerreviews)
# print(jokerreviews)

unplannedreviews = printreviews(review3)
unplannedreviews = ",".join(unplannedreviews)
# print(unplannedreviews)

godfather = printreviews(reviews3)
godfather = ",".join(godfather)
# print(godfather)

DisasterMovie = printreviews(reviews2)
DisasterMovie = ",".join(DisasterMovie)
# print(DisasterMovie)

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


score = SentimentIntensityAnalyzer().polarity_scores(parasitereviews)
# print(score)

score2 = SentimentIntensityAnalyzer().polarity_scores(jokerreviews)
# print(score2)

score3 = SentimentIntensityAnalyzer().polarity_scores(unplannedreviews)
# print(score3)

score5 = SentimentIntensityAnalyzer().polarity_scores(godfather)
# print(score5)

score4 = SentimentIntensityAnalyzer().polarity_scores(DisasterMovie)
# print(score4)


print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {parasite['title']} | Year: {parasite['year']} ")
print()
print(f"The Positive Valence for this movie is {score['pos']}")
print(f"The Negative Valence for this movie is {score['neg']}")
print(f"The Neutral Valence for this movie is {score['neu']}")
print(f"The Compoud for this movie is {score['compound']}")
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {joker['title']} | Year: {joker['year']} ")
print()
print(f"The Positive Valence for this movie is {score2['pos']}")
print(f"The Negative Valence for this movie is {score2['neg']}")
print(f"The Neutral Valence for this movie is {score2['neu']}")
print(f"The Compoud for this movie is {score2['compound']}")
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {unplanned['title']} | Year: {unplanned['year']} ")
print()
print(f"The Positive Valence for this movie is {score3['pos']}")
print(f"The Negative Valence for this movie is {score3['neg']}")
print(f"The Neutral Valence for this movie is {score3['neu']}")
print(f"The Compoud for this movie is {score3['compound']}")
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {thegodfather['title']} | Year: {thegodfather['year']} ")
print()
print(f"The Positive Valence for this movie is {score5['pos']}")
print(f"The Negative Valence for this movie is {score5['neg']}")
print(f"The Neutral Valence for this movie is {score5['neu']}")
print(f"The Compoud for this movie is {score5['compound']}")
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {disastermovie['title']} | Year: {disastermovie['year']} ")
print()
print(f"The Positive Valence for this movie is {score4['pos']}")
print(f"The Negative Valence for this movie is {score4['neg']}")
print(f"The Neutral Valence for this movie is {score4['neu']}")
print(f"The Compoud for this movie is {score4['compound']}")
print()
print("---------------------------------------------------------------------------------------------------------------------------")


