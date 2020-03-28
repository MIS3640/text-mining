# ----------------------------------------INSTRUCTIONS: ----------------------------------------
# 1. Install jsonpickle, Twython, nltk, and numpy using pip if you do not have them already
# 2. First, run this twitter_tweets.py to set the search query and the number of tweets to mine
# 3. Next, run tweets_sentiment_analysis.py to perform sentiment analysis on each tweet collected
# 4. Then finally, run sentiment_analysis_results.py to get the count of polarity (results)
# ----------------------------------------------------------------------------------------------

import jsonpickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import numpy

def main():
    filename = "tweets.txt"
    output_filename = "sentiment_analysis.txt"
    f = open(filename, "r")
    content = f.read()
    tweets = jsonpickle.decode(content)
    f.close()
    print("Loaded {0} tweets.".format(len(tweets)))

    analyzer = SentimentIntensityAnalyzer()
    scores = []
    for tweet in tweets:
        score = dict()
        score["text"] = tweet["text"]
        score["score"] = analyzer.polarity_scores(tweet["text"])
        scores.append(score)

    output_file = open(output_filename, "w")
    output_file.write(jsonpickle.encode(scores, unpicklable=False))
    output_file.close()

    print("Sentiment analysis for {0} tweets was saved to {1}".format(len(scores), output_filename))

if __name__ == '__main__':
    main()