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
