import nltk
import matplotlib.pyplot
import twitter_credentials # this file has my twitter API credentials: consumer key, consumer secret, access token, access secret.
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator # to run a wordcloud you need the proper software installed in system (I have visual studio)
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# the general format for this code was found referencing the tweepy documentation.
# this function will be called later to find the average polarity scores after iterating totals

def percentage(part, whole):
    return 100 * float(part)/float(whole)


auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret) # authentication object
auth.set_access_token(twitter_credentials.token, twitter_credentials.token_secret) # setting the access token & access token secret 
api = tweepy.API(auth) # creating API object that uses auth info

# search and input criteria 

search = input("enter term(s) or hashtag(s) to search:  ") 
number_tweets_analyze = int(input("how many tweets would you like to analyze?  "))
date_since = input("from what date would you like to search (yyyy-mm-dd)?  ")

# this is the search var

tweets = tweepy.Cursor(api.search, q = search + "-filter:retweets" + "-filter:links", lang = "en", since = date_since).items(number_tweets_analyze) # this ultizes tweepy to extract tweets using critera

# defining these variables to iterate over later

positive = 0
negative = 0
neutral = 0
polarity = 0


# this is a forloop to print the tweets and run the textblob polarity analysis 
for t in tweets:
    analysis = TextBlob(t.text)
    polarity += analysis.sentiment.polarity
    print(t.text)
    print()
    print(analysis.sentiment.polarity)
    print()
    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

# these variables call the percentage function to divide the cumulative polarity scores by the number of tweets analyzed. 
positive = percentage(positive, number_tweets_analyze)
negative = percentage(negative, number_tweets_analyze)
neutral = percentage(neutral, number_tweets_analyze)
polarity = percentage(polarity, number_tweets_analyze)

# to two decimals 
positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print('General Sentiment for  ' + search + ' by analyzing ' + str(number_tweets_analyze)+ ' tweets.')

# uses the cumulative polarity to return the general sentiment of the sample 
if (polarity == 0):
    print('general sentiment is neutral')
elif(polarity < 0):
    print('general sentiment is negative')
elif(polarity > 0):
    print('general sentiment is positive')

# code for pie chart https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html

labels = ['Positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]', 'Neutral [' + str(neutral) + '%]']
sizes = [positive, neutral, negative]
colors =['yellow', 'red', 'blue']

patches, texts = plt.pie(sizes, colors = colors, startangle = 90)
plt.legend(patches, labels, loc ="best")
plt.title('General Sentiment for  ' + search + ' by analyzing ' + str(number_tweets_analyze)+ ' tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()





