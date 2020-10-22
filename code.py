pip install imdbpie
pip install wordcloud
pip install nltk

import numpy as np
import matplotlib.pyplot as plt 
import paas as pd 
from imdbpie import imdb 
import nltk
nltk.download ('stopwords')
nltk.download ('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def get_id(title):
    """TITLE: movie title to search 
    Returns information of movies containing ids
    """
    imdb = Imdb()
    return imdb.search_for_title(title)

def id_review(id):
    """ID: movie id
    Returns all reviews combined into one sentence
    """
    assert type(id) == str, 
    "ID must be string"
    imdb = Imdb()
    result = imdb.get_title_user_reviews(id) ['reviews']
    reviews = ''
    for r in result:
        reviews += " " + r.get('reviewText')
    return reviews

def remove_stop(id):
    """ID: movie id
    Returns sentence with stop words removed
    """
    imdb = Imdb()
    title = imdb.get_title(id) ['base']['title']
    t_words = word_tokenize(title)
    movie_sw = ["Movie", "film", "n't", " ", "people", "one"] + t_words
    movie_sw = [s.lower() for s in movie_sw]
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(id_review(id))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = ''
    for w in word_tokens:
        w = w.lower()
        if w not in stop_words and w not in string.punctuation and w not in movie_sw:
            filtered_sentence += w + " "
    return filtered_sentence

def make_cloud(id):
    """ID: movie id
    Draws word cloud of most frequent words in movie review
    """
    plt.subplots(figsize=(10,8))
    wordcloud = WordCloud(scale=2).generate(remove_stop(id))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("word_cloud.png")

#examples:

make_cloud('tt0120338')
print("Most Frequent Words in the Reviews of Titanic")

make_cloud('tt3043630')
print("Most Frequent Words in the Reviews of Tiny Times")

make_cloud('tt3371366')
print("Most Frequent Words in the Reviews of Transformers")
