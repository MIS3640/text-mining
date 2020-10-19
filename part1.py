from twython import Twython
from config import TOKEN_SECRET_HIDDEN
from config import CONSUMER_SECRET_HIDDEN
import string
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
data = t.search(q="trump", lang = "en", result_type="recent", count = 2) 
strippables = string.punctuation + string.punctuation
for status in data['statuses']:
   tweet = status['text'].strip(strippables).replace('\n','')
   tweet = tweet.lower()
   tlist.append(tweet)
print(tlist)


# for status in data['statuses']:
#    tlist.append(status['text'])

# strippables = string.punctuation + string.whitespace

# for tweet in tlist:
#    clean = tweet['text'].strip(strippables)
#    tweet.lower()
#    print([clean])

# tlist = []
# strippables = string.whitespace + string.punctuation
# for status in tdict['statuses']:
#    tlist.append(status['text'].strip(strippables).lower())
# print(tlist)

# for tweet in tlist:
#    " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

# def process_tweets(filename):
#    hist = {}
#    fp = open(filename, encoding='UTF8')
#    for line in fp:
#       for word in line.split():
#          hist[word] = hist.get(word,0) + 1
#    return hist

# print(process_tweets('output.txt'))

# def main():
#    hist = process_tweets(tdict)


# if __name__ == '__main__':
#    main()

