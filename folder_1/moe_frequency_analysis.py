import os
import string
import pprint

def filler_words():
    """turn file of filler words into list of words"""
    f = open('folder_1/filler.txt')
    filler_words_list = []
    for line in f:
        word = line.strip()
        filler_words_list.append(word)
    return filler_words_list

#print(filler_words())

def only_letters(word):
    abecedary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
    for letter in word:
        if letter not in abecedary:
            return False
    return True

#print(only_letters('Moise'))
#print(only_letters('Babson is cool'))
#print(only_letters('m4h5ise'))
#print(only_letters('m/h\ise'))

def create_histogram(filename):
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

#print(create_histogram('folder_1/post_text.txt'))

def invert_dictionary(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

d = create_histogram('folder_1/post_text.txt')
pprint.pprint(invert_dictionary(d))