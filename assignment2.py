import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
import os
import time


Url_list = [
    "http://www.gutenberg.org/ebooks/699.txt.utf-8",
    "http://www.gutenberg.org/ebooks/730.txt.utf-8",
]
Book_names = ["A Child's Story of England", "Oliver Twist"]
for i in range(len(Url_list)):
    response = urllib.request.urlopen(Url_list[i])
    time.sleep(3)
    data = response.read()  # a `bytes` object
    text = data.decode("utf-8")
    # print(text) # for testing
    with open(Book_names[i] + ".txt", "w", encoding="UTF-8") as f:
        f.write(text)
    f.close()


"""
Now we have two books in hand. 
The next step is to clean the data.
"""
with open(Book_names[0] + ".txt", "r", encoding="UTF-8") as f:
    book1 = f.read()
    f.close()
with open(Book_names[1] + ".txt", "r", encoding="UTF-8") as f:
    book2 = f.read()
    f.close()

# def cleaner(data):
def cleaner(data):
    contents = list(data)
    k = 0
    while k < len(contents):
        if (contents[k].isalnum() == False) & (contents[k] != " "):
            contents[k] = " "
        k += 1
    contents = "".join(contents)
    contents = contents.split()
    for i in range(len(contents) - 1):
        if (contents[i] == "CHAPTER") & (contents[i + 1] == "I"):
            break
    contents = contents[i:]
    for i in range(len(contents)):
        if contents[i] == "END":
            break
    contents = contents[:i]
    return contents
    # contents=''.join(contents)


cleaned_book1 = cleaner(book1)
cleaned_book2 = cleaner(book2)
"""
Now we have cleaned dataset of two books contains only words in main body.
Firstly find the word frequency

"""
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

contents = cleaned_book1
contents = " ".join(contents)
contents = contents.lower()
contents_list = contents.split()
word_list = np.unique(contents_list)
total_words = len(contents_list)
word_dict = {}
for word in word_list:
    word_dict[word] = contents_list.count(word)
sorted_list = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)
df = pd.DataFrame(sorted_list)
df.columns = ["Words", "counts"]
df["Frequencies"] = df["counts"] / total_words


contents = cleaned_book2
contents = " ".join(contents)
contents = contents.lower()
contents_list = contents.split()
word_list = np.unique(contents_list)
total_words = len(contents_list)
word_dict = {}
for word in word_list:
    word_dict[word] = contents_list.count(word)
sorted_list = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)
df2 = pd.DataFrame(sorted_list)
df2.columns = ["Words", "counts"]
df2["Frequencies"] = df["counts"] / total_words

print(df)
print(df2)

df3 = pd.merge(df.iloc[:100, :], df2.iloc[:100, :], on="Words")
fig = plt.figure(figsize=(12, 4))
plt.plot(df3["Words"], df3.loc[:, ["Frequencies_x", "Frequencies_y"]])
plt.xticks(rotation=90)

plt.show()

sentence = " ".join(cleaned_book1)
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

sentence = " ".join(cleaned_book2)
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)