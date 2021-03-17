import random
import string
import sys
from unicodedata import category
import urllib.request
import pickle

<<<<<<< HEAD
def download_file(url):
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    return text

text1 = download_file('https://www.gutenberg.org/files/768/768-0.txt')
text2 = download_file('https://www.gutenberg.org/files/1260/1260-0.txt')
text3 = download_file('http://www.gutenberg.org/files/767/767-0.txt')
text4 = download_file('http://www.gutenberg.org/files/9182/9182-0.txt')
text5 = download_file('http://www.gutenberg.org/files/969/969-0.txt')
=======
url1 = 'https://www.gutenberg.org/files/768/768-0.txt'
response1 = urllib.request.urlopen(url1)
data1 = response1.read()  # a `bytes` object
text1 = data1.decode('utf-8')
url2 = 'https://www.gutenberg.org/files/1260/1260-0.txt'
response2 = urllib.request.urlopen(url2)
data2 = response2.read()  # a `bytes` object
text2 = data2.decode('utf-8')
>>>>>>> 08ae18b62150eae5e70b7800caf2a0379412eef2

with open('saved_texts.pickle','wb') as f:
    pickle.dump(text1,f)
    pickle.dump(text2,f)
<<<<<<< HEAD
    pickle.dump(text3,f)
    pickle.dump(text4,f)
    pickle.dump(text5,f)
=======



>>>>>>> 08ae18b62150eae5e70b7800caf2a0379412eef2
