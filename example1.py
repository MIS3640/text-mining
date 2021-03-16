# Get data
from imdbpie import Imdb
import pprint

imdb = Imdb()

# Get movie imdb-id

movie_name = [
    "Star Wars: Episode I - The Phantom Menace",
    "Star Wars: Episode II - Attack of the Clones",
    "Star Wars: Episode III - Revenge of the Sith",
]

# Get info from imdb (title, id, number of reviews, reviews text)
def get_info(movie_list):
    '''
    Retrieves movie title, movie ID, number of reviews, rating of the review, 
    and the review username for all the movies in the list.
    '''
    movie_sum = []
    for movie in movie_name:
        movie_info = {}
        movie_info["movie_title"] = movie
        movie_info["imdb_id"] = imdb.search_for_title(movie)[0]["imdb_id"]

        reviews = imdb.get_title_user_reviews(movie_info["imdb_id"])
        movie_info["number_of_reviews"] = len(reviews["reviews"])
        
        movie_info['review_info']=[]
        for i in range(5):
            # len(reviews["reviews"]) - 1
            each_r = {'username':reviews["reviews"][i]['author']['displayName'],
                    'imdb_rating':reviews['reviews'][i]['authorRating'],
                    'review_text': reviews['reviews'][i]['reviewText']
                    }
            movie_info['review_info'].append(each_r)

        movie_sum.append(movie_info)
    return movie_sum
    # pprint.pprint(movie_sum)


full_review_text = get_info(movie_name)
# print(imdb.search_for_title('Star Wars: Episode I - The Phantom Menace')[0])

'''The format of the new dictionary
{movie name: 'Star Wars: Episode IV - A New Hope',
movie_id: 'tt0076759',
number_of_reviews: __,
review_text:
    [{
    username: ___,
    review_text:___,
    user_rating: ___
    }]'''



# Pickling & save data to a file called review data
import pickle

with open('review_data.pickle','wb') as f:
    pickle.dump(full_review_text,f)
