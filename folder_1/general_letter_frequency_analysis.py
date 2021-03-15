import os
import string
import pprint

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

def create_letter_histogram(filename):
    """Creates a dictionary with the keys being every unique letter in the Reddit posts and the values being their frequency"""
    hist = {}
    fp = open(filename, encoding='latin-1')
    strippables = string.punctuation + string.whitespace
    for line in fp:
        line = line.replace('-', ' ')
        line = line.split()
        for word in line:
            word = word.strip(strippables)
            word = word.lower()
            if only_letters(word):
                for letter in word:
                    if letter not in hist:
                        hist[letter] = 1
                    else:
                        hist[letter] += 1
    return hist

#print(create_letter_histogram('folder_1/post_text.txt'))

def invert_letter_dictionary(d):
    """Creates a dictionary with key value being the number of times a letter appears in the Reddit posts and the value being a list of letters
    that appear in the Reddit post with that frequency"""
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

d = create_letter_histogram('folder_1/post_text.txt')
#pprint.pprint(invert_letter_dictionary(d))

def order_letters_by_frequency(d):
    """Creates a list of the unique letters in the Reddit posts ordered in descending order by frequency"""
    letter_freq_list = []
    for letter, freq in d.items():
        t = (freq, letter)
        letter_freq_list.append(t)
    sorted_list = sorted(letter_freq_list,reverse=True)
    return sorted_list

#print(order_letters_by_frequency(d))

def most_frequent_letters(limit):
    """prints the most frequent letters in the Reddit posts. The 'limit' parameter stands for how many 
    letters will be printed. If limit = 10, then will print top 10 letters"""
    letter_freq_list = order_letters_by_frequency(d)
    count = 0
    for pair in letter_freq_list:
        print(pair)
        count += 1
        if count == limit:
            break

print(most_frequent_letters(20))