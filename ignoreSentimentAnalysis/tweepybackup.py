# import tweepy as tw

# auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(TOKEN, TOKEN_SECRET)
# api = tw.API(auth)
# rawdata = tw.Cursor(
#     api.search, q="donald trump", lang="en", tweet_mode="extended"
# ).items(2)
# print(rawdata)