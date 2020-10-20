import string

def process_file(filename):
    """Makes a histogram that contains the words from a file.

    filename: string

    returns: map from each word to the number of times it appears.
    """
    hist = dict()
    fp = open(filename, encoding='UTF8')

    strippables = string.punctuation + string.whitespace

    for line in fp:
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    return hist

def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []

    stopwords = process_file('data/stopwords.txt')

    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)

def exclusive_dict(d1,d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    res = list()
    for word in d1.items():
        if word not in d2.items():
            res.append(word)
    return res
    # for  in d1:
    #     if key not in d2:
    #         res[key] = None
    # return res





def main():
    hist = process_file('data/trump.txt')

    # print(process_file('data/trump.txt'))

    # print(most_common(hist, excluding_stopwords=True))

    # print_most_common(hist, num=30)

    biden = process_file('data/biden.txt')
    exclusive_dict(hist,biden)
    # diff = exclusive_dict(hist, words)
    # print("The words in trump that aren't in biden are:")
    # for word in diff.keys():
    #     print(word, end=' ')

if __name__ == '__main__':
    main()