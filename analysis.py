import imdbmini
import matplotlib.pyplot as plt
import operator
import collections
from imdbpie import Imdb
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vader_lexicon')

def barchart(topic, limit):
    """
    Accepts a topic as a list, or in this case a call to the imdbmini API.
    Displays the frequency of records (i.e. directors/stars) in the list in a bar chart
    Limits the plot based to the nu,ber of records specified by the user in 'limit'
    """
    d = dict()
    subjects = topic
    for subject in subjects:
        if subject not in d:
            d[subject] = 1
        else:
            d[subject] += 1
    sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    sorted_d = dict(collections.Counter(sorted_d).most_common(limit))
    plt.bar(sorted_d.keys(), sorted_d.values())
    plt.show()

def hist(list):
    """
    Accepts a list and returns a histogram of the freqeuncies at each point.
    """
    plt.hist(list)
    plt.show()

def average_reviewscore(title):
    """
    Accepts a movie title from user as a string.
    Calls the imdbpie API and iterates through each user review left for the specified title.
    Uses sentiment analysis and prints the average compound score of all reviews left for the particular title.
    """
    imdb = Imdb()
    id = imdb.search_for_title(title)[0]['imdb_id']
    reviews = imdb.get_title_user_reviews(id)
    numberofreviews = len(reviews['reviews'])
    compound_scores = []
    for i in range(numberofreviews):
        review = reviews['reviews'][i]['reviewText']
        score = SentimentIntensityAnalyzer().polarity_scores(review)
        compound_scores.append(score['compound'])
    numerator = 0
    denominator = len(compound_scores)
    for i in range(denominator):
        numerator += compound_scores[i]
    average = numerator / denominator
    print(average)

def top_titles(limit):
    titles = imdbmini.get_titles()
    for i in range(0, limit):
        print(f'{i + 1}: {titles[i]}')



def main():
    barchart(imdbmini.get_directors(), 10)
    barchart(imdbmini.get_stars(), 10)
    hist(imdbmini.get_runtimes())
    top_titles(10)
    average_reviewscore('The Shawshank Redemption')
    average_reviewscore('Cats')

if __name__ == "__main__":
    main()