import string
import os
import praw


reddit = praw.Reddit(
    client_id="tQrzWPu2ZLugIg",
    client_secret="gxNvyLA3H-MYqk8IIZCxraStrXdbYQ",
    user_agent="windows:pyth0n3xp3rts:v0.1 (by u/python_group_v_2)",   
)

subreddit = reddit.subreddit("nosleep")

def subreddit_isolate():
    count = 1 
    for submission in subreddit.hot(limit=10):
        filename = f"story{count}.txt"
        new_story = open(f'folder_1/stories/{filename}', 'w') 
        new_story.write(submission.selftext)
        new_story.close()
        count += 1
   
subreddit_isolate()

import nltk

# nltk.download() #download packages first before using nltk

def sentiment_analysis(file):
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    sent = SentimentIntensityAnalyzer()
    with open(file) as story:
        score = sent.polarity_scores(story) 
    # score is a dictionary with negativity scores
    return score 

print(sentiment_analysis('folder_1/story1.txt'))

# print for other 9 stories as well
