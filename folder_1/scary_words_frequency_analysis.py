import os
import string
import pprint

def scary_words():
    """turn file of scary words into list of scary words"""
    f = open('folder_1/scary_words.txt')
    scary_words_list = []
    for line in f:
        word = line.strip()
        scary_words_list.append(word)
    return scary_words_list

#print(scary_words())

def only_letters(word):
    """returns True only if string is only made out of letters or spaces. 
    Will use this to clean Reddit text before creating a histogram"""
    abecedary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
    for letter in word:
        if letter not in abecedary:
            return False
    return True

#print(only_letters('Moise'))
#print(only_letters('Babson is cool'))
#print(only_letters('m4h5ise'))
#print(only_letters('m/h\ise'))

def scary_histogram(filename):
    """Creates a dictionary with the keys being scary words in the Reddit posts and the values being their frequency"""
    scary_words_list =scary_words()
    hist = {}
    fp = open(filename, encoding='latin-1')
    strippables = string.punctuation + string.whitespace
    for line in fp:
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            if word in scary_words_list and only_letters(word):
                hist[word] = hist.get(word, 0) + 1
    return hist

#print(scary_histogram('folder_1/post_text.txt'))

def invert_scary_dictionary(d):
    """Creates a dictionary with key value being the number of times a scary word appears in the Reddit posts and the value being a list of scary words
    that appear in the Reddit post with that frequency"""
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

d = scary_histogram('folder_1/post_text.txt')
#pprint.pprint(invert_scary_dictionary(d))

def order_scary_words_by_frequency(d):
    """Creates a list of the unique scary words in the Reddit posts ordered in descending order by frequency"""
    word_freq_list = []
    for word, freq in d.items():
        t = (freq, word)
        word_freq_list.append(t)
    sorted_list = sorted(word_freq_list,reverse=True)
    return sorted_list

#print(order_scary_words_by_frequency(d))

def most_frequent_words(limit):
    """prints the most frequent scary words in the Reddit posts. The 'limit' parameter stands for how many 
    scary words will be printed. If limit = 10, then will print top 10 scary words"""
    word_freq_list = order_scary_words_by_frequency(d)
    count = 0
    for pair in word_freq_list:
        print(pair)
        count += 1
        if count == limit:
            break

print(most_frequent_words(10))