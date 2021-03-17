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

d = create_letter_histogram('folder_1/post_text.txt')

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

def order_letters_by_frequency(d):
    """Creates a list of the unique letters in the Reddit posts ordered in descending order by frequency"""
    letter_freq_list = []
    for letter, freq in d.items():
        t = (freq, letter)
        letter_freq_list.append(t)
    sorted_list = sorted(letter_freq_list,reverse=True)
    return sorted_list

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

def main():
    reddit_file = 'folder_1/post_text.txt'
    #pprint.pprint(create_letter_histogram(reddit_file)) #uncomment to print full histogram
    d = create_letter_histogram(reddit_file)
    #pprint.pprint(invert_letter_dictionary(d)) #uncomment to print full inverted histogram
    #pprint.pprint(order_letters_by_frequency(d)) #uncomment to print full list of letters with their frequency
    top_letters = 20
    pprint.pprint(most_frequent_letters(top_letters))

if __name__ == "__main__":
    main()