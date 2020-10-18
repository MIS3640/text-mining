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
# .hot, .new, .controversial, .top, .gilded
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

    # comments = submission.comments
    # for comment in comments:
    #     print(30 * "-")
    #     print(comment.body)
    #     if len(comment.replies) > 0:
    #         for reply in comment.replies:
    #             print("Reply:", reply.body)

    # submission.comments.replace_more(limit=0)
    comments = submission.comments.list()
    for comment in comments:
        print(30 * "-")
        print("Parent ID:", comment.parent())
        print("Comment ID", comment.id)  # attribute
        print(comment.body)


# Streaming from Reddit

subreddit = reddit.subreddit("stockmarket")

for comment in subreddit.stream.comment():  # for submission
    try:
        # parent_id = str(comment.parent())

        # original = reddit.comment(parent_id)
        # print("Parent:")
        # print(original.body)
        # print("Reply:")
        print(comment.body)  # just streaming comments
        # print submission.title
    except praw.exceptions.PRAWException as e:  # can use just Exception if not working to stream
        # print(str(e)) # This is for submissions
        pass
