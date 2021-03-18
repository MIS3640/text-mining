import sys
from unicodedata import category
import string
import pprint


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


def ordered_frequency(hist):
    """this function returns an ordered list of words by frequency"""
    x = sorted(hist.items(), key=lambda item: item[1], reverse= True)
    return x


def top_ten(hist):
    """this function returns the top 10 frequent words"""
    x = sorted(hist.items(), key=lambda item: item[1], reverse= True)[0:10]
    return x


def after_10(hist):
    """this function returns the top 11-20 frequent words"""
    x = sorted(hist.items(), key=lambda item: item[1], reverse= True)[11:20]
    return x


def after_20(hist):
    """this function returns the top 21-30 frequent words"""
    x = sorted(hist.items(), key=lambda item: item[1], reverse= True)[21:30]
    return x


def unique_words(hist):   
    return len(hist)



def bottom_ten(hist):
    """this function returns the top 10 frequent words"""
    x = sorted(hist.items(), key=lambda item: item[1], reverse= False)[0:3350]
    return x


def words_the(hist):
    """this function returns a list of words that have the in it"""
    x = filter(lambda hist: 'the' in hist, hist)
    return list(x)


def words_phone(hist):
    """this function returns a list of words that have phone in it"""
    x = filter(lambda hist: 'phone' in hist, hist)
    return list(x)

def words_tech(hist):
    """this function returns a list of words that have tech in it"""
    x = filter(lambda hist: 'tech' in hist, hist)
    return list(x)

def words_apple(hist):
    """this function returns a list of words that have apple in it"""
    x = filter(lambda hist: 'apple' in hist, hist)
    return list(x)


    

    





def main():
    filename ='Iphone.txt'
    hist = word_summary('Iphone.txt')
    
    
    # print(hist)
    print('Total number of words:', total_words(hist))
    print("there are",unique_words(hist),"unique words in this wikipedia page")
    print(ordered_frequency(hist)) 
    # print(type(ordered_frequency(hist)))

    print('the top ten words are:', top_ten(hist))
    print('the next top ten words are:', after_10(hist))
    print('the next top ten words are:', after_20(hist))

    print('the ten least used words are:', bottom_ten(hist))

    print(words_the(hist))
    print("the number of words that have the in it is", len(words_the(hist)))

    print(words_phone(hist))
    print("the number of words that have phone in it is",len(words_phone(hist)))

    print(words_tech(hist))
    print("the number of words that have tech in it is",len(words_tech(hist)))

    print(words_apple(hist))
    print("the number of words that have apple in it is",len(words_apple(hist)))

   
    



if __name__ == '__main__':
    main()