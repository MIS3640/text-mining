# from nltk.corpus import brown
# print(brown.words())

from twython import Twython
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
darth = SentimentIntensityAnalyzer()

from config import TOKEN_SECRET_HIDDEN, CONSUMER_SECRET_HIDDEN
import re, unicodedata

""" 
Resources:
Twitter Search - https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
Twitter Standard Operators - https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/standard-operators
Twython Search - https://twython.readthedocs.io/en/latest/usage/starting_out.html#dynamicfunctionarguments
 """
# TODO:
# 1. Figure out how to hide the config.py (Unless if he needs it to run the code)
# 2. Is this actually doing anything? "Truncated = False"
# 3. Figure out if need to tokenize the tweets
# 4. Docstrings
# 5. What to improve in the code? - check instructions to ensure all points have been covered
# 6. Maybe make the "tweet = ..." edits more efficient
# 7. Potentially have words analysis
# 8. Print the original tweet vs cleaned tweet for tweets_nlp?
# 9. Test how accurate the analyzer is - use known sentences and known scores to see if implementation is correct

TOKEN = "1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH"
TOKEN_SECRET = TOKEN_SECRET_HIDDEN
CONSUMER_KEY = "AmSWYiODOWhTIWLo7R09nh3sJ"
CONSUMER_SECRET = CONSUMER_SECRET_HIDDEN

t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
# data - dict, data['statuses'] - list, status - dict, status['text'] - str
tlist = list()
data = t.search(
    q="trump",
    lang="en",
    result_type="recent",
    count=2,
    tweet_mode="extended",
    truncated=False,
)
print(data["statuses"])
for status in data["statuses"]:
    tweet = (
        status["full_text"].lower().replace("\n", "")
    )  # remove whitespace and make it lowercase
    tweet = "".join(re.sub(r"http\S+", "", tweet))  # remove URL
    tweet = re.sub(r"[^\w\s]", "", tweet)  # remove punctuation
    tweet = (
        unicodedata.normalize("NFKD", tweet)
        .encode("ascii", "ignore")
        .decode("utf-8", "ignore")
    )  # remove emojis
    tlist.append(tweet)


def tweets_nlp(tweets):
    """
    
    """
    for tweet in tweets:
        # sentence = word_tokenize(tweet)
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        print(f"Tweet: {tweet}")
        print(f"Score: {score}")
        print()


def main():
    tweets = tlist
    print(tweets_nlp(tweets))


if __name__ == "__main__":
    main()
