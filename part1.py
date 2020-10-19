from twython import Twython
from config import TOKEN_SECRET_HIDDEN, CONSUMER_SECRET_HIDDEN
import re, unicodedata
""" 
Resources:
Twitter Search - https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
Twitter Standard Operators - https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/standard-operators
Twython Search - https://twython.readthedocs.io/en/latest/usage/starting_out.html#dynamicfunctionarguments
 """

TOKEN = "1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH"
TOKEN_SECRET = TOKEN_SECRET_HIDDEN
CONSUMER_KEY = "AmSWYiODOWhTIWLo7R09nh3sJ"
CONSUMER_SECRET = CONSUMER_SECRET_HIDDEN

t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
# data - dict, data['statuses'] - list, status - dict, status['text'] - str
tlist = list()
data = t.search(q="hello", lang = "en", result_type="recent", count = 2) 
for status in data['statuses']:
   tweet = status['text'].lower().replace('\n','')  # remove whitespace and make it lowercase
   tweet = ''.join(re.sub(r'http\S+', '', tweet))  # remove URL
   tweet = re.sub(r'[^\w\s]', '', tweet)   # remove punctuation
   tweet = unicodedata.normalize('NFKD', tweet).encode('ascii', 'ignore').decode('utf-8', 'ignore')  # remove emojis
   tlist.append(tweet)
print(tlist)

