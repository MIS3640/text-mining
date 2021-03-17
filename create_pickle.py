import random
import string
import sys
from unicodedata import category
import urllib.request
import pickle

url1 = 'https://www.gutenberg.org/files/768/768-0.txt'
response1 = urllib.request.urlopen(url1)
data1 = response1.read()  # a `bytes` object
text1 = data1.decode('utf-8')
url2 = 'https://www.gutenberg.org/files/1260/1260-0.txt'
response2 = urllib.request.urlopen(url2)
data2 = response2.read()  # a `bytes` object
text2 = data2.decode('utf-8')

with open('saved_texts.pickle','wb') as f:
    pickle.dump(text1,f)
    pickle.dump(text2,f)



