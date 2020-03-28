# ----------------------------------------INSTRUCTIONS: ----------------------------------------
# 1. Install jsonpickle, Twython, nltk, and numpy using pip if you do not have them already
# 2. First, run this twitter_tweets.py to set the search query and the number of tweets to mine
# 3. Next, run tweets_sentiment_analysis.py to perform sentiment analysis on each tweet collected
# 4. Then finally, run sentiment_analysis_results.py to get the count of polarity (results)
# ----------------------------------------------------------------------------------------------

import jsonpickle
from twittersearcher import TwitterSearcher

def main():
    search_query = "#coronavirus" # Enter a search term you wish to search for
    count = 15000 # Enter how many search results you wish to mine
    filename = "tweets.txt"

    TOKEN = '980837803-ThcIIggIdTaXGfBoin6zIIEoRINUIEG3B87uXN7u'
    TOKEN_SECRET = '6M1qRwFUNSwx7xi34ddE4Mp5IK0huYtLQFGn7Thov025R'
    CONSUMER_KEY = 'FKbm2hZCv7orhm48w4s4J3HUo'
    CONSUMER_SECRET = 'RWUOtZIRGihJHe0rIFGo8uRUFxbwKRP1Vfj3se56INQDsaHSMm'
    t = TwitterSearcher(CONSUMER_KEY, CONSUMER_SECRET,
                TOKEN, TOKEN_SECRET)

    tweets = t.twitterSearch(search_query, count)

    f = open(filename, "w")
    f.write(jsonpickle.encode(tweets, unpicklable=False))
    f.close()
    print("Downloaded {0} tweets about {1} and saved to {2}.".format(len(tweets), search_query, filename))

if __name__ == '__main__':
    main()