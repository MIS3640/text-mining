from imdbpie import Imdb
import pprint
import re

imdb = Imdb()
print(imdb.search_for_title("The Fault In Our Stars")[0])
reviews = imdb.get_title_user_reviews("tt2582846")

# import pprint
# pprint.pprint(reviews) #prints all the 669 reviews

print(reviews['reviews'][2]['author']['displayName'])
mystr = print(reviews['reviews'][2]['reviewText'])

# movieName = "The Fault In Our Stars"
# imdb = Imdb() 
# movieDict =  imdb.search_for_title(movieName)[0] # closest match is the first index
# id = movieDict['imdb_id']
# reviews = imdb.get_title_user_reviews(id)

# pprint.pprint(reviews['reviews'][0]) # heavy printing 
# allReviews = reviews['reviews'] # get the reviews into a dictionary
