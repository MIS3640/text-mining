# THE FOLLOWING CODE IS WHAT I USED TO GATHER DATA OF VARIOUS TYPES

# IN DEPTH DATA FOR SELECTED FILM
import imdb

# Need an internet connection to run
moviesDB = imdb.IMDb()

movies = moviesDB

movies = moviesDB.search_movie("The Shawshank Redemption")

# 1) Searching for a title of a movie (returns all movies under title given)
""" 
for movie in movies:
    title = movie["title"]
    year = movie["year"]
    print(f"{title} - {year}")
"""

# 2) Listing movie info

# below variables are used for #3 as well
id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie["title"]
year = movie["year"]
rating = movie["rating"]
directors = movie["directors"]
casting = movie["cast"]


print("MOVIE INFO")
# Prints title and year of movie
print(f"{title} - {year}")
# IMDB rating
print(f"rating: {rating}")

# Pulls direcotr of film
direcStr = " ".join(map(str, directors))
print(f"directors: {direcStr}")

# pulls actors in film
actors = ", ".join(map(str, casting))
print(f"actors: {actors}")


# 3) Actor info
# Pulls info on the primary actor listed
id = casting[0].getID()
person = moviesDB.get_person(id)
bio = moviesDB.get_person_biography(id)

name = person["name"]
birthDate = person["birth date"]
height = person["height"]
trivia = person["trivia"]
titleRefs = bio["titlesRefs"]

# actor name
print(f"name: {name}")
# actor birthday
print(f"birth date: {birthDate}")
# actor height
print(f"height: {height}")
# actor trivia
print(f"trivia: {trivia[0]}")

# pulls all movies actor stars in
titleRefsStr = ", ".join(map(str, titleRefs))
print(f"bio title refs: {titleRefsStr}")

# FOR MOVIE REVIEW
# This will print a review for the selected movie

from imdbpie import Imdb

imdb = Imdb()
# 1) input movie title
print(imdb.search_for_title("The Shawshank Redemption")[0])
# 2) imdb id
reviews = imdb.get_title_user_reviews("tt0111161")

# import pprint
# pprint.pprint(reviews)

print(reviews["reviews"][0]["author"]["displayName"])
print(reviews["reviews"][0]["reviewText"])

