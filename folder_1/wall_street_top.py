import praw
import string
import os


def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THE PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist



reddit = praw.Reddit(
    client_id="tQrzWPu2ZLugIg",
    client_secret="gxNvyLA3H-MYqk8IIZCxraStrXdbYQ",
    user_agent="windows:pyth0n3xp3rts:v0.1 (by u/python_group_v_2)",
    
)
# assume you have a reddit instance bound to variable `reddit`
subreddit = reddit.subreddit("nosleep")
print(subreddit.display_name)  # output: redditdev
print(subreddit.title)         # output: reddit development
print(subreddit.description)   # output: a subreddit for discussion of ...
# assume you have a Subreddit instance bound to variable `subreddit`
def subreddit_trawl():
    with open('folder_1/post_text.txt','w') as fout:
        d = {}
        for submission in subreddit.hot(limit=50):
            # print(f'{submission.title},   {submission.score} ')
            # print(f'{submission.selftext} \n \n \n')
            fout.write(submission.selftext)
            # for word in submission.selftext
def text_analyze(filename):
    stop_words = process_file('folder_1/filler.txt')
    hist = {}
    fp = open(filename, encoding='latin-1')
    strippables = string.punctuation + string.whitespace
    for line in fp:
        line = line.replace('-', ' ')
        for word in line.split():
            if word not in stop_words:
                word = word.strip(strippables)
                word = word.lower()
                hist[word] = hist.get(word, 0) + 1
    return hist
# subreddit_trawl()
print(text_analyze('folder_1/post_text.txt'))