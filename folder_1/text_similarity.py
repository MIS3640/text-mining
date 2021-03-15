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
    with open('folder_1/textsimilarity.txt','w') as fout:
        for submission in subreddit_.hot(limit = limit_num):
            fout.write(submission.selftext)
    return 'folder_1/textsimilarity.txt'

def create_histogram(filename):
    """Creates a dictionary with the keys being every unique word in the Reddit posts and the values being their frequency"""
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

def hist_prom(hist):
    prom_hist = {}
    for keys in hist:
        if int(hist.get(keys)) > 5:
            prom_hist[keys] = hist.get(keys)
    return prom_hist


def analysis(limit_num, compared_to):
    filler_words_list = filler_words()
    with open('folder_1/single_post_text.txt', 'w') as fout:
        for post in subreddit_.top(limit=limit_num):
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
                    final_hist_result[words] = 1
                    count += 1
            print(f'The final number of similar words in this post is {count}')




def main():
    harvest_time = text_similarity_baseline(10)
    hist_harvest = create_histogram(harvest_time)
    prom_hist_hot_5 = hist_prom(hist_harvest)
    analysis(5, prom_hist_hot_5)
    

if __name__ == '__main__':
    main()



