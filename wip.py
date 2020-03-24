# Work in Progress

import tweepy

# Codes availiable in final documentation
access_token = "173816701-5oYZgixJxTAO0dyE1EyYQivHFJqUDi9CqpsNFxXt"
access_token_secret =
consumer_key = "U0S0rabX7Kwhw5mN8phJP5uRa"
consumer_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

alltweets = api.user_timeline(screen_name = "realDonaldTrump", count=200)
tweets = [[tweet.text.lower()] for tweet in alltweets]


for tweet in alltweets:
    print(tweets)