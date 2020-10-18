import random
import string


def create_dictionary(filename):
    """Makes a histogram that contains the words from a file.

    filename: string

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding="UTF8")

    strippables = string.punctuation + string.whitespace

    for line in fp:
        line = line.replace("-", " ")

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


#  Question 1 - What are the top 10 frequent words in each text, with stopwords removed?
def most_common(hist):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency that do not include the stopwords.

    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is true, do not include any stopwords in the list.

    returns: list of (frequency, word) pairs
    """
    t = []
    stopwords = list("data/stopwords.txt")
    for word, freq in hist.items():
        if word not in stopwords:
            t.append((freq, word))
        else:
            continue
    t.sort(reverse=True)
    return t


def main():
    """code that runs all the functions above to answer our questions with regards to the 10 texts."""
    # Create Dictionaries
    emma_hist = create_dictionary("data/emma.txt")
    men_hist = create_dictionary("data/little_men.txt")
    women_hist = create_dictionary("data/little_women.txt")
    mansfield_hist = create_dictionary("data/mansfield_park.txt")
    poirot_hist = create_dictionary("data/poirot_investigates.txt")
    pride_hist = create_dictionary("data/pride_and_prejudice.txt")
    sense_hist = create_dictionary("data/sense_and_sensibility.txt")
    cask_hist = create_dictionary("data/the_cask_of_amontillado.txt")
    raven_hist = create_dictionary("data/the_raven.txt")

    # Number 1. Most Frequent Words
    t = most_common(emma_hist)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, "\t", freq)


if __name__ == "__main__":
    main()