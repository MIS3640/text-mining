# Load data
import nltk
nltk.download('vader_lexicon')
import pickle
import pprint

with open('example_file.pickle','rb') as data_input:
    reloaded_review_text = pickle.load(data_input)


# pprint.pprint(reloaded_review_text)
# print(type(reloaded_review_text))

# Clean data
# Not sure if this is neccessary
# from unicodedata import category
# import sys

# strippables = "".join(
#     [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
# )

# stripped_text = []
# for line in reloaded_review_text:
#     line = line.replace("-", " ").replace(chr(8212), " ")

#     for word in line.split():
#         word = word.strip(strippables)
#         word = word.lower()

#     stripped_text.append(line)


# pprint.pprint(stripped_text)


# Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sent_dict = {}
for i in reloaded_review_text:
    s = SentimentIntensityAnalyzer().polarity_scores(reloaded_review_text[i])
    if i not in sent_dict:
        sent_dict[i] = s

print(sent_dict)