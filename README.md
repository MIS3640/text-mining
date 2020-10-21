# text-mining

## Program Overview
This program is designed to harvest 1,000 tweets containing 'donald trump' from the Twitter API using Twython. It will remove urls, punctuation, numbers, emojis, and stop words from the tweets. The program will then run a computational analysis on the tweets. It will display a bar chart of the top 10 most frequently used words from the tweets as well as generate a word cloud that visualizes the most popular words in an interesting and informative way. The frequency of the words dictates the word size within the word cloud.  

## Program Instructions
To begin, left-click on the program and select "Run Python File In Terminal".
### Default Values
This program will run with a default of 1,000 tweets and 10 top words for the bar chart. The default stopwords are from nltk.corpus.stopwords and the customized stopwords are: rt, donald, trump, trumps, biden, bidens, republican, republicans, democrat, democrats, democratic, president. 
#### Change Custom Stopwords
The custom stopwords are located on lines 22-33. The user may change custom stopwords.
#### Change Number of Tweets
The number of tweets is located on line 37 and is controlled by "count=1000". The user may change the number of tweets.
#### Change Number of Top Words
The number of top words is located in the main() function on line 120 and is controlled by "num=10". The user may change the number of top words. 