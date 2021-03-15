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











# # from nltk.sentiment.vader import SentimentIntensityAnalyzer

# def polarity_scores():
#     """generates polarity scores for each story in the reddit thread, using the isolate_post() function to run through each post (50 posts total)"""
#     # while loop to redo the analysis for each story
    
#         isolate_post()
#     # do sentiment analysis 

# # sentence = 'Software Design is my favorite class because learning Python is so cool!'
# # score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# # print(score)