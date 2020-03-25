import requests
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def text_mine(subreddit, size, after, before):
    '''
    subreddit: string
    size: int
    after, before: int (epoch time)

    return dataframe with size rows consiting of highest score submissions submmitted between after and before in subreddit 
    '''
    url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size={size}&fields=title&sort=desc&sort_type=score&after={after}&before={before}'
    response = requests.get(url).json().get('data')

    text_list = []
    for submission in response:
        text_list.append(submission['title'])
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


def nl_score(df):
    '''
    df: datafarame

    return average sentiment score of dataframe
    '''
    # nltk.download('vader_lexicon')
    df['score'] = df['title'].apply(lambda x: SentimentIntensityAnalyzer().polarity_scores(x))

    total = {'neg':0, 'neu':0, 'pos':0, 'compound':0}
    for key in total:
        for index, row in df.iterrows():
            total[key] += row['score'][key]
        total[key] = total[key]/len(df.index)

    return(total)


def daily_count(subreddit, after, end):
    '''
    subreddit: string
    after, end: int (epoch time)

    return dataframe consisting of number of submissions in subreddit per day between after and end
    '''
    url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size=0&after={after}&before={end}&aggs=created_utc&frequency=day'
    response = requests.get(url).json().get('aggs').get('created_utc')

    df = pd.DataFrame(columns=['count'])
    for date in response:
        df = df.append({'count': date['doc_count']},ignore_index=True)

    return df


def daily_score(subreddit, size, after, before, end):
    '''
    subreddit: string
    size: int
    after, before, end: int (epoch time)

    return dataframe consisintg of average sentiment scores of top size submissions in subreddit per day between after and end
    '''
    index = 0
    df = pd.DataFrame(columns=['date', 'neg', 'neu', 'pos', 'compound'])

    while after <= end:
        score = nl_score(text_clean(text_mine(subreddit, size, after, before)))

        df = df.append({'date': dt.datetime.fromtimestamp(after).strftime('%Y-%m-%d'),
                        'neg': score['neg'], 
                        'neu': score['neu'], 
                        'pos': score['pos'], 
                        'compound': score['compound']
                        },ignore_index=True)

        index += 1
        after += 86400
        before += 86400

    return df


def daily_df(subreddit, size, s_y, s_m, s_d, e_y, e_m, e_d):
    '''
    subreddit: string
    size: int
    s_y, s_m, s_d, e_y, e_m, e_d: int (dates)

    return dataframe consisting of average sentiment scores and number of submission per day between s_y, s_m, s_d (%Y, %m, %d), and e_y, e_m, e_d (%Y, %m, %d)
    '''
    after = int(dt.datetime(s_y, s_m, s_d).timestamp())
    before = after + 86399
    end = int(dt.datetime(e_y, e_m, e_d).timestamp())

    df_1 = daily_score(subreddit, size, after, before, end)
    df_2 = daily_count(subreddit, after, end)
    df = df_1.join(df_2)

    return df


def main():
    # dates earlier than 2020, 1, 21 will result in error because there are no submissions
    # corona = daily_df('Coronavirus', 10, 2020, 1, 21, 2020, 3, 21)
    # print(corona)
    # corona.to_pickle("./corona.pkl")
    corona = pd.read_pickle('./corona.pkl')

    corona.plot(kind='line',x='date',y='count',ax=plt.gca())
    plt.show()

    corona.plot(kind='line',x='date',y='compound',ax=plt.gca())
    plt.show()  
    

if __name__ == "__main__":
    main()