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
    filename = f"story{count}.txt"
    while count < 11: 
        for submission in subreddit.hot(limit=10):
            new_story = open(f'folder_1/{filename}', 'w') 
            new_story.write(submission.selftext)
            new_story.close()
            count += 1
   
subreddit_isolate()

import nltk 

def sentiment_analysis(file):
    with open(file) as story:
        score = nltk.SentimentIntensityAnalyzer().polarity_scores(story)
    return score 

print(sentiment_analysis('folder_1/story1.txt'))

# print for other 9 stories as well
