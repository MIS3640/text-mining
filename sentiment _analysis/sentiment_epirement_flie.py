'''
this is an expiriemental file, it generates a twitter stream based on keywords
'''


import twitter_credentials # this file has my twitter API credentials: consumer key, consumer secret, access token, access secret.
import tweepy
import pandas as pd
import numpy as np

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# the general format for this code was found referencing the tweepy documentation.
 
auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret) # authentication object
auth.set_access_token(twitter_credentials.token, twitter_credentials.token_secret) # setting the access token & access token secret 


api = tweepy.API(auth) # creating API object that uses auth info

class listener(StreamListener):

    def on_data(self, data):
        
            print(data)
            save_file = open('twitterstream.csv','a')
            save_file.write(data)
            save_file.write('\n')
            save_file.close()
            return True

    def on_error(self, status):
        print(status)

words_search = ['trump' , 'donald trump', 'COVID-19']
twitterStream = Stream(auth, listener())
twitterStream.filter(languages=['en'], track=words_search)



if __name__ == "__main__":


    pass


