import urllib.request
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt


def download_url(url):
    """Download a book from Project Gutenberg.
    url: url of the book
    returns: string
    """
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    return text


def process_url(text, skip_header=True):
    """
    Process a string and map each word to its frequency
    text: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns:map from each word to the number of times it appears.
    """
    word_list = {}
    strippables = string.punctuation + string.whitespace + "“" + "”"
    skip = True
    for line in text.split('\n'):
        if skip_header:
            if line.startswith('*** START OF THIS PROJECT'):
                skip = False
                continue

        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        if not skip:
            for word in line.split():
                word = word.strip(strippables)
                word = word.lower()
                word_list[word] = word_list.get(word, 0) + 1

    return word_list


def most_common(word_list, excluding_stopwords=True, excluding_names=True, name_list=[]):
    """
    Return a list of most common words, excluding stopwords and names
    word_list: word_listogram (map from word to frequency)
    excluding_stopwords: boolean, whether to exclude stopwords
    excluding_names: boolean, whether to exclude names
    """
    common_words = []
    stopwords = []
    f = open("stopwords.txt", encoding='utf8')
    for line in f:
        for word in line.split():
            stopwords.append(word)

    for word, freq in word_list.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        if excluding_names:
            if word in name_list:
                continue
        common_words.append((freq, word))

    common_words.sort(reverse=True)
    return common_words


def print_most_common(common_words, num=10, printing=True, book_name=""):
    """
    Prints the most commons words in a word list and their frequencies
    common_words: a list of words sorted by frequency
    """
    print(f'The most common words in {book_name} are:')
    for freq, word in common_words[0:num]:
        print(word, '\t', freq)
    return


def different_common(list1, list2, num=100):
    """List the words that are included in the 100 most common words in list 1 but not in list2
    list1, list2: a list of tuples (frequency, word), from most common to least common
    num: number of most common words in list1
    """
    dif = []
    for i in range(num):
        include = False
        for j in range(num):
            if list1[i][1] == list2[j][1]:
                include = True
        if not include:
            dif.append(list1[i][1])
    return dif


def exclude_name(*names):
    """
    List all the main characters' names
    names: string
    return: a list of all the input characters' names
    """
    name_list = []
    for name in names:
        name = name.lower()
        name_list.append(name)
    return name_list


def sentiment_analysis(text):
    """
    returns the sentiment in the text: negative, positive, or neutral
    """
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return(score)


def text_similarity(dict1, dict2):
    """
    Calculates the cosine similarity between two dictionary
    dict1, dict2: two dictionary with words and the frequency
    returns: cosine similarity, a number between 0 and 1
    """
    set1 = {word for word in dict1.keys()}
    set2 = {word for word in dict2.keys()}
    word_union = set1.union(set2)
    vector1 = []
    vector2 = []
    for word in word_union:
        if word in set1:
            vector1.append(dict1[word])
        else:
            vector1.append(0)
        if word in set2:
            vector2.append(dict2[word])
        else:
            vector2.append(0)

    product1 = 0
    sum1 = 0
    sum2 = 0
    for i in range(len(word_union)):
        product1 += vector1[i]*vector2[i]
        sum1 += vector1[i]**2
        sum2 += vector2[i]**2

    cosine = product1/(sum1*sum2)**0.5

    return cosine


def similarity_matrix(*lists):
    """
    Returns a matrix of similarities between each elements in lists
    """
    sim_array = []
    for i in range(len(lists)):
        sim_row = []
        for j in range(len(lists)):
            sim = text_similarity(lists[i], lists[j])
            sim_row.append(sim)
        sim_array.append(sim_row)
    return sim_array


def main():
    littleWomenUrl = 'http://www.gutenberg.org/ebooks/514.txt.utf-8'
    littleWomenTxt = download_url(littleWomenUrl)
    # print(littleWomenTxt)
    littleWomenList = process_url(littleWomenTxt)
    # print(littleWomenList)

    scarletUrl = 'http://www.gutenberg.org/files/244/244-0.txt'
    scarletTxt = download_url(scarletUrl)
    # print(scarletTxt)
    scarletList = process_url(scarletTxt)
    # print(scarletList)

    littleWomenName = exclude_name(
        "Jo", "Meg", "Beth", "Amy", "Laurie", "March", "mother", "father")
    littleWomenCommon = most_common(littleWomenList, name_list=littleWomenName)
    # print_most_common(littleWomenCommon, book_name="Little Women")

    scarletName = exclude_name(
        "Sherlock", "Holmes", "Jefferson", "Stangerson", "Lucy", "Lestrade", "Gregson")
    scarletCommon = most_common(scarletList, name_list=scarletName)
    # print_most_common(scarletCommon, book_name="A Study in Scarlet")

    # print(different_common(scarletCommon, littleWomenCommon, num=100))
    # print(different_common(littleWomenCommon, scarletCommon, num=100))

    # print(f"Little Women {sentiment_analysis(littleWomenTxt)}")
    # print(f"A Study in Scarlet: {sentiment_analysis(scarletTxt)}")

    signOfFourUrl = "http://www.gutenberg.org/files/2097/2097-0.txt"
    signOfFourTxt = download_url(signOfFourUrl)
    signOfFourList = process_url(signOfFourTxt)

    adventureHolmesUrl = "http://www.gutenberg.org/files/1661/1661-0.txt"
    adventureHolmesTxt = download_url(adventureHolmesUrl)
    adventureHolmesList = process_url(adventureHolmesTxt)

    romeoJulietUrl = "http://www.gutenberg.org/cache/epub/1112/pg1112.txt"
    romeoJulietTxt = download_url(romeoJulietUrl)
    romeoJulietList = process_url(romeoJulietTxt)

    hamletUrl = "http://www.gutenberg.org/files/27761/27761-0.txt"
    hamletTxt = download_url(hamletUrl)
    hamletList = process_url(hamletTxt)

    othelloUrl = "http://www.gutenberg.org/files/1531/1531-0.txt"
    othelloTxt = download_url(othelloUrl)
    othelloList = process_url(othelloTxt)

    macbethUrl = "http://www.gutenberg.org/files/1533/1533-0.txt"
    macbethTxt = download_url(macbethUrl)
    macbethList = process_url(macbethTxt)

    learUrl = "http://www.gutenberg.org/files/1532/1532-0.txt"
    learTxt = download_url(learUrl)
    learList = process_url(learTxt)

    merchantVeniceUrl = "http://www.gutenberg.org/files/1515/1515-0.txt"
    merchantVeniceTxt = download_url(merchantVeniceUrl)
    merchantVeniceList = process_url(merchantVeniceTxt)

    midsummerUrl = "http://www.gutenberg.org/files/1514/1514-0.txt"
    midsummerTxt = download_url(midsummerUrl)
    midsummerList = process_url(midsummerTxt)

    # print(text_similarity(adventureHolmesList, signOfFourList))
    sim_matrix = similarity_matrix(littleWomenList, scarletList, signOfFourList,
                                   adventureHolmesList, romeoJulietList, hamletList, othelloList, macbethList, learList, merchantVeniceList, midsummerList)
    S = np.asarray(sim_matrix)
    dissimilarities = 1 - S
    coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)
    plt.scatter(coord[:, 0], coord[:, 1])
    for i in range(coord.shape[0]):
        plt.annotate(str(i), (coord[i, :]))
    plt.show()


if __name__ == "__main__":
    main()
