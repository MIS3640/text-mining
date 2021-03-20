#Code developed by Raphael using the class and online ressources
import random
import string
import sys
from unicodedata import category


def process_file(filename, skip_header):
    """
    Opens the book from data and start to read it after the header and ends before the footer. Removes all of the punctuation and turns the book into individual words.
    It then counts the amount of times each word appears and saves it into a histogram
    """
    hist = {}
    book = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(book)

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in book:
        if line.startswith('*** END'):
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
    """
    Starts to read the book after the header
    """
    for line in book:
        if line.startswith('*** START'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def main():
    # A Modest Proposal by Jonathan Swift (UK 18th century)
    hist = process_file('data/a_modest_proposal.txt', skip_header=True)

    # # The Coquette by Hannah Webster Foster (US 18th century)
    # hist = process_file('data/the_coquette.txt', skip_header=True)

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

if __name__ == "__main__":
    main()

    #Sakshi code

    # t = most_common(hist, excluding_stopwords=True)
    # print('The most common words are:')
    # for frequent, word in t[0:20]: 'data/a_modest_proposal.txt'
    # print(word, '\t', frequent)

    # words = process_file('words.txt', skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=' ')



#     wordstring = 'data/a_modest_proposal.txt'
#     wordstring += 'data/the_coquette.txt'

# wordlist = wordstring.split()

# wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))

# print("String\n" + wordstring +"\n")
# print("List\n" + str(wordlist) + "\n")
# print("Frequencies\n" + str(wordfreq) + "\n")
# print("Pairs\n" + str(list(zip(wordlist, wordfreq))))

# import math 
# import string 
# import sys 

# reading the text file 
# This functio will return a 
# list of the lines of text 
# in the file. 
# def read_file(filename): 'data/a_modest_proposal.txt'
	
# try: 
# 	with open('data/a_modest_proposal.txt', 'r') as f: 
# 			data = f.read() 
	  
	
# except IOError: 
# 	print("Error opening or reading input file: ", filename) 
# 	sys.exit() 

# # splitting the text lines into words 
# # translation table is a global variable 
# # mapping upper case to lower case and 
# # punctuation to spaces 
# translation_table = str.maketrans(string.punctuation+string.ascii_uppercase, 
# 									" "*len(string.punctuation)+string.ascii_lowercase) 
	
# # returns a list of the words 
# # in the file 
# def get_words_from_line_list(text): 
	
# 	text = text.translate(translation_table) 
# 	word_list = text.split() 
	
# 	return word_list 
