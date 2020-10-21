from twython import Twython
from config import TOKEN_SECRET_HIDDEN, CONSUMER_SECRET_HIDDEN
import re, unicodedata, string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# word cloud
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image as im
# %matplotlib inline

def fetch_tweets():
    TOKEN = "1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH"
    TOKEN_SECRET = TOKEN_SECRET_HIDDEN
    CONSUMER_KEY = "AmSWYiODOWhTIWLo7R09nh3sJ"
    CONSUMER_SECRET = CONSUMER_SECRET_HIDDEN

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET) 
    count = {}
    cloudlist = []
    rawdata = t.search(
        q="hello",
        lang="en",
        result_type="recent",
        count= 3,
        tweet_mode="extended",
        truncated=False,
    )
    for status in rawdata["statuses"]:
        tweet = status["full_text"]
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
        tweet = list(tweet.split(" "))    # make each tweet a list of words
        for word in tweet:
            count[word] = count.get(word,0) + 1 # word frequency count
            cloudlist.append(word)
    return count

# def cloud():


def top_words(count, num):
    top = []
    for word, freq in count[].items():
        t = (freq, word)
        top.append(t)
    top.sort(reverse = True)
    return top

def print_top_words(count, num):
    t = top_words(count)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)
    

def main():
    count = fetch_tweets()
    t = top_words(count)
    print('The most common words are:')
    for freq, word in t[0:10]:
        print(word, '\t', freq)

    # t = most_common(hist, excluding_stopwords=False)
    # print('The most common words are:')
    # for freq, word in t[0:20]:
    #     print(word, '\t', freq)


if __name__ == '__main__':
    main()
