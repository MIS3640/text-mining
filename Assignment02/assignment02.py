import random
import string
import urllib.request
from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

url = 'https://www.gutenberg.org/files/84/84-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')


def remove_punc(r):
    """
    this function will remove punctuation
    """
    punctuation = string.punctuation
    for p in r:
        if p in punctuation:
            r = r.replace(p,'')
    return r


def book_list():
    """
    this will break apart the text
    """
    book = []
    for r in text.split(): 
        r = remove_punc(r)
        r=r.lower()
        book.append(r)    
    return book

print(book_list())

def make_dict():
    words_list = book_list()
    dictionary = {}
    stop = set(stopwords.words('english'))
    for word in words_list:
        if word not in stop and word not in dictionary:
            dictionary[word] = 1
        elif word not in stop and word in dictionary:
            dictionary[word] += 1
    return dictionary
print(make_dict())


whatever=Counter(make_dict())

top_twenty= whatever.most_common(20)
print('top 20 words:')
print('words : freq')
print('--------------')
for q in top_twenty:
    print(q[0],' :', q[1])


top_twenty = dict(top_twenty) 
words = list(top_twenty.keys())
values = list(top_twenty.values())
x_pos = [i for i, _ in enumerate(words)]
plt.bar(x_pos, values, color='green') 
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency in Selected Book")
plt.xticks(x_pos, words)
plt.show()