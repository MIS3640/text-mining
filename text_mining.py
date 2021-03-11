import praw
import pickle

def import_subreddit():
    '''imports the top 100 posts under wallstreetbets subreddit'''
    reddit = praw.Reddit(client_id = 'UV_0pi49dIB77w', client_secret = 'xrAIGSNfOco13rjEJii23FB7EDPJBQ', username = 'verkxies1', password = 'problemsolvingandsoftwaredesign', user_agent = 'verkxies1')
    sub = 'wallstreetbets'
    submissions = reddit.subreddit(sub).top('day', limit = 100)
    top100 = [(submission.title, submission.selftext) for submission in submissions]
    return top100

def main():
    data = import_subreddit()

if __name__ == "__main__":
    main()

