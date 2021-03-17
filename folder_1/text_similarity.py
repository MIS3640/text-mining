import praw
import string
import os

reddit = praw.Reddit(
    client_id="tQrzWPu2ZLugIg",
    client_secret="gxNvyLA3H-MYqk8IIZCxraStrXdbYQ",
    user_agent="windows:pyth0n3xp3rts:v0.1 (by u/python_group_v_2)",
)
subreddit_ = reddit.subreddit("nosleep")

def filler_words():
    """turn file of filler words into list of words"""
    f = open('folder_1/filler.txt')
    filler_words_list = []
    for line in f:
        word = line.strip()
        filler_words_list.append(word)
    return filler_words_list

def only_letters(word):
    """returns True only if string is only made out of letters or spaces. 
    Will use this to clean Reddit text before creating a histogram"""
    abecedary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
    for letter in word:
        if letter not in abecedary:
            return False
    return True

def text_similarity_baseline(limit_num):
    """This writes the hot posts of 'nosleep' into a text document called textsimilarity.txt.
    It returns the text document after writing it.
    The argument limit_num defines how many posts should be written into the document."""
    with open('folder_1/textsimilarity.txt','w') as fout:
        for submission in subreddit_.hot(limit = limit_num):
            fout.write(submission.selftext)
    return 'folder_1/textsimilarity.txt'

def create_histogram(filename):
    """Returns a dictionary with the keys being every unique word in the Reddit posts and the values being their frequency.
    The histogram analyzes a file, the argument filename, which can be any text document, but in this case is a file 
    of text posts from 'nosleep'."""
    filler_words_list = filler_words()
    hist = {}
    fp = open(filename, encoding='latin-1')
    strippables = string.punctuation + string.whitespace
    for line in fp:
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            if word not in filler_words_list and only_letters(word):
                hist[word] = hist.get(word, 0) + 1
    return hist

def hist_prom(hist, number_appears):
    """This function creates a histogram of all the prominent words in a given histogram with prominence being determined by appearance rate
    In general the histogram this function is being performed on a histogram of all the words in the hot posts on "nosleep
    The argument hist is the histogram the analysis is being performed on while number_appears is the number of appearances required
    by a word to be considered prominent.
    The returned histogram has prominent words as keys and their prominence as values"""
    prom_hist = {}
    for keys in hist:
        if int(hist.get(keys)) > number_appears:
            prom_hist[keys] = hist.get(keys)
    return prom_hist


def analysis(limit_num, compared_to):
    """
    Analyzes the top posts of all time in no sleep compared to a large number of posts in the 'hot' section
    limit_num is the number of top posts the function will analyze.
    Compared to is an argument for a dictionary to compare them to (in this case prom_hist_hot_5). 
    This function has 5 new variables:
        post_num - shows which post_num out of the top 5 is being analyzed
        count - counts the number of similar prominent words between the hot and top posts
        single_post_hist - Is a dictionary that stores the words in a single post
        new_prom_hist - A dictionary that stores the most prominent words in a single post
        final_hist_results - A dictionary that stores the similar prominent words between the hot and top posts.
    At the end the function prints the words that the top 5 posts of all time have in common with the given histogram.
    This allows you to figure out which words in your given scary stories are in the top 5 posts also.
    """
    filler_words_list = filler_words()
    post_num = 0
    for post in subreddit_.top(limit=limit_num):
        with open('folder_1/single_post_text.txt', 'w') as fout:
            post_num += 1
            count = 0
            fout.write(post.selftext)
            fp = open('folder_1/single_post_text.txt', encoding='latin-1')
            strippables = string.punctuation + string.whitespace
            single_post_hist = {}
            for line in fp:
                line = line.replace('-', ' ')
                for word in line.split():
                    word = word.strip(strippables)
                    word = word.lower()
                    if word not in filler_words_list and only_letters(word):
                        single_post_hist[word] = single_post_hist.get(word, 0) + 1
            new_prom_hist = {} 
            for keys in single_post_hist:   
                if int(single_post_hist.get(keys)) > 5:
                    new_prom_hist[keys] = single_post_hist.get(keys)
            final_hist_result = {}
            for words in new_prom_hist:
                if words in compared_to:
                    final_hist_result[words] = single_post_hist.get(words)
                    count += 1
            print(f'{final_hist_result}')
            print(f'The final number of similar words in post {post_num} is {count} \n')




def main():
    harvest_time = text_similarity_baseline(10)
    hist_harvest = create_histogram(harvest_time)
    prom_hist_hot_5 = hist_prom(hist_harvest, 10)
    analysis(5, prom_hist_hot_5)
    

if __name__ == '__main__':
    main()



