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
    """creates the dictionary of words for a specific category for where the words will be stored and returns frequency"""
    word_freq = {}

    hot_top = subreddit.hot(limit=5)
    # .hot, .new, .controversial, .top, .gilded
    for submission in hot_top:
        # print(submission.title)
        count_word_submission(word_freq, submission)

    return word_freq


def count_word_submission(word_freq, submission):
    """takes and counts the words in the thread titles and updates dictionary"""
    comments = submission.comments
    for comment in comments:
        count_word_comment(word_freq, comment)


def count_word_comment(word_freq, comment):
    """takes and counts works in the comments and replies to the comments and updates dictionary"""
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
            print("Something went wrong.")


# reddit_dict = reddit_sub_word_freq()


# def most_common(word_freq, excluding_stopwords=False):
#     """Makes a list of word-freq pairs in descending order of frequency.

#     returns: list of (frequency, word) pairs
#     """
#     # create a list (tuple)
#     common_words = []

#     for word, freq in word_freq.items():
#         t = (freq, word)
#         common_words.append(t)

#     common_words.sort(reverse=True)

#     return common_words


# def print_most_common(word_freq, num=20):
#     """Prints the most commons words in a histgram and their frequencies.
#     num: number of words to print
#     """
#     top_words = most_common(word_freq)
#     for freq, word in top_words[:num]:
#         print(word, freq)


# t = most_common(reddit_dict, excluding_stopwords=True)
# print("The most common words are:")
# for freq, word in t[0:20]:
#     print(word, "\t", freq)


print(reddit_sub_word_freq())