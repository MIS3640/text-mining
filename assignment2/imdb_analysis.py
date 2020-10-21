### IMDB Review Text Analysis , Code developed by Prim Prasitanond ###

# PART 1: Data Importation and Cleaning

# Importing Text - Find Movies and Generate Movies IDs
from imdbpie import Imdb
import pprint
imdb = Imdb()
def find_imdb():
    """
    This function will return a dictionary with movie title as key and the movie IDs as value, based on the user's input. 
    If the user does not have any more movies to add and wish to continue, press enter to run the function.
    
    Note that the function will only grab the first top search, for accuracy, please type in the movie title
    as accurately as possible.
    """
    moviesId = {}

    while True:
        movieTitle = input("What movie would you like to get see the review? Press enter to continue...")
        if movieTitle == '':
            break

        #grabbing first top search
        movie_result  = imdb.search_for_title(movieTitle)[0]
        print(movie_result)

        imdbId = imdb.search_for_title(movieTitle)[0]['imdb_id']
        moviesId[movieTitle] =  imdbId

    return moviesId

# IMDB Reviews
def get_user_review(moviesId):
    """ This function will return the IMDB reviews based on the movies from user's input.
    
    The output of this function is a dictionary with title of the movie as keys and the reviews 
    as values

    moviesId: the dictionary of IDs, output of the function find_imdb()
    
    """
    movie_reviews = {}

    for title ,id in moviesId.items():
        text_review = [] #initialize the list for every title
        reviews = imdb.get_title_user_reviews(id)

        text_review = [review['reviewText'] for review in reviews['reviews']] 
    
        movie_reviews[title] = text_review
    
    return movie_reviews

# IMDB Ratings
def get_imdb_ratings(moviesId):
    """ 
    This function will return a dicitionary of IMDB ratings of the movies based on the user's input. 
    The key of the dictionary is the movie title and the value is the rating.

    moviesId: the dictionary of movie IDs, output of the find_imdb() function
    """
    movie_ratings = {}

    for title ,id in moviesId.items():
        ratings = imdb.get_title_ratings(id)
        total_ratings = ratings['rating']

        movie_ratings[title] = total_ratings
    
    return movie_ratings

# Pre-Processing: Clean Punctuations from Reviews
import string
def clean_text(reviews):
    """This function will return a dictionary with movie title as keys 
    and string of cleaned reviews (without punctuations) as values.

    reviews: dictionary with movie title as keys and user reviews as values, output of 'get_user_review(moviesId)' function
    """
    punctuations = string.punctuation

    cleaned_reviews = {}

    for title, review in reviews.items():
        no_punc = ""
        for i in review:
            for char in i:
                if char not in punctuations:
                    no_punc += char

                cleaned_reviews[title] = no_punc

    return cleaned_reviews

# Pre-Processing: Remove Stopwords from Reviews
from nltk.corpus import stopwords
def remove_stopwords(no_punc_text):
    """
    This function will remove any stopwords, or words that have no meaning by itself (ex. the, in, on,etc). 
    The function will return a dictionary with movie title as the key and list of words in user reviews (without stopwords) as values.
    
    no_punc_text : a dictionary with movie title as keys and string of reviews as values, output of the 'clean_text(reviews)' function.
    """
    stop_words = list(stopwords.words('english'))
    processed_text = {}

    for title, review in no_punc_text.items():
        no_stopwords_text = []
        for word in review.split():
            word =  word.lower()
            if word not in stop_words:
                no_stopwords_text.append(word)
               
            processed_text[title] = no_stopwords_text 

    return processed_text
    
# PART 2: Analyzing your text

# Word Frequency
def word_freq(processed_text):
    """This function will return a nested dictionary with title of the movie as the key and dict of word frequency as the value.
    
   processed_text: a dict with movie title as key, and list of words as values
    """
    word_freq = {}

    for title, words in processed_text.items():
        freq = {} #initialize dict for every title
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
                
        word_freq[title] = freq
    
    return word_freq

# Most common words - descending order
def most_common(word_freq_dict):
    """
    This function returns a sorted dictionary of word frequency (in descending order).

    word_freq_dict: a nested dictionary with title of the movie as key, and dictionary of word and freq as value
    """
    common_words_dict = {}
    for title, words in word_freq_dict.items():
        common_words = [] # initialize the list for every title
        for word, freq in words.items():
            common_words.append((freq, word))

        common_words.sort(reverse=True) # sort once for each title
        common_words_dict[title] = common_words
    return common_words_dict

# Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def sentiment_analysis(processed_text):
    """
    This function will conduct sentimnet analysis on the user's reviews.
    The function will return dictionary of the positive sentiment score of each movie, based on the user's input.
    The score is divided into 4 main sections: neg - negative, neu - neutral, pos - positive, and compound.

    processed_text: a dict with movie title as key, and list of words as values
    """
    sentiment_score = {}

    for title, word in processed_text.items():
        score = []
        sentence = " ".join(word) #joined list of words into sentence for the sentiment analysis
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        print(score)

        #grab only positive score
        pos_score = score['pos']
        sentiment_score[title] = pos_score

    return sentiment_score

# Relationship Graph between ratings and sentiment score
import numpy as np
import matplotlib.pyplot as plt
def plot_graph (ratings, sentiment_score):
    """
    Tbis function returns a scatterplot between ratings and positivesentiment score to show whether
    there is a relationship between the two variables.

    ratings: a dictionary of movie ratings with movie title as key and rating as values, output of get_user_review(moviesId) function.
    sentiment_score: a dictionary of positive sentiment score with movie title as key and score as values, output of sentiment_analysis(processed_text) function.
    """
    #converint dictionary values to list because 'dict_values' object is not subscriptable 
    x = list(ratings.values())
    y = list(sentiment_score.values())
    n = list(ratings.keys())

    #plot graph
    plt.scatter(x, y, color='darkgreen')
    
    #label each point on the graph
    for i, txt in enumerate(n):
        plt.annotate(txt, (x[i], y[i]))

    #best fit line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")  

    #set and label axises
    plt.ylim(0, 0.40)
    plt.xlim(0,10)
    plt.title("The relationship between the IMDB Ratings and Positive Sentiment Score from User's Review")
    plt.xlabel("IMDB Ratings")
    plt.ylabel("Positive Sentiment Score")

    #show the graph
    plt.show()

def main():
    ###   PART 1   ###
    # create a dictionary of movie IDs
    moviesId = find_imdb()
    # print(moviesId)

    # get movie user reviews 
    reviews = get_user_review(moviesId)
    # print(reviews)

    # get movie ratings
    ratings = get_imdb_ratings(moviesId)
    # print(ratings)

    #pre-processing - remove punctuations and stopwords
    no_punc_text = clean_text(reviews)
    # pprint.pprint(no_punc_text)

    processed_text = remove_stopwords(no_punc_text)
    # print(processed_text)

    ###   PART 2   ###  
    # word frequency    
    word_freq_dict = word_freq(processed_text)
    # print(word_freq_dict)
    
    # most common words 
    most_common_word = most_common(word_freq_dict)
    # print(most_common_word)

    # sentiment analysis
    sentiment_score = sentiment_analysis(processed_text)
    print(sentiment_score)
    
    # scatterplot
    plot_graph(ratings, sentiment_score)

if __name__ == '__main__':
    main()