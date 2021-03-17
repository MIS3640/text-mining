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

def only_letters(word):
    """returns True only if string is only made out of letters or spaces. 
    Will use this to clean Reddit text before creating a histogram"""
    abecedary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
    for letter in word:
        if letter not in abecedary:
            return False
    return True

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

def order_scary_words_by_frequency(d):
    """Creates a list of the unique scary words in the Reddit posts ordered in descending order by frequency"""
    word_freq_list = []
    for word, freq in d.items():
        t = (freq, word)
        word_freq_list.append(t)
    sorted_list = sorted(word_freq_list,reverse=True)
    return sorted_list

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

def filler_words():
    """turn file of filler words into list of words"""
    f = open('folder_1/filler.txt')
    filler_words_list = []
    for line in f:
        word = line.strip()
        filler_words_list.append(word)
    return filler_words_list

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

def count_total_words():
    """returns total number of words in the Reddit posts"""
    sum = 0
    hist = create_histogram('folder_1/post_text.txt')
    for k in hist:
        sum += hist[k]
    return sum

def count_scary_words():
    """returns total number of scary words in the Reddit posts"""
    sum = 0
    hist = scary_histogram('folder_1/post_text.txt')
    for k in hist:
        sum += hist[k]
    return sum

def percentage_scary_words():
    """returns the percentage of total words in the Reddit posts that are scary"""
    number_scary_words = count_scary_words()
    number_total_words = count_total_words()
    percentage = (number_scary_words/number_total_words)*100
    print(number_scary_words)
    print(number_total_words)
    print(f'The percentage of words in the Reddit channel that are scary is {round(percentage,2)}%')

def main():
    reddit_file = 'folder_1/post_text.txt'
    #pprint.pprint(scary_histogram(reddit_file)) #uncomment to print full histogram
    d = scary_histogram(reddit_file)
    #pprint.pprint(invert_scary_dictionary(d)) #uncomment to print full inverted histogram
    #pprint.pprint(order_scary_words_by_frequency(d)) #uncomment to print full list of letters with their frequency
    top_words = 20
    pprint.pprint(most_frequent_words(top_words))
    #print(count_total_words()) #uncomment to print total number of words in posts
    #print(count_scary_words()) #uncomment to print total number of scary words in posts
    percentage_scary_words() #prints % of words that are scary


if __name__ == "__main__":
    main()