from imdbpie import Imdb
import pickle


def review_extracter(movie):
    """input movie name, outputs txt file with reviews on the front page of imdb"""
    ### extracts content from movie page ###
    imdb = Imdb()
    url = imdb.search_for_title(movie)[0]
    reviews = imdb.get_title_user_reviews(url["imdb_id"])
    ### creates list of all reviews present on the front page###
    imdb = Imdb()
    url = imdb.search_for_title(movie)[0]
    reviews = imdb.get_title_user_reviews(url["imdb_id"])
    ### creates txt file for all reviews present on the front page###
    review_list = []
    for i in range(len(reviews["reviews"])):
        line = reviews["reviews"][i]["reviewText"]
        review_list.append(line)
    ###pickles list###
    with open(f"{movie}_imdb.pickle", "wb") as f:
        pickle.dump(review_list, f)
    # with open(f"{movie}.pickle", "rb") as input_file:
    #     copy = pickle.load(input_file)
    # print(copy)
def main():
    review_extracter("Mulan")
if __name__ == "__main__":
    main()