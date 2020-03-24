import random
import string

#Data Cleaning
def process_file(filename, skip_header):
    """
    Makes a histogram that contains the words from a file.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """
    Reads from fp until it finds the line that ends the header.
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

#Characterizing by Word Frequencies
def most_common(hist, excluding_stopwords = False):
    """
    Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    t = [] 

    stopwords = process_file('Assignment 2/stopwords.txt', skip_header=False)

    stopwords = list(stopwords.keys()) 
    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        t.append((freq, word)) 
    t.sort(reverse=True)
    return t

#Computing Summary Statistics
#Top 10 words 
def print_most_common(hist, num=10, excluding_stopwords = False):
    """
    Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist,excluding_stopwords = True)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, freq, sep = '\t')



def main():
    hist = process_file('Assignment 2/Walden.txt', skip_header=True)
    print(hist)
    most_common(hist, excluding_stopwords = False)
    print_most_common(hist,10,excluding_stopwords = False)


if __name__ == '__main__':
    main()