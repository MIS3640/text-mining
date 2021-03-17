from imdbpie import Imdb

imdb = Imdb()

# print(imdb.search_for_title("The Dark Knight"))
# reviews = imdb.get_title_user_reviews("tt0468569")

# import pprint
# pprint.pprint(reviews)

# print(reviews['reviews'][0]['author']['displayName'])
# print(reviews['reviews'][0]['reviewText'])

def get_imdb_reviews(movie_title):
    """
    Function that returns all the reviews for a given movie title
    """
    movie = imdb.search_for_title(movie_title)[0]
    imdb_id = movie['imdb_id']
    reviews = imdb.get_title_user_reviews(imdb_id)
    return reviews

# print(get_imdb_reviews("Parasite"))

def get_review_text(reviews, review_number):
    """
    Function that returns a random review from the first 20 reviews of a movie
    """
    import random
    # random_number = random.randint(1, 20)
    # review_text = reviews['reviews'][random_number]['reviewText']
    review_text = reviews['reviews'][review_number]['reviewText']
    return review_text


def histogram(s):
    """
    Returns count of each item in s
    s = a string or a list
    """
    import string
    d = dict()
    clean_review = []
    # print(clean_review)
    for word in s.split():
        # print(word)
        word = word.strip(string.punctuation)
        word = word.lower()
        # print(word)
        clean_review.append(word)

    for cl_word in clean_review:
        number_of_c = d.get(cl_word, 0)
        number_of_c += 1
        d[cl_word] = number_of_c
        # print(d)
    return d


def sorted_hist(hist):
    """Sorts a word frequency dictionary"""
    lst=[]
    for key, values in hist.items():
        t = (values, key)
        lst.append(t)
    sort_lst = sorted(lst, reverse=True)
    return sort_lst


from scipy import spatial

# print(help(scipy))
reviews = get_imdb_reviews("Parasite")
corpus = []
review1 = get_review_text(reviews, 0)
review2 = get_review_text(reviews, 1)

spatial.distance.cosine(review1, review2)


def main():
    reviews = get_imdb_reviews("Parasite")
    # print(reviews)
    # review_text = get_review_text(reviews, 0)
    # print(review_text)
    # print(type(review_text))
    # hist = (histogram(review_text))
    # print(hist)
    # print(sorted_hist(hist))





if __name__ == '__main__':
    main()