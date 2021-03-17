import sys
from unicodedata import category
import string
from collections import Counter

def word_summary(filename):
    """this function takes away any strippables"""
    hist = {}
    fp = open(filename, encoding = 'UTF8')

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )
    for line in fp:

        line = line.replace('-', ' ').replace(chr(8212), ' ').replace('=', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def total_words(hist):
    """returns the total number of words"""
    return sum(hist.values())


def sorted_words(hist):
    for word in sorted(hist, reverse= True):
        print(word)


def most_frequent(hist):
    count, itm = 0, ''
    for item in reversed(hist):
         hist[item] = hist.get(item, 0) + 1
         if hist[item] >= count :
             count, itm = dict[item], item

    return(itm)

    


def main():
    filename ='Iphone.txt'
    hist = word_summary('Iphone.txt')
    print(hist)
    print('Total number of words:', total_words(hist))
    print(most_frequent(hist))
   
    




if __name__ == '__main__':
    main()