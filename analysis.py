import sys
from unicodedata import category
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer



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

    # dict = {}
    # count, itm = 0, ''
    # for item in reversed(hist):
    #      dict[item] = dict.get(item, 0) + 1
    #      if dict[item] >= count :
    #          count, itm = dict[item], item

    # return(itm)


def top_ten(hist):
    """this function returns the top 10 frequent words"""
    x = sorted(hist.items(), key=lambda item: item[1], reverse= True)[0:10]
    return x



def bottom_ten(hist):
    """this function returns the top 10 frequent words"""
    x = sorted(hist.items(), key=lambda item: item[1], reverse= False)[0:10]
    return x


def feeling(filename):
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return score





def main():
    filename ='Iphone.txt'
    hist = word_summary('Iphone.txt')

    # # print(hist)
    # print('Total number of words:', total_words(hist))
    # # # print(ordered_frequency(hist))
    # print('the top ten words are:', top_ten(hist))
    # print('the 10 least used words are:', bottom_ten(hist))
    print(feeling)

    



if __name__ == '__main__':
    main()