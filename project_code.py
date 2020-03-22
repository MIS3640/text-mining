import praw
import string
from collections import Counter
import matplotlib.pyplot as plt 

reddit = praw.Reddit(client_id='5Lw5ka108mAmzA',
                     client_secret='b2XDXrWhbazbjT7QdFgHm_NgiEk',
                     user_agent='problem solving project (by u/k0og13)',
                     username='k0og13',
                     password='Genkenrex1!')

print(reddit.read_only)

subreddit = reddit.subreddit('Coronavirus')
top_subreddit = subreddit.top(limit=300) #pulling the top 300 submissions from r/Coronavirus
top300_title = []
for submission in top_subreddit:
    top300_title.append(submission.title) #creating list of top 300 submission titles
# print(top300_title)


def del_punctuation(item):
    ''' 
        this function removes punctuation from a word
    '''
    punctuation = string.punctuation
    for c in item:
        if c in punctuation:
            item = item.replace(c, '')
    return item


def break_into_words():
    '''
        This function reads file, breaks it into 
        a list of used words in lower case.
    '''
    words_list = []
    for title in top300_title:
        for item in title.split():
            item = del_punctuation(item)
            item = item.lower()
            #print(item)
            words_list.append(item)
    return words_list
# print(break_into_words())

def create_dict():
    '''
        This function calculates words frequency and
        returns it as a dictionary.
    '''
    words_list = break_into_words()
    dictionary = {}
    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
       
    return dictionary

dictionary = create_dict()    

# maximum = max(dictionary, key=dictionary.get)
k = Counter(dictionary)

high = k.most_common(10) #takes top 10 most frequent words in the 300 titles and creates list stored in variable high
print('Words with 10 Highest Values:')
print('Keys: Values')
print('--------------')
for i in high: #prints out top 10 keys and values into list format. each word printed on separate line to create a table
    print(i[0],' :', i[1])
print('\n')
print('The total number of words is {}.'.format(len(break_into_words())))
print('The number of different words used in these posts is {}.'.format(len(dictionary)))

high = dict(high) #creating a dictionary of only the top 10 most frequent words
words = list(high.keys())
values = list(high.values())

x_pos = [i for i, _ in enumerate(words)]
plt.bar(x_pos, values, color='green') #creating the bar graph using dictionary keys (top 10 most frequent words) as x axis and dictionary values as y axis
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency in r/Coronavirus Submission Titles")
plt.xticks(x_pos, words)
# plt.show()

from textblob import TextBlob as tb 
submissions = list(reddit.subreddit('Coronavirus').hot(limit=10))
[str(s) for s in submissions]

# grab the first submission
submission = submissions[0]

# the actual text is in the body
# attribute of a Comment
def get_comments(submission, n=200):
    """
    Return a list of comments from a submission.
    
    n is the number of comments we want to limit
    """
    count = 0
    def pull_comments(iterable=submission.comments):
        """
        This generator pulls out comments.
        """
        nonlocal count
        for c in iterable:
            if hasattr(c, 'body') and count < n:
                count += 1
                yield c.body
            else:
                # c was a Comment and did not have a body
                continue
    return pull_comments()
                
comments = list(get_comments(submission)) #creating a list of all the pulled comments
list(comments)

comment_join = tb(''.join(comments)) #joining all the comments into one list

print(comment_join.sentiment)
