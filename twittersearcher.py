# ----------------------------------------INSTRUCTIONS: ----------------------------------------
# 1. Install jsonpickle, Twython, nltk, and numpy using pip if you do not have them already
# 2. First, run this twitter_tweets.py to set the search query and the number of tweets to mine
# 3. Next, run tweets_sentiment_analysis.py to perform sentiment analysis on each tweet collected
# 4. Then finally, run sentiment_analysis_results.py to get the count of polarity (results)
# ----------------------------------------------------------------------------------------------

import jsonpickle
import twython
from twython import Twython


class TwitterSearcher:
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET):
        self._twython = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                TOKEN, TOKEN_SECRET)

    def twitterSearch(self, search_query, count):
        tweets = []
        tweets_per_qry = 100
        max_id = -1
        tweets_count = 0

        while tweets_count < count:
            try:
                if count - tweets_count < tweets_per_qry:
                    search_count = count - tweets_count
                else:
                    search_count = tweets_per_qry

                if max_id == -1:
                    new_tweets = self._twython.search(q=search_query, lang="en", count=search_count)
                else:
                    new_tweets = self._twython.search(q=search_query, lang="en", count=search_count, max_id=max_id)
                if not new_tweets:
                    break

                for tweet in new_tweets['statuses']:
                    tweets_count += 1
                    tweets.append(tweet)
                last_tweet = new_tweets['statuses'][-1]
                max_id = last_tweet['id'] - 1
                print("tweets count {0}".format(len(tweets)))
            except twython.TwythonError as e:
                print("some error : " + str(e))
                break
        return tweets
