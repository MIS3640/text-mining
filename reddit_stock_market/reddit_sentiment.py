from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


import praw


reddit = praw.Reddit(
    client_id="MtwTkf_DOPpB_A",
    client_secret="hW_ZKOsPCtr1t2gpy_REhSCG1cE",
    username="kluu2020",
    password="Malden123!",
    user_agent="Reddit Text Mining Version 1",
)


def submission_sentiment():
    """output the titles of reddit threads and performe sentiment analysis on them"""
    headlines = set()
    for submission in reddit.subreddit("stockmarket").new(limit=1000):
        headlines.add(submission.title)
        display.clear_output()
        # print(len(headlines))

    sia = SIA()
    results = []
    # sentiment analysis
    for line in headlines:
        score = sia.polarity_scores(line)
        score["headline"] = line
        results.append(score)

    pprint(results[:10], width=1000)
    df = pd.DataFrame.from_records(results)
    pos_neg(df)  # calling the function to pass in results of next function


def pos_neg(df):
    """Examine and compare positive and negative headlines within a specific topic"""

    # categorize pos and neg headlines
    df["label"] = 0 
    df.loc[df["compound"] > 0.1, "label"] = 1
    df.loc[df["compound"] < -0.1, "label"] = -1

    print(df.label.value_counts())

    # Prints examples of pos/neg headlines
    print("Positive headlines:\n")
    pprint(list(df[df["label"] == 1].headline)[:5], width=200)

    print("\nNegative headlines:\n")
    pprint(list(df[df["label"] == -1].headline)[:5], width=200)


print(submission_sentiment())
print(pos_neg())