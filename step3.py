
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

def sent_analysis():
    """Analyzes the sentiment of each review and add the score
    to the dictionary"""
    for movie in reloaded_review_text:
        for sub_list in movie['review_info']:
            t = sub_list['review_text'] 
            s = SentimentIntensityAnalyzer().polarity_scores(t)
            sub_list['sentiment_score'] = s
        # pprint.pprint(sub_list)
    return reloaded_review_text


print(sent_analysis())


