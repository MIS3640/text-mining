import praw
import pickle
import csv

def stock_list():
    '''opens csv file and creates a list with all of the stock tickers in the US'''
    with open('stock.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        lst = []
        for row in reader:
            lst.append(row['ticker'])
    return lst


def import_subreddit():
    '''imports the top 1000 post titles under wallstreetbets subreddit'''
    reddit = praw.Reddit(client_id = 'UV_0pi49dIB77w', client_secret = 'xrAIGSNfOco13rjEJii23FB7EDPJBQ', username = 'verkxies1', password = 'problemsolvingandsoftwaredesign', user_agent = 'verkxies1')
    sub = 'wallstreetbets'
    submissions = reddit.subreddit(sub).top('day', limit = 50)
    top = [(submission.title) for submission in submissions]
    return top

def word_parse():
    '''a list of titles with a sublist that parses each word in the title into a list''' 
    lst = []
    for title in import_subreddit():
        lst.append(title.split())
    return(lst)

def ticker_check(word):
    '''This function checks if the word is a stock ticker'''
    if word.replace('$', '') in stock_list():
        return True
    return False

def ticker_one(title):
    '''This function creates a dictionary of all stock tickers that appear in a title, assigning a value of 1 to each'''
    d = {}
    for word in title:
        if ticker_check(word):
            d[word.replace('$', '')] = 1
    return d

def ticker_count():
    '''Counts all the posts where a ticker is mentioned and stores it in a dictionary with the ticker as the key'''
    d = {}
    for title in word_parse():
        for key in ticker_one(title):
            if key in d:
                d[key] = ticker_one(title)[key] + d[key]
            else:
                d[key] = ticker_one(title)[key]
    return d
        


def main():
    # data = import_subreddit()
    # title_test = ['$gme', 'gme', 'gme', 'at', '330', 'to', 'rob', 'lox', 'and', 'never', 'felt', 'more', 'smarter.', '#robloxnextgme']
    # print(stock_list())
    # print(data)
    # print(word_parse()[-1])
    # print(ticker_check('GME'))
    # print(ticker_one(title_test))
    print(ticker_count())


if __name__ == "__main__":
    main()

