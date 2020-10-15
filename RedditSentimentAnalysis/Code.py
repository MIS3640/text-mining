import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt
import seaborn as sns
from keras_preprocessing.text import Tokenizer
from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
sns.set(style='darkgrid', context='talk', palette='Dark2')

import praw

reddit = praw.Reddit(client_id='-TsFhkdUc3g7Rg',
                     client_secret='9vDtLQINo05-HOjGKGyqH8KgB7k',
                     user_agent='hfu32')

headlines = set() 

for submission in reddit.subreddit('Coronavirus').new(limit=None):
    """
    Iterates through headlines in /r/Coronavirus
    """
    headlines.add(submission.title)

print(len(headlines))

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for line in headlines:
    """
    Appends each sentiment to a list called results 
    """
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:3], width=100)

# Prints dataframe 

df = pd.DataFrame(results)
print("Printing df below")
print(df.head())

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()

# Saves data to Excel for further exploration 

df2 = df[['headline', 'label']]
df2.to_csv('reddit_headlines_labels.csv', mode='a', encoding='utf-8', index=False)

# Prints positive and negative headlines

print("Positive headlines:\n")
pprint(list(df[df['label'] == 1].headline)[:5], width=200)

print("\nNegative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:5], width=200)


# How many total positives and negatives in dataset 

print(df.label.value_counts())

print(df.label.value_counts(normalize=True) * 100)

# Use matplotlib to create bar chart

fig, ax = plt.subplots(figsize=(8, 8))

counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

plt.show()

# NLTK imports 

from nltk.tokenize import word_tokenize, RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

def process_headlines(headlines):
    """
    reads headlines, lowercases letters, tokenizes into words, and removes stop words
    """
    tokens = []
    for line in headlines:
        toks = tokenizer.tokenize(line)
        toks = [t.lower() for t in toks if t.lower() not in stop_words]
        tokens.extend(toks)
    
    return tokens

# Calls function to get most common words in positive headlines

pos_lines = list(df[df.label == 1].headline)

pos_tokens = process_headlines(pos_lines)
pos_freq = nltk.FreqDist(pos_tokens)

print(f'positive words are: {pos_freq.most_common(20)}')

# Plot frequency distribution and examines pattern of words 

y_val = [x[1] for x in pos_freq.most_common()]

fig = plt.figure(figsize=(10,5))
plt.plot(y_val)

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Distribution (Positive)")
plt.show()

# # Log-log plot 

y_final = []
for i, k, z, t in zip(y_val[0::4], y_val[1::4], y_val[2::4], y_val[3::4]):
    y_final.append(math.log(i + k + z + t))

x_val = [math.log(i + 1) for i in range(len(y_final))]

fig = plt.figure(figsize=(10,5))

plt.xlabel("Words (Log)")
plt.ylabel("Frequency (Log)")
plt.title("Word Frequency Distribution (Positive)")
plt.plot(x_val, y_final)
plt.show()

# Negative words 

neg_lines = list(df2[df2.label == -1].headline)

neg_tokens = process_headlines(neg_lines)
neg_freq = nltk.FreqDist(neg_tokens)

print(f'negative words are: {neg_freq.most_common(20)}')

# Plots negative words 

y_val = [x[1] for x in neg_freq.most_common()]

fig = plt.figure(figsize=(10,5))
plt.plot(y_val)

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Distribution (Negative)")
plt.show()

# log-log plot 

y_final = []
for i, k, z in zip(y_val[0::3], y_val[1::3], y_val[2::3]):
    if i + k + z == 0:
        break
    y_final.append(math.log(i + k + z))

x_val = [math.log(i+1) for i in range(len(y_final))]

fig = plt.figure(figsize=(10,5))

plt.xlabel("Words (Log)")
plt.ylabel("Frequency (Log)")
plt.title("Word Frequency Distribution (Negative)")
plt.plot(x_val, y_final)
plt.show()

