import random
import string
import sys
import pickle
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

with open('saved_texts.pickle','rb') as input_file:
    Wuthering_Height = pickle.load(input_file)
    Jane_Eyre = pickle.load(input_file)


def process_file(text, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    if skip_header:
        skip_gutenberg_header(text)

    strippables = string.punctuation + string.whitespace

    for line in text.split('/n'):
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

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
        if line.startswith('*** START OF THIS PROJECT'):
            break


# def total_words(hist):
#     """Returns the total of the frequencies in a histogram."""
#     return sum(hist.values())

# def different_words(hist):
#     """Returns the number of different words in a histogram."""
#     return len(hist)

def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    common_words = []
    for word, freq in hist.items():
        if word in stopwords.words('english'):
            hist[word] = None
        elif word == 'mr' or word == 'would' or word == 'i' or word == 'said' or word == 'catherine' or word == 'jane' or word == 'john':
            hist[word] = None
        else:
            t = (freq, word)
            common_words.append(t)

    common_words.sort()
    common_words.reverse()
    return common_words


def print_most_common(hist, num=100):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        return word, '\t', freq
        print(word, '\t', freq)


hist = process_file(Wuthering_Height, skip_header=True)
hist1 = process_file(Jane_Eyre, skip_header=True)
   
s1 = set(print_most_common(hist, num = 100))
s2 = set(print_most_common(hist1, num=100))
l1 =[]
l2 =[] 

rvector = s1.union(s2)  
for w in rvector: 
    if w in s1: 
        l1.append(1) # create a vector 
    else: 
        l1.append(0) 
    if w in s2: 
        l2.append(1) 
    else: 
        l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine) 



def main():
    hist = process_file(Wuthering_Height, skip_header=True)
    hist1 = process_file(Jane_Eyre, skip_header=True)

#     print('Total number of words in Wuthering Height:', total_words(hist))
#     print('Total number of words in Jane Eyre:', total_words(hist1))
#     print('Number of different words in Wuthering Height:', different_words(hist))
#     print('Number of different words in Jane Eyre:', different_words(hist1))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words in Wuthering Height are:')
    for freq, word in t[0:100]:
        print(word, '\t', freq)

    t = most_common(hist1, excluding_stopwords=True)
    print('The most common words in Jane Eyre are:')
    for freq, word in t[0:100]:
        print(word, '\t', freq)
   
    

    


if __name__ == '__main__':
    main()




# import nltk, string
# from sklearn.feature_extraction.text import TfidfVectorizer
# hist = process_file(Wuthering_Height, skip_header=True)
# hist1 = process_file(Jane_Eyre, skip_header=True)
# def cosine_sim(text1, text2):
#     tfidf = TfidfVectorizer().fit_transform(text1, text2)
#     return ((tfidf * tfidf.T).A)[0,1]
# print(cosine_sim(hist, hist1))