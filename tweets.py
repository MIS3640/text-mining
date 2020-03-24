import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'AczBVcVl7W1kIqoEwKjZa34jO'
consumer_secret = 'sjWqaeCKqBghkxqYLOYKZWKMz8LM6i3K0YMn5Lhw6Zn1KRySqy'
access_token = '1873709048-bsx9JjSvNQv7vEtZLcufaHEMzjLUJLIvc7BwOkQ'
access_token_secret = 'aIpz3h7axzJhLobZjfhLrXchdvhQZOyyXgBk9WX0smcSY'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# # Step 2 - Retrieve Tweets
public_tweets = api.search('Red Sox')

print(public_tweets)