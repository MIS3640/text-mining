import praw

reddit = praw.Reddit(
    client_id="tQrzWPu2ZLugIg",
    client_secret="gxNvyLA3H-MYqk8IIZCxraStrXdbYQ",
    user_agent="windows:pyth0n3xp3rts:v0.1 (by u/python_group_v_2)",
    
)
# assume you have a reddit instance bound to variable `reddit`
subreddit = reddit.subreddit("wallstreetbets")
print(subreddit.display_name)  # output: redditdev
print(subreddit.title)         # output: reddit development
print(subreddit.description)   # output: a subreddit for discussion of ...
# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.hot(limit=2):
#     print(submission.title)
#     # Output: the submission's title
#     print(submission.score)
#     # Output: the submission's score
    # print(submission.id)
    top_level_comments = list(submission.comments)
    all_comments = submission.comments.list()
    new_id = submission.id
    top_level_comments = list(submission.comments)
    all_comments = submission.comments.list()
    print(all_comments)
    # assume you have a Reddit instance bound to variable `reddit`
    submission = reddit.submission(id=new_id)
    submission.comment_sort = "new"
    top_level_comments = list(submission.comments)
    # print(top_level_comments)
    # for id_ in top_level_comments:
    #     print(id_)
    #     comment_id = id_
    #     reddit.comment(id=str(comment_id))




# # print(reddit.read_only)
# # #change the subreddit for info
# # for submission in reddit.subreddit("wallstreetbets").hot(limit=10):
# #     print(submission.title)

# # assume you have a reddit instance bound to variable `reddit`
# subreddit = reddit.subreddit("wallstreetbets")

# print(subreddit.display_name)  # output: redditdev
# print(subreddit.title)         # output: reddit development
# print(subreddit.description)   # output: a subreddit for discussion of ...

# # assume you have a Subreddit instance bound to variable `subreddit`
# for submission in subreddit.hot(limit=10):
# #     print(submission.title)
# #     # Output: the submission's title
# #     print(submission.score)
# #     # Output: the submission's score
#     print(submission.id)
#     # Output: the submission's ID
# #     print(submission.url)
# #     # Output: the URL the submission points to or the submission's URL if it's a self post

