import random
import string
import sys
import pickle
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

with open('saved_texts.pickle','rb') as input_file:
    The_Modest_Proposal = pickle.load(input_file)
    Time_Machine = pickle.load(input_file)


def process_file(text, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    if skip_header:
        skip_gutenberg_header(text)

    strippables = string.punctuation + string.whitespace

    for line in text.split('/n'):
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(text):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in text:
        if line.startswith('*** START OF THIS PROJECT'):
            break


# def total_words(hist):
#     """Returns the total of the frequencies in a histogram."""
#     return sum(hist.values())

# def different_words(hist):
#     """Returns the number of different words in a histogram."""
#     return len(hist)

# def most_common(hist, excluding_stopwords=False):
#     """Makes a list of word-freq pairs in descending order of frequency.
#     hist: map from word to frequency
#     returns: list of (frequency, word) pairs
#     """
#     common_words = []
#     for word, freq in hist.items():
#         if word in stopwords.words('english'):
#             hist[word] = None
#         elif word == 'gutenberg' or word == 'tm' or word == 'works' or word == 'project':
#             hist[word] = None
#         else:
#             t = (freq, word)
#             common_words.append(t)

#     common_words.sort()
#     common_words.reverse()
#     return common_words


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)
    pass





# def main():
#      hist = process_file(The_Modest_Proposal, skip_header=True)
#      hist1 = process_file(Time_Machine, skip_header=True)

#     print('Total number of words in The Modest Proposal:', total_words(hist))
#     print('Total number of words in Time Machine:', total_words(hist1))
#     print('Number of different words in The Modest Proposal:', different_words(hist))
#     print('Number of different words in Time Machine:', different_words(hist1))

#     t = most_common(hist, excluding_stopwords=True)
#     print('The most common words in The Modest Proposal are:')
#     for freq, word in t[0:10]:
#         print(word, '\t', freq)

#     t = most_common(hist1, excluding_stopwords=True)
#     print('The most common words in Time Machine are:')
#     for freq, word in t[0:10]:
#         print(word, '\t', freq)
   
    

    


# if __name__ == '__main__':
#     main()




hist = process_file(The_Modest_Proposal, skip_header=True)
hist1 = process_file(Time_Machine, skip_header=True)
for key, value in hist.items():
    a = [key, value]
    lst.append(a)
    return lst
for key, value in hist1.items():
    a = [key, value]
    lst1.append(a)   
    return lst1
import difflib as dl



sim = dl.get_close_matches

s = 0

wa = lst.split()
wb = lst1.split()

for i in wa:
    if sim(i, wb):
        s += 1

n = float(s) / float(len(wa))
print('%d%% similarity' % int(n * 100))