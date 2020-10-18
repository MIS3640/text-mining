import praw

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

hot_python = subreddit.hot(limit=5)

for submission in hot_python:
    # print(submission) # submission thread ids
    # print(dir(submission))
    if not submission.stickied:
        # print(submission.title)
        print(
            "Title: {}, ups: {}, downs: {}, Have we visited: {}".format(
                submission.title, submission.ups, submission.downs, submission.visited
            )
        )
