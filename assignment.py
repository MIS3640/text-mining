from twython import Twython
from config import TOKEN_SECRET_HIDDEN, CONSUMER_SECRET_HIDDEN
import re, unicodedata, string
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud


def fetch_tweets():
    TOKEN = "1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH"
    TOKEN_SECRET = TOKEN_SECRET_HIDDEN
    CONSUMER_KEY = "AmSWYiODOWhTIWLo7R09nh3sJ"
    CONSUMER_SECRET = CONSUMER_SECRET_HIDDEN

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
    # bad = set(stopwords.words('english') + list(string.punctuation) + list(string.digits))
    stop = stopwords.words('english')  # stop words 
    stop.extend(('rt','donald','trump','trumps','bidens','biden','republican','republicans','democrat','democrats','democratic'))
    count = {}
    rawdata = t.search(
        q="donald trump",
        lang="en",
        # result_type="recent",
        count=30
    )
    for status in rawdata["statuses"]:
        tweet = status["text"]
        tweet = (
            status["text"].lower().replace("\n", "")
        )  # remove whitespace and make it lowercase
        tweet = "".join(re.sub(r"http\S+", "", tweet))  # remove URL
        tweet = re.sub(r"[^\w\s]", "", tweet)  # remove punctuation
        tweet = re.sub(r"[0-9]", "", tweet)  # remove punctuation
        tweet = (
            unicodedata.normalize("NFKD", tweet)
            .encode("ascii", "ignore")
            .decode("utf-8", "ignore")
        )  # remove emojis
        tweet = list(tweet.split())  # make each tweet a list of words
        for word in tweet:
            if len(word) < 2:   # remove outlier words
                tweet.remove(word)
                # print(f"FUCKED UP WORDS {word}")                
            if word not in stop:
                count[word] = count.get(word, 0) + 1  # word frequency count
            # else:
            #     print(f"STOPPED WORDS {word}")
    return count
    

def top_words(count):
    top = []
    for word, freq in count.items():
        t = (freq, word)
        top.append(t)
    top.sort(reverse=True)
    return top


def panda_common_words(top, num):
    pandalist = []
    for freq, word in top[:num]:
        pandalist.append(tuple((word, freq)))
    return pandalist

def panda_bar_visualization(pandalist):
    df = pd.DataFrame(pandalist, columns=['word', 'frequency'])
    ax = df.plot(kind='bar', x='word', title = 'Most Popular Words', legend=False)
    ax.set(xlabel='Word', ylabel='Frequency')
    plt.show()

def word_cloud_visualization(top):
    reversetop = []
    for t in top:
        reversetop.append(t[::-1]) 
    wordcloud = WordCloud(
        max_font_size=50, max_words=1000, background_color="white"
    ).generate_from_frequencies(dict(reversetop))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def main():
    count = fetch_tweets()
    top = top_words(count)
    pandalist = panda_common_words(top, num = 10)
    panda_bar_visualization(pandalist)
    word_cloud_visualization(top)


if __name__ == "__main__":
    main()

#######################################################################
# Additional Ideas
#######################################################################
# CAN DO OUTLIER WORDS

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