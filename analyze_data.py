import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    # if skip_header:
    #     skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist) 


def most_common(hist, excluding_stopwords = False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = [] 

    stopwords = process_file('delete_words.txt', skip_header=False)

    stopwords = list(stopwords.keys()) 

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word)) 
    t.sort(reverse=True)
    return t


def sentiment_analysis(filename):
    score = SentimentIntensityAnalyzer().polarity_scores(filename)
    print(score)


def main():
    hist = process_file('tweets.txt', skip_header = False)
    print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist, excluding_stopwords = True)
    print('The most common words are:')
    for freq, word in t[0:40]:
        print(word, '\t', freq)

    print(sentiment_analysis('tweets.txt'))


if __name__ == '__main__':
    main()
