#print('hello world')

#nick.tweet
#token = 2178503649-kqpfuLJ64sDWPojjgNT47MreT522yfQUsadxWzk
#token secret = 4nS8MA96g3DpmK4oCXpBhsS5Ehz2s2xcIaj10ircQ0VjZ
#api key= C2WeweCvU8DilvziKTrbNadB7
#API secret= DVs4pZ4yEXPQzdNWsN13tZrcHxXboC1g7DdQNVWF9KP3PmTgqz
# authentication


import tweepy
TOKEN = '2178503649-kqpfuLJ64sDWPojjgNT47MreT522yfQUsadxWzk'
TOKEN_SECRET = '4nS8MA96g3DpmK4oCXpBhsS5Ehz2s2xcIaj10ircQ0VjZ'
CONSUMER_KEY = 'C2WeweCvU8DilvziKTrbNadB7'
CONSUMER_SECRET = 'DVs4pZ4yEXPQzdNWsN13tZrcHxXboC1g7DdQNVWF9KP3PmTgqz'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(CONSUMER_KEY,TOKEN_SECRET)

api = tweepy.API(auth)

for tweet in api.search(q="basketball", lang="en", rpp=10):
    print(f"{tweet.user.name}: {tweet.text}")