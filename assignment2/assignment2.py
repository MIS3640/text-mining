from mediawiki import MediaWiki
import word_freq

# Data Source
wikipedia = MediaWiki()
print('Enter A Wiki Page:')
title_1 = input()
page_1 = wikipedia.page(title_1)


# Frequency of the Title in the Wiki Page
print(f'The Frequency of the Wiki Page title \'{title_1}\' is {word_freq.word_freq(page_1.content,title_1)}')

# Top 10 Most Frequent Words in the Wiki Page
print(f'Top 10 Most Frequent Words and its Frequency in Wiki page \'{page_1.title}\' are:')
word_freq.top_10_most_freq(word_freq.clean(page_1.content))


# Naturalization
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

score_1 = SentimentIntensityAnalyzer().polarity_scores(page_1.content) # AI Emotions
print(score_1)

neu_1 = score_1.get('neu')

def is_neutral(neu):
    """
    Identify if the inputed neutrality measurement is greater or equal to .80
    """
    if neu >= 0.80:
        return True
    else:
        return False

if is_neutral(neu_1) is True:
    print(f'The {page_1.title} Wikipedia Page is Neutral')
else:
    print(f'The {page_1.title} Wikipedia Page is not Neutral')


# Similar Pairs
# Compare Different Data
print(f'Enter a Wiki Page you want to compare {page_1.title} Page with:')
title_2 = input()
page_2 = wikipedia.page(title_2)

# Frequency of the Title in the Wiki Page
print(f'The Frequency of the Wiki Page title \'{title_2}\' is {word_freq.word_freq(page_2.content,title_1)}')

# Top 10 Most Frequent Words in the Wiki Page
print(f'Top 10 Most Frequent Words and its Frequency in Wiki page \'{page_2.title}\' are:')
word_freq.top_10_most_freq(word_freq.clean(page_2.content))

score_2 = SentimentIntensityAnalyzer().polarity_scores(page_2.content) # AI Emotions
print(score_2)

neu_2 = score_2.get('neu')

if is_neutral(neu_2) is True:
    print(f'The {page_2.title} Wikipedia Page is Neutral')
else:
    print(f'The {page_2.title} Wikipedia Page is not Neutral')

clean_1 = word_freq.clean(page_1.content)
clean_2 = word_freq.clean(page_2.content)

common_pairs = dict()
for key in clean_1:
    if (key in clean_2 and clean_1[key] == clean_2[key]):
        common_pairs[key] = clean_1[key]
print(common_pairs)