

import praw

reddit = praw.Reddit(
    client_id="MtwTkf_DOPpB_A",
    client_secret="hW_ZKOsPCtr1t2gpy_REhSCG1cE",
    username="kluu2020",
    password="Malden123!",
    user_agent="Reddit Text Mining Version 1",
)

econ = reddit.subreddit('economy')

def find_moderators():
    """Finding top moderators that contribute to a specific topic and build a community"""
    mod_list = []
    for mod in econ.moderator():
        mod_list.append(mod.name)

    return mod_list

print(find_moderators())


# This function is used to compare the different categories of submissions and see similarities and differences

def top_new_contro_econ():
    """search posts in 3 different categories"""
    print('These are the top submissions!')
    for submission in econ.top(limit=1):
        print(f'Title of the submission:{submission.title}, User name: {submission.name}, Upvotes: {submission.ups}, Down votes it has:{submission.downs}, Overall score: {submission.score}, Number of comments: {submission.num_comments}.')

    print('-'*50)
    print('These are the new submissions!')
    for submission in econ.new(limit=1):
        print(f'Title of the submission:{submission.title}, User name: {submission.name}, Upvotes: {submission.ups}, Down votes it has:{submission.downs}, Overall score: {submission.score}, Number of comments: {submission.num_comments}.')

    print('-'*50)
    print('These are the controversial submissions!')
    for submission in econ.controversial(limit=1):
        print(f'Title of the submission:{submission.title}, User name: {submission.name}, Upvotes: {submission.ups}, Down votes it has:{submission.downs}, Overall score: {submission.score}, Number of comments: {submission.num_comments}.')


print(top_new_contro_econ())