# Work in Progress

import tweepy

access_token = "173816701-JsK4FaBfB84E5XJPbq0jDeRYLCHFs5n2UASWqK8l"
access_token_secret = "NJDi1dK0VJJnKGGnYaSkqoRjbncXV3CLbRj92nw6x3Hby"
consumer_key = "U0S0rabX7Kwhw5mN8phJP5uRa"
consumer_secret = "vsRLlAGVdOEKQ4BGBJdi5jouQwlz1J7HRPV2vaBFRM95M3iisq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

alltweets = api.user_timeline(screen_name = "realDonaldTrump", count=200)
tweets = [[tweet.text] for tweet in alltweets]

print(tweets)