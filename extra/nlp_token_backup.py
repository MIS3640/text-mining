# from twython import Twython
# from config import TOKEN_SECRET_HIDDEN, CONSUMER_SECRET_HIDDEN
# import string, re, unicodedata
# import nltk from nltk.corpus import stopwords set(stopwords.words('english'))

# from nltk.corpus import twitter_samples
# positive = twitter_samples.strings('positive_tweets.json')
# negative = twitter_samples.strings('negative_tweets.json')
# text = twitter_samples.strings('tweets.20150430-223406.json')
# tweet_tokens = twitter_samples.tokenized('positive_tweets.json')

# print(tweet_tokens)
# def fetch_tweets():
#     TOKEN = "1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH"
#     TOKEN_SECRET = TOKEN_SECRET_HIDDEN
#     CONSUMER_KEY = "AmSWYiODOWhTIWLo7R09nh3sJ"
#     CONSUMER_SECRET = CONSUMER_SECRET_HIDDEN

#     t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
#     # data - dict, data['statuses'] - list, status - dict, status['text'] - str
#     count = {}  # Acts as a counter for how many times a word appears 
#     data = t.search(
#         q="trump",
#         lang="en",
#         result_type="recent",
#         count= 3,
#         tweet_mode="extended",
#         truncated=False,
#     )
#     for status in data["statuses"]:
#         tweet = status["full_text"]
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
#         tweet = list(tweet.split(" "))    # make each tweet a list of words
#         for word in tweet:
#             count[word] = count.get(word,0) + 1 # word frequency count
#     return count

# def tokenize_count(count): 

# def main():
#     print(fetch_tweets())

# if __name__ == "__main__":
#     main()
