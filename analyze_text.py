import random
import string
import sys
import pickle
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

# Unpicking the first two books
with open("saved_texts.pickle", "rb") as input_file:
    Wuthering_Height = pickle.load(input_file)
    Jane_Eyre = pickle.load(input_file)


def process_file(text, skip_header):
    """Makes a histogram that contains the words from a file.
    text: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    if skip_header:
        skip_gutenberg_header(text)

    strippables = string.punctuation + string.whitespace

    for line in text.split("/n"):
        if line.startswith("*** END OF THIS PROJECT"):
            break

        line = line.replace("-", " ")

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(text):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in text:
        if line.startswith("*** START OF THIS PROJECT"):
            break


def total_words(h):
    """Returns the total of the frequencies in a histogram."""
    return sum(h.values())


def different_words(h):
    """Returns the number of different words in a histogram."""
    return len(h)


def most_common(h, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    h: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    common_words = []
    for word, freq in h.items():
        if word not in stopwords.words("english") or [
            "mr",
            "would",
            "said",
            "catherine",
            "jane",
            "john",
        ]:
            t = (freq, word)
            common_words.append(t)

    common_words.sort()
    common_words.reverse()  # sort in descending order
    return common_words


def print_most_common(h, num=100):
    """Prints the top 100 most commons words in a histgram and their frequencies.
    h: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(h)
    print("The most common words are:")
    for freq, word in t[:num]:
        return word, "\t", freq


def main():
    hist = process_file(Wuthering_Height, skip_header=True)
    hist1 = process_file(Jane_Eyre, skip_header=True)

    print("Total number of words in Wuthering Height:", total_words(hist))
    print("Total number of words in Jane Eyre:", total_words(hist1))
    print("Number of different words in Wuthering Height:", different_words(hist))
    print("Number of different words in Jane Eyre:", different_words(hist1))

    t = most_common(hist, excluding_stopwords=True)
    print("The top 100 most common words in Wuthering Height are:")
    for freq, word in t[0:100]:
        print(word, "\t", freq)

    t = most_common(hist1, excluding_stopwords=True)
    print("The top 100 most common words in Jane Eyre are:")
    for freq, word in t[0:100]:
        print(word, "\t", freq)


if __name__ == "__main__":
    main()
