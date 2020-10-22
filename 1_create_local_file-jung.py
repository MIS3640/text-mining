# I. Extract data and store as a file

""" 1) Get data downloaded to Python"""

import urllib.request

url = "http://www.gutenberg.org/files/48225/48225-0.txt"
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
jung_texts = data.decode("utf-8")
print(jung_texts)  # for testing


""" 2) Save data to a file"""
import pickle

with open("jungs_texts.pickle", "wb") as fp:
    pickle.dump(jung_texts, fp)

""" 3) Load data from a file"""
with open("jungs_texts.pickle", "rb") as input_file:
    reloaded_copy_of_text = pickle.load(input_file)

print(reloaded_copy_of_text)

#