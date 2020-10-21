import string
import pickle
 
 
def process_file(movie, source):
    """Makes a histogram that contains the words from a file.
 
    movie: string
    source: string
 
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    # opens pickle
    with open(f"{movie}_{source}.pickle", "rb") as input_file:
        fp = pickle.load(input_file)
 
    # removes extra chracters and stores into dictionary by frequency
    strippables = string.punctuation + string.whitespace
 
    for line in fp:
        line = line.replace("-", " ")
        line = line.replace('"', " ")
 
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
 
            hist[word] = hist.get(word, 0) + 1
    if "" in hist:
        del hist[""]
 
    return hist
 
 
def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
 
    hist: map from word to frequency
 
    returns: list of (frequency, word) pairs
    """
    # imports stopword.txt and creates lists
    common_words = []
    stopwords = open("stopword.txt")
    stopwords_list = []
    # turns stopwords.txt into list
    for line in stopwords:
        lin = line.strip()
        stopwords_list.append(lin)
    # sorts dictionary by frequency and returns list of tupples
    for word, freq in hist.items():
        if not excluding_stopwords or not word in stopwords_list:
            common_words.append((freq, word))
    common_words.sort(reverse=True)
    return common_words
 
 
def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
 
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist, excluding_stopwords=True)
    for freq, word in t[0:num]:
        print(f"{word:<10}", "*" * int((freq)))
 
 
def main():
    movie = "Mulan"
    hist = process_file(movie, "imdb")
    t = most_common(hist, excluding_stopwords=True)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(f"{word:<10} {freq}")
    print_most_common(hist, num=10)
 
 
if __name__ == "__main__":
    main()

