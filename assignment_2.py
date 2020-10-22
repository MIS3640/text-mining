#Importing Libraries Needed for Project
import pandas as pd
import numpy as np
import random
import seaborn as sns 
import requests
import urllib.request
import matplotlib.pyplot as plt

#Getting the Book From Guttenberg
url = 'http://www.gutenberg.org/files/61085/61085-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing

#Performing a Function to Find the Frequency of Each Word in the entire "In our Time" book
rs = requests.get('http://www.gutenberg.org/files/61085/61085-0.txt')

""" This function gets the amount of times (frequency) each word appears in the text
"""
if (rs.status_code == 200):
    wordlist = rs.text.lower().split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
    for word, freq in list(zip(wordlist, wordfreq)):
        print ("Word:  {} - Frequency: {}".format(word, freq))

#Putting this List of Frequencies into a DataFrame Format (so we can perform computational analysis)
data = {'word':wordlist ,'frequency':wordfreq}
df = pd.DataFrame(data)
#Dropping duplicate values from DataFrame
df.drop_duplicates(subset ="word", 
                     keep = "first", inplace = True) 
t = df.sort_values("frequency", ascending = False)
t

#Basic Information About the DataFrame
t.shape, 
t.index, 
t.columns, 
t.info(), 
t.count()

#Descriptive Statistics About the DataFrame
t.describe()

#Performing a Normal Distribution with the Data Above
mu, sigma = t.mean(), t.std()
norm_dist = np.random.normal(mu, sigma, 1996)

#Plotting the Normal Distribuition of the Frequency of Words in In our Time Book
sns.histplot(norm_dist)

#Distribution Plot of the Frequency (Count = Number of Words)
sns.displot(wordfreq)
plt.xlabel("Frequency of Word")
plt.ylabel("Count of Word")
plt.title("Frequency of Apperance per Amount of Words")

#BoxPlot to Confirm Outliers 
sns.boxplot(data= t, orient = 'h')