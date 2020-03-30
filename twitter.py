import tweepy # Twitter API Library
import sys # Allow Python to interact with more functions
import re # Support regular expression (such as white space characters) through libraries 
import csv # Reading and writing data from CSV files
from textblob import TextBlob # Sentiment Analysis
import matplotlib.pyplot as plt # Data Visualization: plotting 


class SentimentAnalysis:

    def __init__(self):
        """
        allow the class to initialize the attributes of the class 
        when an object is created from the class.
        
        self is the newly created object, which has two lists to
        store data.
        """
        self.tweets = []
        self.tweetText = []

    def twitterData(self):
        """
        authenticating access key
        """
        apiKey = 'wsrpR3F0nCD5dk4kku7LzPMu9'
        apiSecret = 'QfUfxRoiaxrof2f37xENysPZSOsHhsZIxOZstnW6PNXojrKA79'
        accessToken = '1032033926552936449-aIi5NiSX9fSXIl4dlBXDyhUOq27XOv'
        accessTokenSecret = '05y2MazUtzUkpzfbWB5AkBJ5P0q57nwvUghLIbrvtJauH'
        auth = tweepy.OAuthHandler(apiKey, apiSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        # Generate user input
        word = input("Please enter keyword or hashtag: ")
        wordNumber = int(input("Enter how many tweets to analyze: "))
        print()

        # Find tweets, append data into a csv file, and convert the user's data into delimited strings
        self.tweets = tweepy.Cursor(api.search, q=word, lang = "en").items(wordNumber)
        csvFile = open('result.csv', 'a')
        csvWriter = csv.writer(csvFile)

        # Create variables to store sentiment analysis information
        polarity = 0
        positive = 0
        negative = 0
        neutral = 0

        for tweet in self.tweets:
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity 

            if (analysis.sentiment.polarity == 0): 
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 1):
                positive += 1
            elif (analysis.sentiment.polarity < 0 and analysis.sentiment.polarity >= -1):
                negative += 1


        # Save data into csv file and close it
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # Calculate the average number of reaction
        positive = self.percentage(positive, wordNumber)
        negative = self.percentage(negative, wordNumber)
        neutral = self.percentage(neutral, wordNumber)

        # Calculate the average number of reaction
        polarity = polarity / wordNumber

        # Show overall reaction
        print("Twitter's reaction on " + str(wordNumber) + " tweets of the search term: " + word + ".")
        print()
        print("Overall Reaction in Twitter: ")

        # Set calculation rules
        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0 and polarity <= 1):
            print("Positive")
        elif (polarity < 0 and polarity >= -1):
            print("Negative")

        # Show reaction details
        print()
        print("Reaction Report: ")
        print(str(positive) + "% positive reaction")
        print(str(negative) + "% negative reaction")
        print(str(neutral) + "% neutral reaction")

        self.plotPieChart(positive, negative, neutral, word, wordNumber)


    def cleanTweet(self, tweet):
        """
        Remove unnecessary thins in sentimental analysis
        """
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    def percentage(self, part, whole):
        """
        Calculate the percentage
        """
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def plotPieChart(self, positive, negative, neutral, word, wordNumber):
        """
        Draw pie chart
        """
        labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
        sizes = [positive, neutral, negative]
        colors = ['orange','blue','grey']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('Reaction on Twitter about ' + str(wordNumber) + ' tweets of the search term: ' + word + '.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()


if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.twitterData()