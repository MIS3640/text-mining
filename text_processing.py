import random
import string


def process_str(s):
    """Makes a histogram that contains the words from a string, s.

    returns: map from each word to the number of times it appears.
    """
    hist = {}

    strippables = string.punctuation + string.whitespace
    for word in s.split():
        # word could be 'Sussex.'
        word = word.strip(strippables)
        word = word.lower()
        # update the dictionary
        hist[word] = hist.get(word, 0) + 1

    return hist


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    freq = []
    for key in hist:
        if hist[key] not in freq:
            freq.append(hist[key])
    freq.sort()
    freq.reverse()

    pairs = []
    for n in freq:
        for key in hist:
            if n == hist[key] and key != "":
                temp = (key, n)
                pairs.append(temp)
    return pairs


def main():
    process_str("aaaaaaaaaabbbbbbbbbbbbbbbccccccccccc")


if __name__ == "__main__":
    main()