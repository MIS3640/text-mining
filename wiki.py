from mediawiki import MediaWiki
import random 
import string 


def process_file(source):
    """Makes a histogram that contains the words from a file and their occurances.
    source: string
    """
    hist = {}

    strippables = string.punctuation + string.whitespace
    for word in content.split(): #basic cleaning 
        word = word.strip(strippables)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

    return hist


def most_common(histogram):
    """Makes a list of word-freq pairs in descending order of frequency.
    histogram: map from word to frequency
    returns: list of 10 mostly used (frequency, word) pairs except the stopwords
    """
    top_10 = []
    t = [] 
    stopwords = open('assignment 2/stopwords.txt')

    stopwords = stopwords.read().split('\n')
    # stopwords = list(stopwords)
    # print(stopwords)

    for word, freq in hist.items(): #filter out stopwords
        if word in stopwords:
            continue
        else:
            t.append((freq, word)) 
            
    t.sort(reverse=True) #from most used to least used 
    # return t
    top_10 = t[0:10] 
    return(top_10)


#run through program to get words from search of "feminism"
wikipedia = MediaWiki()
ws = wikipedia.page("feminism")
content = ws.content
hist = process_file(content)
print('The ten most common words in wiki search for \"Feminism\" are:')
print(most_common(hist))
############### sentiment analysis #######################
# import nltk
# nltk.download('vader_lexicon')
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sentence = contents
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)


#run through program to get words from search of "patriarchy"
ws = wikipedia.page("patriarchy")
content = ws.content
hist = process_file(content)
print(hist)
print('The ten most common words in wiki search for \"Patriarchy\" are:')
print(most_common(hist))
############### sentiment analysis #######################
# import nltk
# nltk.download('vader_lexicon')
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sentence = contents
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)