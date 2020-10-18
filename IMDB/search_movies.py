import imdb

# Need an internet connection to run
moviesDB = imdb.IMDb()

movies = moviesDB

movies = moviesDB.search_movie("The Shawshank Redemption")

# 1) Searching for a title of a movie (returns all under title)
""" `
for movie in movies:
    title = movie["title"]
    year = movie["year"]
    print(f"{title} - {year}")
"""

# 2) Listing movie info

id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie["title"]
year = movie["year"]
rating = movie["rating"]
directors = movie["directors"]
casting = movie["cast"]

print("movie info")
print(f"{title} - {year}")
print(f"rating: {rating}")

direcStr = " ".join(map(str, directors))
print(f"directors: {direcStr}")

actors = ", ".join(map(str, casting))
print(f"actors: {actors}")


# 3) Actor info - needs debugging
"""
id = casting[0].getID()
person = moviesDB.get_person(id)
bio = moviesDB.get_person_biography(id)

name = person["name"]
birthDate = person["birth date"]
height = person["height"]
trivia = person["trivia"]
titleRefs = bio["titlesRefs"]

print(f"name: {name}")
print(f"birth date: {birthDate}")
print(f"height: {height}")
print(f"trivia: {trivia[0]}")

titleRefsStr = ", ".join(map(str, titleRefs))
print(f"bio title refs: {titleRefsStr}")
"""
