import random
import string
import sys
from unicodedata import category

# with open("test.txt") as f:
#     for line in f:
#         if line.rstrip() == "***a":
#             print("")
#             for line in f:
#                 if line.rstrip() == "---a":
#                     break
#                 print(line.rstrip())
# Which for:

# ***a
# foo bar
# lorem ipsum
# dolor
# ---a
# ***a
# bar bar
# foobar
# foob
# ---a
# xzy = 'CAPE COD'
# with open('data/cape_cod.txt', encoding = 'UTF8') as f:
#         for line in f:
#             if line.rstrip() == f'*** START OF THIS PROJECT GUTENBERG EBOOK {xzy} ***':
#                 print("")
#                 for line in f:
#                     if line.rstrip() == f'*** END OF THIS PROJECT GUTENBERG EBOOK {xzy} ***':
#                         break
#                     print(line.rstrip())

# with open('data/cape_cod.txt', encoding = 'UTF8') as f:
#         for line in f:
#             if line.startswith('*** START OF THIS PROJECT'):
#                 print("")
#                 for line in f:
#                     if line.startswith('*** END OF THIS PROJECT'):
#                         break
#                     # text = line.decode('utf-8')
#                     fout = open('data/cape_cod_c.txt','w',encoding="utf-8")
#                     # fout.write(line)
#                     # fout.close()
#                     for i in line:
#                         fout.write(i + '\n')
#                     fout.close()

# print('dsa')           
# print(type(text))
# print(text)
# fout = open('data/cape_cod_c.txt','w')
# fout.write(text)
# fout.close()

# myText = open(r'path where the text file will be created\file name.txt','w')
# myString = 'Type your string here'
# myText.write(myString)
# myText.close()

        #             for line in book:
        # if line.startswith('*** START OF THIS PROJECT'):
        #     break

# f'Percentage increase {P:.2f}%'
# with open('data/cape_cod.txt', encoding = 'UTF8') as f:
#     # itertools.imap python2
#     f = map(str.rstrip, f)
#     for line in f:
#         if line == "***a":
#             print("")
#             for line in f:
#                 if line == "---a":
#                     break
#                 print(line)

def clean_book(filename):
    # cleaned = ()
    # book = open(filename, encoding = 'UTF8')
    
    # print(line.starts)
    
    # cleaned = line
    # return cleaned

    # if skip_footer:
    #     skip_gutenberg_footer(book) 

    # print(book)
    with open(filename, encoding = 'UTF8') as f:
        for line in f:
            if line.rstrip() == '*** START OF THIS PROJECT':
                print("")
                for line in f:
                    if line.rstrip() == '*** END OF THIS PROJECT':
                        break
                    print(line.rstrip())

    

    

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    # TODO: explain skip_header
    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ').replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(book):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in book:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def skip_gutenberg_footer(book):
    for line in book:
        if line.startswith('*** END OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    # Pseudo-code
    # 1. create a list for return, freq_word_list
    # 2. Use for to loop over the dictionary, hist
    #   1. get the word, freq from hist
    #   2. create a tuple this way (freq, word)
    #   3. append the tuple to freq_word_list
    # 3. sort freq_word_list
    # 4. return it


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    pass


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    pass


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    pass


# def main():

    # print('Total number of words:', total_words(hist))
    # print('Number of different words:', different_words(hist))

    # clean = clean_book('data/cape_cod.txt')

    # print(clean)

    # t = most_common(hist, excluding_stopwords=True)
    # print('The most common words are:')
    # for freq, word in t[0:20]:
    #     print(word, '\t', freq)

    # words = process_file('words.txt', skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=' ')


# if __name__ == '__main__':
#     main()