from mediawiki import MediaWiki
import re
import string
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt


def process_file(text, skip_header):
    """
    Process strings and map each word to its frequency

    text:string
    skip_header: boolean, skip header in the page
    return: map each word to the number of times it appers
    """

    frequency = {}
    text_1 = text.lower()
    out = re.sub(r"[^\w\s]", "", text_1)  # return the string
    # print(out)
    out = out.split(" ")

    for word in out:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def total_words(frequency):
    """Returns the total of the frequencies in this Wikipedia page."""

    result = 0
    f = frequency.values()
    for i in f:
        result += i
    return result


def different_words(frequency):
    """Returns the number of different words in a histogram."""

    return len(frequency)


def most_common(frequency, excluding_stopwords=False):
    """
    Makes a list of tuples and get word and frequence and load them to the tuple
    append the tuple to the list, sort the list and return the common words

    hist: map from word to frequency

    returns: list of (frequency, word) pairs, tuple, number and string
    """
    common_words = []

    filter_word = [
        "the",
        "of",
        "to",
        "and",
        "in",
        "a",
        "an",
        "is",
        "was",
        "for",
        "by",
        "from",
        "on",
        "as",
        "with",
    ]

    for word, freq in frequency.items():
        if word not in filter_word:
            common_words.append((freq, word))

    common_words.sort(reverse=True)  # high to low
    return common_words


def text_duplicates(text1, text2):
    """
    Compare two web pages's similarity (same words) and
    retrun the common word and its frequency

    text 1: first web page
    text 2: second web page

    return: list of duplicate words and its appeared times in each text page
    """
    text1_frequency = process_file(text1, None)
    text2_frequency = process_file(text2, None)

    filter_word = [
        "the",
        "of",
        "to",
        "and",
        "in",
        "a",
        "an",
        "is",
        "was",
        "for",
        "by",
        "from",
        "on",
        "as",
        "with",
    ]

    text_frequency_similarity = []

    for a, b in text1_frequency.items():
        if (a not in filter_word) and (a in text2_frequency):
            text_frequency_similarity.append((a, b, text2_frequency[a]))
    return text_frequency_similarity


def cal_similaritys(text1, text2):
    """
    Calculate two web pages's similarity and retrun its computed similarities

    text 1: first web page
    text 2: second web page
    """
    text1_frequency = process_file(text1, None)
    text2_frequency = process_file(text2, None)
    text1_num = 0
    # text2_num = 0
    for a in text1_frequency.items():
        if a in text2_frequency:
            text1_num += 1

    # for a,b in text2_frequency.items():
    #     if a in text1_frequency:
    #         text2_num +=1

    return [
        [1.0, text1_num / len(text2_frequency)],
        [text1_num / len(text2_frequency), 1.0],
    ]


def text_clustering(similaritys):
    """
    Based on similarities computed from the preivous cal_similaritys,
    use Metric Multi-dimensional Scaling (MDS) to visualize the texts in a two dimensional space

    """

    S = np.asarray(similaritys)

    dissimilarities = 1 - S

    coord = MDS(dissimilarity="precomputed").fit_transform(dissimilarities)
    plt.scatter(coord[:, 0], coord[:, 1])

    for i in range(coord.shape[0]):
        plt.annotate(str(i), (coord[i, :]))

    plt.show()


def main():
    wikipedia = MediaWiki()
    Blizzard = wikipedia.page("Blizzard Entertainment").content

    text = process_file(Blizzard, skip_header=True)
    print(text)
    print("Total number of words:", total_words(text))
    print("Number of different words:", different_words(text))

    t = most_common(text, excluding_stopwords=True)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, "\t", freq)

    take_2 = wikipedia.page("Take-Two Interactive").content
    frequency_similarity = text_duplicates(Blizzard, take_2)
    print("The duplicate words are:")

    for info in frequency_similarity:
        print(info[0] + ":" + str(info[1]) + " " + str(info[2]))

    similaritys = cal_similaritys(Blizzard, take_2)
    text_clustering(similaritys)


if __name__ == "__main__":
    main()