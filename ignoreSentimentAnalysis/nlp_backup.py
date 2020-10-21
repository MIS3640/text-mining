# # from nltk.corpus import brown
# # print(brown.words())

# from twython import Twython
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# print(stopwords.words("english"))

# darth = SentimentIntensityAnalyzer()

# from config import TOKEN_SECRET_HIDDEN, CONSUMER_SECRET_HIDDEN
# import re, unicodedata

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# """
# Resources:
# Twitter Search - https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
# Twitter Standard Operators - https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/standard-operators
# Twython Search - https://twython.readthedocs.io/en/latest/usage/starting_out.html#dynamicfunctionarguments
#  """


# def fetch_tweets():
#     TOKEN = "1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH"
#     TOKEN_SECRET = TOKEN_SECRET_HIDDEN
#     CONSUMER_KEY = "AmSWYiODOWhTIWLo7R09nh3sJ"
#     CONSUMER_SECRET = CONSUMER_SECRET_HIDDEN

#     t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
#     # data - dict, data['statuses'] - list, status - dict, status['text'] - str
#     tlist = list()
#     data = t.search(
#         q="trump",
#         lang="en",
#         result_type="recent",
#         count=2,
#         tweet_mode="extended",
#         truncated=False,
#     )
#     for status in data["statuses"]:
#         tweet = (
#             status["full_text"].lower().replace("\n", "")
#         )  # remove whitespace and make it lowercase
#         tweet = "".join(re.sub(r"http\S+", "", tweet))  # remove URL
#         tweet = re.sub(r"[^\w\s]", "", tweet)  # remove punctuation
#         tweet = (
#             unicodedata.normalize("NFKD", tweet)
#             .encode("ascii", "ignore")
#             .decode("utf-8", "ignore")
#         )  # remove emojis
#         tlist.append(tweet)
#     return tlist


# def tweets_nlp(tweets):
#     """"""
#     scoredict = dict()
#     for tweet in tweets:
#         score = SentimentIntensityAnalyzer().polarity_scores(tweet)
#         print(score)
#         scoredict[tweet] = score
#         sentence = word_tokenize(tweet)
#         print(f"Tweet: {tweet}")
#         print(f"Score: {score}")
#         print()
#     return df
#     return scoredict


# def pandascore(scores):
#     df = pd.DataFrame(list(scores.items()), columns=["Neg", "Neu", "Pos", "Compound"])
#     df = pd.DataFrame.from_dict(scores, orient="index")
#     df = pd.DataFrame.from_dict(scores)
#     df["label"].value_counts()
#     HISTOGRAM
#     fig, ax = plt.subplots(figsize=(8, 6))
#     df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1], ax=ax, color="purple")
#     plt.title("Sentiments from Tweets")
#     plt.show()

#     tweettext = scores.keys()
#     scoring = scores.values()
#     plt.bar(tweettext, scoring)

#     lists = sorted(scores.items())
#     x, y = zip(*lists)

#     plt.plot(x, y)
#     plt.show()

#     print(df)


# def main():
#     raw_tweets = fetch_tweets()
#     scores = scoredict
#     print(pandascore(tweets_nlp(tweets)))
#     returned_scoredict = tweets_nlp(raw_tweets)
#     print(tweets_nlp(raw_tweets))
#     print(pandascore(returned_scoredict))


# if __name__ == "__main__":
#     main()