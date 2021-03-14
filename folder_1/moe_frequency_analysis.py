import os
import string

def text_analyze(filename):
    stop_words = open('folder_1/filler.txt')
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