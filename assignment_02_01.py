import praw

import pandas as pd

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def text_mine(reddit, subreddit, n):
    '''
    reddit: praw.reddit.Reddit object
    subreddit: string 
    n: integer

    return dataframe with n rows consisting of hot posts form subreddit
    '''
    text_list = []
    for submission in reddit.subreddit(subreddit).hot(limit=n):
        text_list.append(submission.title)
    df = pd.DataFrame(text_list, columns=['title'])
    return df


def text_clean(df):
    '''
    df: dataframe

    return dataframe that is cleaned by performing tokenization, lemmatization, and removal of stopwords
    '''
    # nltk.download('stopwords')
    # nltk.download('wordnet')
    df['title'] = df['title'].apply(lambda x: RegexpTokenizer(r'\w+').tokenize(x.lower()))
    df['title'] = df['title'].apply(lambda x: [word for word in x if word not in stopwords.words('english')])
    df['title'] = df['title'].apply(lambda x: ' '.join(WordNetLemmatizer().lemmatize(word) for word in x))
    return df


def most_frequent(df, n):
    '''
    df: dataframe
    n: integer

    prints n words with highest frequency in dataframe
    '''
    word_list = df.values.sum().split()

    frequency = dict()
    for word in word_list:
        frequency[word] = frequency.get(word, 0) + 1

    print('most frequently used words are:')
    index = 0
    for word in sorted(frequency, key=frequency.get, reverse=True):
        index += 1
        print(word, frequency[word])
        if index == n:
            break
    
    
def nl_score(df):
    '''
    df: datafarame

    prints average sentiment score of dataframe
    '''
    # nltk.download('vader_lexicon')
    df['score'] = df['title'].apply(lambda x: SentimentIntensityAnalyzer().polarity_scores(x))

    total = {'neg':0, 'neu':0, 'pos':0, 'compound':0}
    for key in total:
        for index, row in df.iterrows():
            total[key] += row['score'][key]
        total[key] = total[key]/len(df.index)

    print()
    print('average sentiment scores are:')
    print(total)


def main():
    reddit = praw.Reddit(
        client_id='client id',
        client_secret='client secret',
        username='username',
        password='password',
        user_agent='user agent')

    # r/all
    all = text_mine(reddit, 'all', 1000)
    all = text_clean(all)
    most_frequent(all, 10)
    nl_score(all)

    # r/Coronavirus
    corona = text_mine(reddit, 'Coronavirus', 1000)
    corona = text_clean(corona)
    most_frequent(corona, 10)
    nl_score(corona)


if __name__ == "__main__":
    main()
