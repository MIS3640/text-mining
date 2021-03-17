### STEP 1
from imdbpie import Imdb
import pprint

imdb = Imdb()

### Get info from imdb (title, id, number of reviews, reviews text)

movie_name = [
    "Star Wars: Episode I - The Phantom Menace",
    "Star Wars: Episode II - Attack of the Clones",
    "Star Wars: Episode III - Revenge of the Sith",
    "Star Wars: Episode IV - A New Hope",
    "Star Wars: Episode V - The Empire Strikes Back",
    "Star Wars: Episode VI - Return of the Jedi",
    "Star Wars: Episode VII - The Force Awakens",
    "Star Wars: Episode VIII - The Last Jedi",
    "Star Wars: Episode IX - The Rise of Skywalker",
]


def get_info(movie_list):
    """
    Retrieves movie title, movie ID, number of reviews, rating of the review,
    and the review username for all the movies in the list.
    """
    movie_sum = []
    for movie in movie_name:
        movie_info = {}
        movie_info["movie_title"] = movie
        movie_info["imdb_id"] = imdb.search_for_title(movie)[0]["imdb_id"]

        reviews = imdb.get_title_user_reviews(movie_info["imdb_id"])
        movie_info["number_of_reviews"] = len(reviews["reviews"])

        movie_info["review_info"] = []
        for i in range(len(reviews["reviews"]) - 1):
            # to get all the reviews: len(reviews["reviews"]) - 1
            each_r = {
                "username": reviews["reviews"][i]["author"]["displayName"],
                "review_text": reviews["reviews"][i]["reviewText"],
            }
            try:
                each_r["imdb_rating"] = reviews["reviews"][i]["authorRating"]
            except KeyError:
                continue
            # print(reviews["reviews"][i]["authorRating"])
            movie_info["review_info"].append(each_r)

        movie_sum.append(movie_info)
    return movie_sum


full_review_text = get_info(movie_name)
# pprint.pprint(full_review_text)


### Pickling & save data to a file called review data
import pickle

with open("review_data.pickle", "wb") as f:
    pickle.dump(full_review_text, f)


"""The format of the new dictionary
{movie name: 'Star Wars: Episode IV - A New Hope',
movie_id: 'tt0076759',
number_of_reviews: __,
review_text:
    [{
    username: ___,
    review_text:___,
    user_rating: ___
    }]"""