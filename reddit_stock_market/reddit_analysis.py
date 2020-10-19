# Characterizing by Word Frequencies - number of times particular words appear in comments section/title/replies?

# Comparing stock market threads and overall economy threads and words used

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
subreddit = reddit.subreddit("stockmarket")
# submissions = reddit.subreddit(sub).top('day', limit=5)
# top5 = [(submission.title, submission.selftext) for submission in submissions]


def reddit_words():
    hot_python = subreddit.hot(limit=5)
    # .hot, .new, .controversial, .top, .gilded
    for submission in hot_python:
        print(submission.title)
        comments = submission.comments
        for comment in comments:
            print(30 * "-")
            print(comment.body)
            if len(comment.replies) > 0:
                for reply in comment.replies:
                    print("Reply:", reply.body)


print(reddit_words())


# def reddit_mining():
#     dic = {}

#     strippables = string.punctuation + string.whitespace
#     line = line.replace("-", " ")
#     for word in line.split():
#             # word could be 'Sussex.'
#             word = word.strip(strippables)
#             word = word.lower()

#             # update the dictionary
#             hist[word] = dic.get(word, 0) + 1

#     return dic
