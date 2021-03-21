#Code developed by Raphael using the class and online ressources
from collections import Counter
from textblob import TextBlob
import random
import string
import sys
from unicodedata import category


def most_common_words(filename, n_of_words):
    """
    Gets the most common nouns from the books that are being analysed
    """
    book = open(filename, 'r', encoding='UTF8')
    book1 = book.read()
    # Removes the header and footer
    book2 = book1[1020:-18940]
    # print('hello1')

    #The punctuation that has to be removed
    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )
    # Removes the punctuation from the book
    no_punctuation = ""
    for char in book2:
        if char not in strippables:
            no_punctuation = no_punctuation + char

    # print(no_punctuation)
    # print('hello2')
    #Turns the words into single words
    blob = TextBlob(no_punctuation)
    # print(blob)
    
    # #print(Counter)

    # Will only count the words that are nouns
    Count = Counter(blob.noun_phrases)
    #print('hello2')

    #Prints the filename    
    print(filename)
    #The most common nouns in the book
    most_common = Count.most_common(n_of_words)
    print(most_common)

# un-comment the book to be run
def main():
    most_common_words('data/a_modest_proposal.txt',20)
    # most_common_words('data/cape_cod.txt',20)
    # most_common_words('data/frankenstein.txt',20)
    # most_common_words('data/mrs_dalloway_in_bond_street.txt',20)
    # most_common_words('data/the_coquette.txt',20)
    # most_common_words('data/the_great_gatsby.txt',20)


if __name__ == "__main__":
    main()