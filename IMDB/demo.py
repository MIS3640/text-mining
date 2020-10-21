from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("The Dark Knight")[0])
reviews = imdb.get_title_user_reviews("tt0468569")

# import pprint
# pprint.pprint(reviews)

print(reviews['reviews'][0]['author']['displayName'])
print(reviews['reviews'][0]['reviewText'])