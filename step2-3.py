### Load data
import pickle
import pprint
with open('review_data.pickle','rb') as data_input:
    reloaded_review_text = pickle.load(data_input)
# pprint.pprint(reloaded_review_text)
# print(type(reloaded_review_text))


### Remove punctuations
from unicodedata import category
import sys

def remove_punct(imdb_data_list):
    """
    Removes punctuations in the reviews and puts it back in the original data list 
    """
    strippables = "".join(
    [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")])
    stripped_text = []

    for movie in reloaded_review_text:
        for sub_list in movie['review_info']:
            t = sub_list['review_text'] 
            t = t.replace("-", " ").replace(chr(8212), " ")
            new_t = ("".join(x for x in t if x not in strippables))
            sub_list['review_text'] = new_t

    return reloaded_review_text

cleaned = remove_punct(reloaded_review_text)
pprint.pprint(cleaned)

### Save data
import pickle
with open("review_data.pickle", "wb") as f:
    pickle.dump(cleaned, f)

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
            del sub_list['review_text']
        # pprint.pprint(sub_list)
    return reloaded_review_text

sent_dict = sent_analysis()
# pprint.pprint(sent_dict)

### Save data
import pickle
with open("sent_data.pickle", "wb") as f:
    pickle.dump(sent_dict, f)

# create list for imdb rating and compound scores
imdb_rating_list = []
compound_list = []
for movie in sent_dict:    
    for user in movie['review_info']:
        imdb_rating_list.append(user['imdb_rating']) # list for imdb rating
        compound_list.append(user['sentiment_score']['compound']) # list for compound score

# print(len(imdb_rating_list))
# print(len(compound_list))

import matplotlib.pyplot as plt

plt.scatter(imdb_rating_list, compound_list)
plt.xlabel('IMDB rating')
plt.ylabel('compound score')
plt.title('IMDB rating vs. compound score')
plt.show() # scatter plot


# for average compound score by movie (bar chart)
avg_compound_list = []
for movie in sent_dict:
    compound_list = []
    for user in movie['review_info']:
        compound_list.append(user['sentiment_score']['compound'])
    avg_compound = sum(compound_list)/len(compound_list) # finding mean
    avg_compound_list.append(avg_compound)
    
print(avg_compound_list)

data = avg_compound_list
plt.bar(['I', 'II', 'III', 'IV', 'V', 'VI','VII','VIII','IX'], data)
plt.xlabel('movie #')
plt.ylabel('average compound score')
plt.title('Average Compound Score by Movie')
plt.bar(range(len(data)), data) 
plt.show() # print bar chart


