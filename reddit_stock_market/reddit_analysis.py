# Characterizing by Word Frequencies - number of times particular words appear in comments section/title/replies?
# bull/bear/specific stocks
# Comparing stock market threads and overall economy threads and words used (connotation)

# Sentiment Analysis

# Analysis on authors and habbits


import praw
import string

# import config
reddit = praw.Reddit(
    client_id="MtwTkf_DOPpB_A",
    client_secret="hW_ZKOsPCtr1t2gpy_REhSCG1cE",
    username="kluu2020",
    password="Malden123!",
    user_agent="Reddit Text Mining Version 1",
)
subreddit = reddit.subreddit("economy")
# submissions = reddit.subreddit(sub).top('day', limit=5)
# top5 = [(submission.title, submission.selftext) for submission in submissions]


def reddit_sub_word_freq():
    word_freq = {}

    hot_python = subreddit.hot(limit=5)
    # .hot, .new, .controversial, .top, .gilded
    for submission in hot_python:
        # print(submission.title)
        count_word_submission(word_freq, submission)

    return word_freq


def count_word_submission(word_freq, submission):
    comments = submission.comments
    for comment in comments:
        count_word_comment(word_freq, comment)
    
   


def count_word_comment(word_freq, comment):
    strippables = string.punctuation + string.whitespace

    
    for word in comment.body.split():
        word = word.replace("-", " ")
        word = word.strip(strippables)
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1
        
    replies = comment.replies.list()

    for reply in replies:
        if isinstance(reply, praw.models.Comment):
            count_word_comment(word_freq, reply)
        elif isinstance(reply, praw.models.MoreComments):
            for more_reply in reply.comments():
                count_word_comment(word_freq, more_reply)
        else:
            print('Something went wrong.')


print(reddit_sub_word_freq())

# Need to sort words from greatest to least