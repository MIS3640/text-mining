# Get data
from imdbpie import Imdb
import pprint

imdb = Imdb()
print(imdb.search_for_title('Star Wars: Episode IV - A New Hope')[0])
reviews = imdb.get_title_user_reviews('tt0076759')['reviews']
review_text = {}
for r in reviews:
    rt = r['reviewText']
    auth = r['author']['displayName']
    review_text[auth] = rt

pprint.pprint(review_text)

# print(reviews['reviews'][0]['author']['displayName'])
# print(reviews['reviews'][0]['authorRating'])
# print(reviews['reviews'][0]['reviewText'])

# example_text = reviews['reviews'][0:3]


# Pickling 
import pickle

# save data to a file
with open('example_file.pickle','wb') as f:
    pickle.dump(review_text,f)

