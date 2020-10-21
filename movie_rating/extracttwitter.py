from twython import Twython
import pickle
def twitter_extracter(movie, tweet_number=50):
    """extracts twitter posts related to input: movie, and # of tweets. outputs: pickle of tweets"""
    ###enters API keys###
    APP_KEY = "9iNbqBABwgvjucc9dE2pW7mTm"
    APP_SECRET = "PIVYIesOdEVCvrdQbI81YzrpPCdExhA32QkvsYefgSkijBKeZK"
    twitter = Twython(APP_KEY, APP_SECRET)
    ###searches###
    data = twitter.search(q=f"{movie} review", count=tweet_number)
    ###creates list of tweets###
    twitter_list = []
    for status in data["statuses"]:
        twitter_list.append(status["text"])
    ###pickles tweets###
    with open(f"{movie}_twitter.pickle", "wb") as f:
        pickle.dump(twitter_list, f)
def main():
    twitter_extracter("Mulan")
if __name__ == "__main__":
    main()
