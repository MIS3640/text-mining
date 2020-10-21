from twython import Twython
import re, unicodedata, string
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud


def fetch_tweets():
    """
    Obtains tweets using Twython. Transforms raw data into tweet text. Cleans the tweet text and removes stopwords. Returns a dictionary.
    """
    TOKEN = "1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH"
    TOKEN_SECRET = "8toSo9U9UBrzDBTIQHmtq0F4mbWdagCCMFKLUNvKBugp8"
    CONSUMER_KEY = "AmSWYiODOWhTIWLo7R09nh3sJ"
    CONSUMER_SECRET = "Fsrzx8Ir3LYioa0EdTCozhYyKfRAsjO4XqRM67OAbxOVzfNMHn"

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
    stop = stopwords.words("english")  
    stop.extend(
        (
            "rt",
            "donald",
            "trump",
            "trumps",
            "bidens",
            "biden",
            "republican",
            "republicans",
            "democrat",
            "democrats",
            "democratic",
            "president",
        )
    )
    count = {}
    rawdata = t.search(q="donald trump", lang="en", count=1000)
    for status in rawdata["statuses"]:
        tweet = status["text"]
        tweet = (
            status["text"].lower().replace("\n", "")
        )  # Remove whitespace and change to lowercase
        tweet = "".join(re.sub(r"http\S+", "", tweet))  # Remove URL
        tweet = re.sub(r"[^\w\s]", "", tweet)  # Remove punctuation
        tweet = re.sub(r"[0-9]", "", tweet)  # Remove numbers
        tweet = (
            unicodedata.normalize("NFKD", tweet)
            .encode("ascii", "ignore")
            .decode("utf-8", "ignore")
        )  # Remove all unknown symbols (emojis) and applies compatibility decomposition
        tweet = list(tweet.split())  
        for word in tweet:
            if len(word) < 2:  # Remove outlier letters from truncated tweets
                tweet.remove(word)
            if word not in stop:
                count[word] = count.get(word, 0) + 1  
    return count


def top_words(count):
    """Sorts key-value pairs in reverse. Returns a list of tuples.

    Keyword arguments:
    count -- Dictionary of word and word count pairs.
    """
    top = []
    for word, freq in count.items():
        t = (freq, word)
        top.append(t)
    top.sort(reverse=True)
    print(top)
    return top


def panda_top_words(top, num):
    """Creates a new list with a specified amount of the most frequent words for visualization purposes. Returns a list of tuples.

    Keyword arguments:
    top -- List of tuples containing words and frequencies.
    num -- Parameter that dictates the quantity of top words desired.
    """
    pandalist = []
    for freq, word in top[:num]:
        pandalist.append(tuple((word, freq)))
    return pandalist


def panda_bar_visualization(pandalist):
    """Plots the specified top words and frequencies in a bar chart.

    Keyword arguments:
    pandalist -- List of tuples containing words and frequencies.
    """
    df = pd.DataFrame(pandalist, columns=["word", "frequency"])
    ax = df.plot(kind="bar", x="word", title="Most Popular Words", legend=False)
    ax.set(xlabel="Word", ylabel="Frequency")
    plt.show()


def word_cloud_visualization(top):
    """Creates a word cloud with all the top words. Size is dictated by the word frequency.

    Keyword arguments:
    top -- List of tuples containg words and frequencies.
    """
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
    """Define keyword arguments. Runs visualization functions."""
    count = fetch_tweets()
    top = top_words(count)
    pandalist = panda_top_words(top, num=10)
    panda_bar_visualization(pandalist)
    word_cloud_visualization(top)


if __name__ == "__main__":
    main()
