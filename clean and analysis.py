import random
import string
import sys
from unicodedata import category


def process_file(filename, skip_header):
    """Opens the file, then removes the header and footer, then seperates all the words individual and 
    Makes a histogram that contains the words from a file.
    """
    hist = {}
    book = open(filename, encoding='UTF8')

    # TODO: explain skip_header
    if skip_header:
        skip_gutenberg_header(book)

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in book:
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
    """Starts to read the book from the line startswith
    """
    for line in book:
        if line.startswith('*** START OF THIS PROJECT'):
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
<<<<<<< Updated upstream
    """
=======
    """ 

    #Pseudo-code
    #1. create a list for return, freq_word_list
    #2. Use for to loop over the dictionary, hist
    #  1. get the word, freq from hist
     # 2. create a tuple this way (freq, word)
      #3. append the tuple to freq_word_list
    #3. sort freq_word_list
    #4. return it
>>>>>>> Stashed changes


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


def main():
    # # A Modest Proposal by Jonathan Swift (UK 18th century)
    # hist = process_file('data/a_modest_proposal.txt', skip_header=True)

    # The Coquette by Hannah Webster Foster (US 18th century)
    hist = process_file('data/the_coquette.txt', skip_header=True)

    # # Frankenstein by Mary Wollstonecraft (Godwin) Shelley (UK 19th century)
    # hist = process_file('data/frankenstein.txt', skip_header=True)

    # # Cape Cod by Henry David Thoreau (US 19th century)
    # hist = process_file('data/cape_cod.txt', skip_header=True)

    # # Mrs Dalloway in Bond Street, by Virginia Woolf (UK 18th century)
    # hist = process_file('data/mrs_dalloway_in_bond_street.txt', skip_header=True)
    
    # # The Great Gatsby by F. Scott Fitzgerald (US 20th century)
    # hist = process_file('data/the_great_gatsby.txt', skip_header=True)



    print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

def most_common(hist, including_stopwords=True) 


    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main() 

