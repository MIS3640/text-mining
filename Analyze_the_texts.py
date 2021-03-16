import random
import string
import sys
from unicodedata import category
import urllib.request

url1 = 'http://www.gutenberg.org/files/1080/1080-0.txt'
response1 = urllib.request.urlopen(url1)
data1 = response1.read()  # a `bytes` object
text1 = data1.decode('utf-8')
url2 = ''
response2 = urllib.request.urlopen(url2)
data2 = response2.read()  # a `bytes` object
text2 = data2.decode('utf-8')
print(text1) # for testing





