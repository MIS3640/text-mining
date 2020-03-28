def printreviews(reviews):
    p = []
    i = 0
    while i < 10
        for n in reviews['reviews']:
            p.append(random.choice(n['reviewText']))
        return p


from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("Parasite")[0])
reviews = imdb.get_title_user_reviews("tt6751668")

parasitereviews = printreviews(reviews)
parasitereviews = ",".join(parasitereviews)
print(parasitereviews)