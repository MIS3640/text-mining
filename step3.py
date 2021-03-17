# Load data
import nltk
import pickle
import pprint

with open('review_data.pickle','rb') as data_input:
    reloaded_review_text = pickle.load(data_input)

# pprint.pprint(reloaded_review_text)
# print(type(reloaded_review_text))

# Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sent_dict = {}
for i in reloaded_review_text:
    s = SentimentIntensityAnalyzer().polarity_scores(reloaded_review_text[i])
    if i not in sent_dict:
        sent_dict[i] = s

print(sent_dict)