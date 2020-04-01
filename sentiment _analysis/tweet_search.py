import nltk
import matplotlib.pyplot
import json
import twitter_credentials # this file has my twitter API credentials: consumer key, consumer secret, access token, access secret.
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator # to run a wordcloud you need the proper software installed in system (I have visual studio)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# the general format for this code was found referencing the tweepy documentation.
 
auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret) # authentication object
auth.set_access_token(twitter_credentials.token, twitter_credentials.token_secret) # setting the access token & access token secret 



search = input("enter term(s) or hashtag(s) to search:  ") 
number_tweets_analyze = int(input("how many tweets would you like to analyze?  "))
date_since = input("from what date would you like to search (yyyy-mm-dd)?  ")





api = tweepy.API(auth, wait_on_rate_limit = True) # creating API object that uses auth info
tweets = tweepy.Cursor(api.search, q = search + "-filter:retweets" + "-filter:links", lang = "en", since = date_since).items(number_tweets_analyze) # this ultizes tweepy to extract tweets using critera


aggregated_tweet = ''
for tweet in tweets: 
    """
    this is a basic for loop to iterate over the output 
    from the tweets var to print the tweets. 
    """
    print(tweet.text)
    print()
    aggregated_tweet += tweet.text # this iterates to create one long tweet to analyze


# tweets_word_list = aggregated_tweet.split('/n') # convert str to list


analysis = SentimentIntensityAnalyzer() # this is a tool from the VADERsentiment module
vs = analysis.polarity_scores(aggregated_tweet)
# print(vs)

def get_tweet_sentiment():
    '''
    this is a function to return the levels of sentiment 
    aggreaged into categories as per the VADERSentiment 
    source code.
    '''
    score = analysis.polarity_scores(vs)
    lb = score['compound'] # this is the best metric 
    if lb >= 0.05:
        return int(1)
    elif lb <= -0.05:
        return int(-1)
    else:
        return int(0)
        
   
print(vs)
print(get_tweet_sentiment())   
   


  





# output_data = aggregated_tweet

# stopwords = set(STOPWORDS)

# def word_cloud(data, title = "Search worldcloud"):
#     wordcloud = WordCloud(
#         background_color='white',
#         stopwords=stopwords,
#         max_words=200,
#         max_font_size=40,
#         scale=3
#     ).generate(str(data))

#     fig = plt.figure(1, figsize = (20,30))
#     plt.axis('off')
#     if title:
#         fig.suptitle(title, fontsize=20)
#         fig.subplots_adjust(top=2.3)

#     plt.imshow(wordcloud)
#     plt.show()

#     word_cloud(output_data.dropna())

    

