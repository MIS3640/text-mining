
from imdbpie import Imdb

imdb = Imdb()
parasite = (imdb.search_for_title("Parasite")[0])
reviews = imdb.get_title_user_reviews("tt6751668")

joker = (imdb.search_for_title("Joker")[0])
review2 = imdb.get_title_user_reviews("tt7286456")


unplanned = (imdb.search_for_title("Unplanned")[0])
review3 = imdb.get_title_user_reviews("tt9024106")

thegodfather = (imdb.search_for_title("The Godfather")[0])
reviews3 = imdb.get_title_user_reviews("tt0068646")

disastermovie = (imdb.search_for_title("Disaster Movie")[0])
reviews2 = imdb.get_title_user_reviews("tt1213644")


import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def printreviews(reviews):
    """
    print all and only the reviews of movies
    """
    p = []
    for n in reviews['reviews']:
        p.append(n['reviewText'])
    return p

parasitereviews = printreviews(reviews)
jokerreviews2 = printreviews(review2)
unplannedreviews2 = printreviews(review3)
godfather2 = printreviews(reviews3)
DisasterMovie2 = printreviews(reviews2)
print(parasitereviews)

def scorepersentence(reviews):
    """
    Polarity Scores on each reviews within the movie.
    """
    vs = []
    for sentence in reviews:
        vs.append(analyzer.polarity_scores(sentence))
    return vs
        

parasitereviewsscore = scorepersentence(parasitereviews)
print(parasitereviewsscore)

jokerreviewsscore = scorepersentence(jokerreviews2)
print(jokerreviewsscore)
unplannedreviewsscore = scorepersentence(unplannedreviews2)
godfatherscore = scorepersentence(godfather2)
DisasterMoviescore = scorepersentence(DisasterMovie2)



def negvalenceavg (score):
    """
    Total negative valence measured by averaging all the negative valence in the reviews.
    """
    ng = []
    for n in score:
        ng.append(n['neg'])
    return sum(ng) / len (ng)


def posvalenceavg (score):
    """
    Total positive valence measured by averaging all the postive valence in the reviews.
    """
    ps = []
    for n in score:
        ps.append(n['pos'])
    return sum(ps) / len (ps)

def neuvalenceavg (score):
    """
    Total neutral valence measured by averaging all the neutral valence in the reviews.
    """
    neu = []
    for n in score:
        neu.append(n['neu'])
    return sum(neu) / len (neu)

def cpndavg(score):
    """
    Total compound valence measured by averaging all the compound valence in the reviews.
    """
    cpnd = []
    for n in score:
        cpnd.append(n['compound'])
    return sum(cpnd) / len (cpnd)

def finalscore(score):
    """
    Layout all the scores in sentence. 
    """
    print(f"The Positive Valence for this movie is {posvalenceavg(score)}")
    print(f"The Negative Valence for this movie is {negvalenceavg(score)}")
    print(f"The Neutral Valence for this movie is {neuvalenceavg(score)}")
    print(f"The Compoud for this movie is {cpndavg(score)}")


print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {parasite['title']} | Year: {parasite['year']} ")
print()
finalscore(parasitereviewsscore)
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {joker['title']} | Year: {joker['year']} ")
print()
finalscore(jokerreviewsscore)
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {unplanned['title']} | Year: {unplanned['year']} ")
print()
finalscore(unplannedreviewsscore)
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {thegodfather['title']} | Year: {thegodfather['year']} ")
print()
finalscore(godfatherscore)
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print(f"Movie Title: {disastermovie['title']} | Year: {disastermovie['year']} ")
print()
finalscore(DisasterMoviescore)
print()
print("---------------------------------------------------------------------------------------------------------------------------")
print()
print()