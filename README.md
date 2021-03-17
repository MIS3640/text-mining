Scary Story Text Analysis Bot

The goal of this program is to better understand how good horror stories are written, by analyzing popular submission on the subreddit "Nosleep"

Installation

The bot requires installation of praw (pip install praw) and nltk (pip install nltk). The nltk package requires a sentiment analysis download (nltk.download()). 

How to use general_word_frequency_analysis.py:

General_word_frequency_analysis.py is a file that focuses on analyzing the frequency of words in the 'nosleep' reddit posts. To find out what words are most commonly used in the horror stories, run the main() function. The main() function will output the most frequent words and their frequency. If you are interested in seeing the whole histogram of words and frequency, uncomment the commented functions inside of main().

How to use text_similarity.py

text_similarity.py is a file that focuses on analyzing similarities in word choice between popular horror stories. In order to run the analysis in the text_similarity.py file simply open the file and run it. Alternatively create a file and type "from text_similarity import main" and then on a second line type "main()". By running those two lines of code, the text similarity analysis will be printed.

How to use use natural_language_processing.py & headlines_nlp.py: 

Calling on the main function will execute the polarity analysis on the existing text code. The headline_analysis(incident, nameincident) can be used to analyze any dictionary containing key:value pairs that consist of a newspaper name, and an article fragment. 

How to run all files at once:

If you wish to run all of the files at once open the document "mainloops.py" and run it in vscode. This will run the main loops of all of the files in folder_1 and print out our full analysis.

Thank you for using our application!