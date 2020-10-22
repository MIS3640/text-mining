# I. Extract data and store as a file

""" 1) Get data downloaded to Python"""

import urllib.request

url = "http://www.gutenberg.org/ebooks/15489.txt.utf-8"
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
freud_texts = data.decode("utf-8")
print(freud_texts)  # for testing


""" 3) Save data to a file"""
import pickle

with open("freud_texts.pickle", "wb") as fp:
    pickle.dump(freud_texts, fp)

""" 4) Load data from a file"""
with open("freud_texts.pickle", "rb") as input_file:
    reloaded_copy_of_text = pickle.load(input_file)

print(reloaded_copy_of_text)
