<<<<<<< HEAD
print('hello world')

hello
=======
#print('hello world')

#nick.tweet
#token =  2178503649-YShNbZnh5DcCARV4wxSdDrhzkl4N9s4kUG5Xqmv
#token secret = iylb6e9Rd7HoLB1F4Rc8hMCcGXfAuLgzKyMpqsz80Zy4s
#api key= sdT0eSA6CwgwBcbVn5zE0W7HZ
#API secret= gYb5HJ6Xbly0Zf4nFkQSIm3mfjXtREDfKUpb3HGIDDI5GEcqUX
# authentication


import tweepy
TOKEN = '2178503649-HYmo1ucpYKnvDoQOUzfG8UsDFoKE2xpHd9whMfW'
TOKEN_SECRET = '8VRn991DZyPp7RjFgRuhaNKM3ty02sWnEBSxYVBUFJwZl'
CONSUMER_KEY = 'sdT0eSA6CwgwBcbVn5zE0W7HZ'
CONSUMER_SECRET = 'gYb5HJ6Xbly0Zf4nFkQSIm3mfjXtREDfKUpb3HGIDDI5GEcqUX'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(CONSUMER_KEY,TOKEN_SECRET)

api = tweepy.API(auth)

for tweet in api.search(q="basketball", lang="en", rpp=10):
    print(f"{tweet.user.name}: {tweet.text}")
>>>>>>> 6b515606686c1dedd34a52a50d758066a511ddb9
