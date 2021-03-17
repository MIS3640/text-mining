from imdbpie import Imdb

imdb = Imdb()

# print(imdb.search_for_title("The Dark Knight"))
# reviews = imdb.get_title_user_reviews("tt0468569")

# import pprint
# pprint.pprint(reviews)

# print(reviews['reviews'][0]['author']['displayName'])
# print(reviews['reviews'][0]['reviewText'])


def get_imdb_reviews(movie_title):
    """
    Function that returns all the reviews for a given movie title
    """
    movie = imdb.search_for_title(movie_title)[0]
    imdb_id = movie["imdb_id"]
    reviews = imdb.get_title_user_reviews(imdb_id)
    return reviews


# print(get_imdb_reviews("Parasite"))


def get_review_text(reviews, review_number=0, rand=True):
    """
    Function that returns a random review from the first 20 reviews of a movie
    """
    import random

    random_number = random.randint(1, 20)

    if rand == True:
        review_text = reviews["reviews"][random_number]["reviewText"]
    else:
        review_text = reviews["reviews"][review_number]["reviewText"]
    return review_text

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(review_text):
    """ 
    Function that returns a tiple contianing the review text and the sentiment analysis score it recieved
    """
    score = SentimentIntensityAnalyzer().polarity_scores(review_text)
    return review_text, score

def lexical_diversity(review_text):
    return len(set(review_text)) / len(review_text)


def histogram(s):
    """
    Returns count of each item in s
    s = a string or a list
    """
    import string

    d = dict()
    clean_review = []
    # print(clean_review)
    for word in s.split():
        # print(word)
        word = word.strip(string.punctuation)
        word = word.lower()
        # print(word)
        clean_review.append(word)

    for cl_word in clean_review:
        number_of_c = d.get(cl_word, 0)
        number_of_c += 1
        d[cl_word] = number_of_c
        # print(d)
    return d


def sorted_hist(hist, exclude_stopwords=True):
    """Sorts a word frequency dictionary from greatest to smallest frequency
    hist : dictionary with word frequency"""


    lst = []
    stopwords = open("stopword.txt", encoding="UTF8")
    # print(stopwords)
    hist_int = hist.copy()
    lst_st_words = []
    for line in stopwords:
        lst_st_words.append(line.strip())
    # print(lst_st_words)
    if exclude_stopwords == True:
        for word in hist:
            if word in lst_st_words:
                hist_int.pop(word)
    # return hist_int
    for key, values in hist_int.items():
        t = (values, key)
        lst.append(t)
    sort_lst = sorted(lst, reverse=True)
    return sort_lst


def main():
    reviews = get_imdb_reviews("Parasite")
    # print(reviews)
    review_text = get_review_text(reviews)
    # print(review_text)
    sentiment = sentiment_analysis(review_text)
    # print(sentiment)
    lexical_div = lexical_diversity(review_text)
    print(lexical_div)
    review_text = get_review_text(reviews, 0, rand=False)
    # print(review_text)
    # print(type(review_text))
    hist = histogram(review_text)
    # print(hist)
    import pprint
    pprint.pprint(sorted_hist(hist))


if __name__ == "__main__":
    main()