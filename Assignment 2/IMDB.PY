#IMDB Movie Reviews

#Part 1: Harvesting text from the Internet
from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("The Dark Knight")[0])
reviews = imdb.get_title_user_reviews("tt0468569")

# import pprint
# pprint.pprint(reviews)

print(reviews['reviews'][0:149]['author']['displayName'])
# print(reviews['reviews'][0]['reviewText'])

#Clean Data
import re

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess_reviews(reviews):
    reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]
    
    return reviews

reviews_train_clean = preprocess_reviews(reviews_train)
reviews_test_clean = preprocess_reviews(reviews_test)