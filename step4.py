import pickle
import pprint
with open('sent_data.pickle','rb') as data_input:
    sent_text = pickle.load(data_input)

# print(sent_text)

# Make a list for each graph
# sent vs. rating
def sent_rate():
    rating_list = []
    for movie in sent_text:
        for sub_list in movie['review_info']:
            imdb_r = sub_list['imdb_rating']
            sent_r = sub_list['sentiment_score']['compound']
            user = sub_list['username']
            sub_list_r = {'username':[imdb_r, sent_r]}
            rating_list.append(sub_list_r)
    return rating_list

pprint.pprint(sent_rate())



# average sentiment 
def avg_sent(): 
    """ Gets the average of sentiment scocres for each movie
    and then returns it in a dictionary"""
    movie_sentiment = {}
    for movie in sent_text: 
        sent_list = []
        for sub_list in movie['review_info']:
            sent_score = sub_list['sentiment_score']['compound']
            sent_list.append(sent_score)
        movie_sentiment[movie['movie_title']] =  sent_list
    # print(movie_sentiment)

    avg_sent = {}
    for k in movie_sentiment.keys():
        a = sum(movie_sentiment[k]) / len(movie_sentiment[k])
        # print(a)
        avg_sent[k] = a
    return avg_sent


pprint.pprint(avg_sent())


# average rating
def avg_rate():
    """ets the average of imdb_rating for each movie
    and then returns it in a dictionary"""
    movie_rating = {}

    for movie in sent_text: 
        rate_list = []
        for sub_list in movie['review_info']:
            rate = sub_list['imdb_rating']
            rate_list.append(rate)
        movie_rating[movie['movie_title']] =  rate_list
    # print(movie_rating)

    avg_rate = {}
    for k in movie_rating.keys():
        a = sum(movie_rating[k]) / len(movie_rating[k])
        # print(a)
        avg_rate[k] = a

    return avg_rate


pprint.pprint(avg_rate())
