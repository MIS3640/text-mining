import praw
import csv
import numpy as np
import matplotlib.pyplot as plt


def stock_list():
    """opens csv file and creates a list with all of the stock tickers in the US"""
    with open("stock.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        lst = []
        for row in reader:
            lst.append(row["ticker"])
    return lst


def import_subreddit():
    """
    imports the top 100 post titles for the day under wallstreetbets subreddit
    """
    reddit = praw.Reddit(
        client_id="UV_0pi49dIB77w",
        client_secret="xrAIGSNfOco13rjEJii23FB7EDPJBQ",
        username="verkxies1",
        password="problemsolvingandsoftwaredesign",
        user_agent="verkxies1",
    )
    sub = "wallstreetbets"
    submissions = reddit.subreddit(sub).top("day", limit=100)
    top = [(submission.title) for submission in submissions]
    return top


def word_parse():
    """a list of titles with a sublist that parses each word in the title into a list"""
    lst = []
    for title in import_subreddit():
        lst.append(title.split())
    return lst


def ticker_check(word):
    """
    This function checks if the word is a stock ticker

    word: input a word
    return: Boolean
    """
    if word.replace("$", "") in stock_list():
        return True
    return False


def ticker_one(title):
    """
    This function creates a dictionary of all stock tickers that appear in a title, assigning a value of 1 to each

    title: input a title
    return: a dictionary with all stock tickers that appear in the title"""
    d = {}
    for word in title:
        if ticker_check(word):
            d[word.replace("$", "")] = 1
    return d


def ticker_count():
    """Counts all the posts where a ticker is mentioned and stores it in a dictionary with the ticker as the key"""
    d = {}
    for title in word_parse():
        for key in ticker_one(title):
            if key in d:
                d[key] = ticker_one(title)[key] + d[key]
            else:
                d[key] = ticker_one(title)[key]
    # Remove a few common words as tickers, as more often than not these words are not refering to the stock
    if "I" in d:
        del d["I"]
    if "A" in d:
        del d["A"]
    if "FOR" in d:
        del d["FOR"]
    if "CEO" in d:
        del d["CEO"]
    if "YOLO" in d:
        del d["YOLO"]
    return d


def sorted_ticker_count():
    """sorts the ticker frequency from highest to lowest"""
    d = ticker_count()
    a = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return a


def ticker():
    """returns index 0 or the first value in the tuple pair from
    sorted_ticker_count() output"""
    tuple_list = sorted_ticker_count()

    first_tuple_elements = [a_tuple[0] for a_tuple in tuple_list]
    return first_tuple_elements


def count():
    """returns index 1 or the second value in the tuple pair from
    sorted_ticker_count() output"""
    tuple_list = sorted_ticker_count()

    second_tuple_elements = [a_tuple[1] for a_tuple in tuple_list]
    return second_tuple_elements


def barChart():
    """creates a bar chart from the outputs of ticker() which will
    be the x-axis lables and count() which will be the y-axis labels"""
    objects = ticker()
    y_pos = np.arange(len(objects))
    performance = count()
    plt.bar(y_pos, performance, align="center", alpha=0.5)
    plt.xticks(y_pos, objects, rotation=90)
    plt.ylabel("Count")
    plt.title("Bar Chart of Tickers and Their Count")
    plt.show()


def main():
    # data = import_subreddit()
    # title_test = ['$gme', 'gme', 'gme', 'at', '330', 'to', 'rob', 'lox', 'and', 'never', 'felt', 'more', 'smarter.', '#robloxnextgme']
    # print(stock_list())
    # print(data)
    # print(word_parse()[-1])
    # print(ticker_check('GME'))
    # print(ticker_one(title_test))
    # print(ticker_count())
    print(sorted_ticker_count())
    # result = sorted_ticker_count()
    # print(ticker())
    # print(count())
    print(barChart())
    # print(result)


if __name__ == "__main__":
    main()
