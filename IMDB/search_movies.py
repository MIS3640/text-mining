import imdb

# Need an internet connection to run
moviesDB = imdb.IMDb()

movies = moviesDB

movies = moviesDB.search_movie("Borat")

# 1) Searching for a title of a movie (returns all movies under title given)
""" `
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

titleRefsStr = ", ".join(map(str, titleRefs))
print(f"bio title refs: {titleRefsStr}")

