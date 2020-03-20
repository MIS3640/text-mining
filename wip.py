# Work in Progress

import tweepy

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

alltweets = api.user_timeline(screen_name = "realDonaldTrump", count=200)
tweets = [[tweet.text] for tweet in alltweets]

print(tweets)